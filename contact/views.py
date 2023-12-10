from django.shortcuts import render,redirect
from .forms import ContactUsModelForm
from .models import ContactUs
from django.views import View

# Create your views here.
# region Function base view
def contact_us_page(request):
    if request.method=="POST":
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            # print (contact_form.cleaned_data)
            # contact=ContactUs(
            #     title=contact_form.cleaned_data.get('title'),
            #     full_name=contact_form.cleaned_data.get('full_name'),
            #     email=contact_form.cleaned_data.get('email'),
            #     message=contact_form.cleaned_data.get('message'),
            # )
            contact_form.save()
            return redirect('home-page')
    else:
        contact_form=ContactUsModelForm()
        return render(request, 'contact/contact_us_page.html', {'contact_form': contact_form})
#endregion

#Region class base view
class ContactUsView(View):
    def get(self,request):
        contact_form=ContactUsModelForm()
        return render(request, 'contact/contact_us_page.html', {'contact_form': contact_form})
    def post(self,request):
        contact_form=ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('home-page')
        return render(request, 'contact/contact_us_page.html', {'contact_form': contact_form})


#endregion