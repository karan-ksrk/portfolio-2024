from django.shortcuts import render
from .models import *


def home(request):

    context = {
        'portfolio': Portfolio.objects.get(is_active=True),
        'projects': Project.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'educations': Education.objects.all(),
        'experiences': Experience.objects.all().order_by('-start_date'),
        'social_links': SocialLink.objects.all(),
        'self_image': SelfImage.objects.get(is_active=True),
        'expertises': Expertise.objects.all().order_by('order')
    }
    return render(request, 'portfolio_1/index.html', context)
        