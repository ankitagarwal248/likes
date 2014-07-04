from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, redirect, render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.templatetags.static import static
from collections import Counter
from django.core.context_processors import csrf
from datetime import datetime
from likes.models import *
from likes.forms import UserForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import urlparse
import urllib
from django.utils.safestring import mark_safe
from decimal import Decimal
from likes.utils.postutils import *

def index(request):
    user = request.user

    context = {
        
    }
    return render(request, 'likes/index.html', context)


def user_register(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    context = RequestContext(request)
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user_login(request)
            return HttpResponseRedirect('/')
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    return render_to_response('likes/register.html', {'user_form': user_form}, context)

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your Likes account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            messages.warning(request, 'Invalid Login Details')
            return render_to_response('likes/login.html', {}, context)
    else:
        return render_to_response('likes/login.html', {}, context)


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')



@login_required(login_url='/login/')
def advertiser(request):
    user = request.user
    campaigns = user.campaign_set.all()

    context = {
        'campaigns': campaigns
    }
    return render(request, 'likes/advertiser.html', context)
    

@login_required(login_url='/login/')
def create_campaign(request):
    user = request.user
    if request.method =='POST':
        link = request.POST['link'].strip()
        title =  request.POST['title'].strip()
        description = request.POST['description'].strip()
        keywords = request.POST['keywords']
        bid = Decimal(request.POST['bid'].strip())
        budget = Decimal(request.POST['budget'].strip())
        status = 0
        campaign = Campaign(user=user, link=link, title=title, description=description, keywords=keywords, bid=bid, budget=budget)    
        campaign.save()
    return HttpResponseRedirect('/advertiser/')

@login_required(login_url='/login/')
def activate_campaign(request, id):
    campaign = Campaign.objects.get(pk=id)
    campaign.status = 1
    campaign.save()
    return HttpResponseRedirect('/advertiser/')


@login_required(login_url='/login/')
def deactivate_campaign(request, id):
    campaign = Campaign.objects.get(pk=id)
    campaign.status = 0
    campaign.save()
    return HttpResponseRedirect('/advertiser/')

@login_required(login_url='/login/')
def delete_campaign(request, id):
    campaign = Campaign.objects.get(pk=id).delete()
    return HttpResponseRedirect('/advertiser/')


@login_required(login_url='/login/')
def publisher(request):
    user = request.user
    posts = user.post_set.all()

    context = {
        'posts': posts
    }
    return render(request, 'likes/publisher.html', context)             



@login_required(login_url='/login/')
def create_post(request):
    user = request.user
    if request.method =='POST':
        post_url = request.POST['url'].strip()
        post_dict = get_postinfo(post_url)
        
        post_title = post_dict['title']
        post_image = post_dict['image']
        post_content = post_dict['content']

    post = Post(user=user, url=post_url, title=post_title, image=post_image, content=post_content)
    post.save()
    return HttpResponseRedirect('/publisher/')   





@login_required(login_url='/login/')
def delete_post(request, id):
    pass



@login_required(login_url='/login/')
def page(request):
    pass        