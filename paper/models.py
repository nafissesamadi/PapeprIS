from django.db import models
from account.models import User




# Create your models here.

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class FieldResearch(models.Model):
    title = models.CharField(max_length=300, db_index=True)
    url_title = models.CharField(max_length=300, db_index=True, null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Activated or Not')
    is_delete = models.BooleanField(verbose_name='Deleted or Not')

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name='Research Field'

class Publication(models.Model):
    name = models.CharField(max_length=500, verbose_name='Publication Name', null=True)
    issn = models.CharField( max_length=8, null=True,verbose_name='ISSN', unique=True)
    description=models.TextField(null=True, blank=True,verbose_name='Description')
    is_active = models.BooleanField(verbose_name='Activated or Not')
    is_delete = models.BooleanField(verbose_name='Deleted or Not')

    class Meta:
        verbose_name='Publication'

    def __str__(self):
        return self.name

class JournalPublication(Publication):
    PAPER_RANK = (
        ('Q1', 'Q1'),
        ('Q2', 'Q2'),
        ('Q3', 'Q3'),
        ('Q4', 'Q4'),
    )
    rank = models.CharField(max_length=10, choices=PAPER_RANK, db_index=True)
    depending_institute=models.CharField(max_length=300,null=True)


class ConferencePublication(Publication):
    holding_location = models.CharField(max_length=300, null=True,blank=True)
    holding_data=models.DateField(null=True,blank=True)




class Author(User):
    affiliation=models.CharField(max_length=300)

    class Meta:
        verbose_name='Author'


    def __str__(self):
        return f"{self.username}"

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(default=0)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.author}"



class PaperTag(models.Model):
    keyword = models.CharField(max_length=300, db_index=True)

    class Meta:
        verbose_name = 'Paper Keyword'

    def __str__(self):
        return self.keyword

class Paper(models.Model):
    title = models.CharField(max_length=300)
    field_research = models.ForeignKey(
        FieldResearch,
        on_delete=models.CASCADE,
        related_name='paper_field',
        verbose_name='Field of Research')
    authors=models.ManyToManyField(
        Author,
        related_name='Auth_paper',
        verbose_name='Authors')
    abstract = models.TextField(verbose_name='Abstract', db_index=True)
    keywords = models.ManyToManyField(PaperTag, related_name='paper_tags')
    citation = models.IntegerField(verbose_name='Citation', null=True)
    doi = models.CharField(max_length=360, db_index=True, null=True, blank=True ,verbose_name='DOI', unique=True)
    slug = models.SlugField(default="", null=True, blank=True,db_index=True, max_length=200)
    PAPER_TYPE = (
        ('Conf', 'Conference'),
        ('Jour', 'Journal')
    )
    type = models.CharField(max_length=10, choices=PAPER_TYPE, db_index=True)
    published_in = models.ForeignKey(Publication,on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=False, verbose_name=' Activated or Not')
    is_delete = models.BooleanField(verbose_name=' Deleted or Not')

    class Meta:
        verbose_name='Paper'
        verbose_name_plural= 'Papers'


    def get_absolute_url(self):
        return reverse('paper-detail', args=[self.slug])



    def __str__(self):
        return f"{self.title} ({self.authors.all()})"


