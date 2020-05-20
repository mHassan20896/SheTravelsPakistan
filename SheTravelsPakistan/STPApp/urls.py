from django.urls import path
from STPApp import views

app_name = 'STP'

urlpatterns = [
    path('about/',views.AboutView.as_view(),name='about'),
    path('destination/',views.DestinationListView.as_view(),name='destination'),
    path('blogs/',views.BlogListView.as_view(),name='blog-list'),
    path('blog/(?P<pk>\d+)',views.BlogDetailView.as_view(),name='blog'),
    path('career/',views.CareerView.as_view(),name='career'),
    path('guide-registration/',views.guide_registration,name='guide-registration'),
    path('career/(?P<pk>\d+)',views.CareerDetailView.as_view(),name='job-description'),
    path('package/<package_title>/',views.get_quotation,name='quotation'),
    path('package/',views.PackageView.as_view(),name='package'),
]
