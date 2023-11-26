from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Author,Profile,Paper
from django.utils.text import slugify

@receiver(post_save,sender=Author)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(author=kwargs['instance'])


@receiver(signal=post_save, sender=Paper)
def generate_slug_for_product(sender,**kwargs):
    if not kwargs['instance'].slug:
        kwargs['instance'].slug=slugify(kwargs['instance'].title)
        kwargs['instance'].save()






