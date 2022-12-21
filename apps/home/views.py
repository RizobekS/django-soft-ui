# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.contrib import messages

from apps.home.forms import ContactForm


def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() and request.POST['address'] == "":
            form.save()
            name = request.POST['name']
            messages.success(request, 'Success!')
            return render(request, 'home/page-contact-us.html', {'name': name})
        else:
            name = " Ooops, something went wrong!"
            return render(request, 'home/page-contact-us.html', {'name': name})
    else:
        return render(request, 'home/page-contact-us.html', {})


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

