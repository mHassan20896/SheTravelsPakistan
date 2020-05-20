from django.shortcuts import render,HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView,View, ListView, DetailView
from STPApp.models import Package, TripCategory, Destination, Comment, TeamMember
from STPApp.forms  import ClientForm,TravelGuideForm
from django.core.mail import send_mail
from django.conf import settings
from  django.urls import reverse
from STPApp.models import Blog,Career

from django.shortcuts import get_object_or_404


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pckg1 = Package.objects.get(id=1)

        context["pckg1"] = Package.objects.get(id=1)
        context["pckg2"] = Package.objects.get(id=2)
        context["pckg3"] = Package.objects.get(id=3)
        context["team_members"] = TeamMember.objects.all()
        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.all()
        context['team_members'] = TeamMember.objects.all()
        return context


class DestinationListView(ListView):
    model = Destination
    template_name = "destination.html"

class BlogListView(ListView):
    model = Blog
    template_name = "blogs.html"

class BlogDetailView(DetailView):
    model = Blog
    template_name = "selected-blog.html"

class CareerView(ListView):
    model = Career
    template_name = "Career.html"

class CareerDetailView(DetailView):
    model = Career
    template_name = "job-description.html"

class PackageView(TemplateView):
    template_name = "packages.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["packages"] = Package.objects.all()
        context["trip_categories"] = TripCategory.objects.all()
        return context

class SelectedBlogView(TemplateView):
    template_name = "selected-blog.html"


def guide_registration(request):
    if request.method == 'POST':
        form = TravelGuideForm(request.POST)
        print(form)
        if form.is_valid():
            travel_guide = form.save()
            subject = 'TOUR GUIDE REGISTRATION'
            message = 'Travel Guide of\n name {} \nand\nemail {}\nhas regitered.'.format(travel_guide.name,travel_guide.email)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['s@b.com',]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'index.html')
        else:
            return HttpResponse('Error')
    else:
        form = TravelGuideForm()
        return render(request,'GuideRegistration.html',{'form':form})


def get_quotation(request,package_title):
    package = get_object_or_404(Package, title=package_title)
    if package_title:
        if request.method == 'POST':
            form = ClientForm(request.POST)
            if form.is_valid():
                client = form.save()
                subject = 'She Travels Pakistan Client Registration'
                message = 'Client Name: {}\nMobile #: {}\nEmail: {}\nThis client filled out the form for {} package'.format(client.name,client.contact,client.email,package_title)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['a@b.com',]
                send_mail( subject, message, email_from, recipient_list )
                return HttpResponseRedirect(reverse('index'))


        form = ClientForm()
        return render(request, 'client-registration.html',{'form':form})

    else:
        raise Http404('hello')
