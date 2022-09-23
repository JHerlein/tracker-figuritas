import http
from itertools import count
from re import S
from django.shortcuts import render, redirect
from .models import UserStickers
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse
import time

# Create your views here.
@login_required(login_url='login')
def home(request):
    countries1 = [
    'FWC','QAT','ECU','SEN','NED','ENG','IRN','USA','WAL','ARG','KSA','MEX','POL','FRA','AUS','DEN','TUN'
    ]  

    countries2 = [
    'ESP','CRC','GER','JPN','BEL','CAN','MAR','CRO','BRA','SRB','SUI','CMR','POR','GHA','URU','KOR'
    ]   
    if request.method == "GET":
        #Search view
        # try:
                       
        #     search_text = request.GET.get('search_sticker')              
        #     request.session['search_sticker'] = search_text            
        #     user = User.objects.get(username=request.user)
        #     user_stickers = UserStickers.objects.filter(country__icontains=search_text,username=user.id).order_by('id')
        #     if search_text.upper() == 'FWC':
        #         paginator = Paginator(user_stickers, 30)
        #     if search_text.upper() != 'FWC':
        #         paginator = Paginator(user_stickers, 19)       
        #     page_number = request.GET.get('page')            
        #     page_obj = paginator.get_page(page_number)
        #     request.session['page_number'] = None
        #     return render(request,'base/home.html', {'page_obj':page_obj, 'user':user, 'countries1':countries1, 'countries2':countries2})
        # #Default view
        # except:        
        #     user = User.objects.get(username=request.user)
        #     user_stickers = UserStickers.objects.filter(username=user.id).order_by('id')
        #     paginator = Paginator(user_stickers, 19)
        #     page_number = request.GET.get('page')
        #     page_obj = paginator.get_page(page_number)
        #     if page_number is None:
        #         page_number = '1'
        #     request.session['page_number'] = page_number
        #     return render(request,'base/home.html', {'page_obj':page_obj, 'user':user, 'countries1':countries1, 'countries2':countries2})

                            
        search_text = request.GET.get('search_sticker')
        figuritas = request.GET.get('figuritas')        
        user = User.objects.get(username=request.user)
        if (search_text is None) and (figuritas is None):
            user_stickers = UserStickers.objects.filter(username=user.id).order_by('id')
            paginator = Paginator(user_stickers, 19)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            if page_number is None:
                page_number = '1'
            request.session['page_number'] = page_number
        if (search_text is not None) and (figuritas is not None) :
            user_stickers = UserStickers.objects.filter(country__icontains=search_text,username=user.id).order_by('id')
            request.session['search_sticker'] = search_text            
            paginator = Paginator(user_stickers, 19)
            page_number = request.GET.get('page')            
            page_obj = paginator.get_page(page_number)
            request.session['page_number'] = None
            if search_text.upper() == 'FWC':
                paginator = Paginator(user_stickers, 30)
            if search_text.upper() != 'FWC':
                paginator = Paginator(user_stickers, 19)
        if (search_text is not None) and (figuritas is None) :
            user_stickers = UserStickers.objects.filter(country__icontains=search_text,username=user.id).order_by('id')
            request.session['search_sticker'] = search_text
            paginator = Paginator(user_stickers, 19)
            page_number = request.GET.get('page')            
            page_obj = paginator.get_page(page_number)
            request.session['page_number'] = None
            if search_text.upper() == 'FWC':
                paginator = Paginator(user_stickers, 30)
            if search_text.upper() != 'FWC':
                paginator = Paginator(user_stickers, 19)
        if (search_text is None) and (figuritas is not None) :
            request.session['figuritas'] = figuritas
            nola = False
            if figuritas == 'nola':
                nola = True 
            if nola:
                user_stickers = UserStickers.objects.filter(count=0,username=user.id).order_by('id')
            if not nola:
                if figuritas == 'todas':
                    count_to_filter = 0
                if figuritas == 'late':
                    count_to_filter = 1
                if figuritas == 'repetidas':
                    count_to_filter = 2                           
                user_stickers = UserStickers.objects.filter(count__gte=count_to_filter,username=user.id).order_by('id')
            paginator = Paginator(user_stickers, 19)
            page_number = request.GET.get('page')            
            page_obj = paginator.get_page(page_number)
            request.session['page_number'] = None
            paginator = Paginator(user_stickers, 19)
        return render(request,'base/home.html', {'page_obj':page_obj, 'user':user, 'countries1':countries1, 'countries2':countries2})
    

@login_required(login_url='login')
def addSticker(request, pk, username):
    user = User.objects.get(username=username)
    if request.method == 'GET':
        user_stickers = UserStickers.objects.get(username=user.id,id_complete=pk)
        user_stickers.count += 1
        if user_stickers.count > 1:
            user_stickers.repeated = True
        if user_stickers.count <= 1:
            user_stickers.repeated = False        
        user_stickers.save()
        if request.session['page_number'] == None:
            url = reverse('home') + '?search_sticker=' + request.session['search_sticker']
        if request.session['page_number'] != None:
            url = reverse('home') + '?page=' + str(request.session['page_number'])        
        return redirect(url)

@login_required(login_url='login')
def subSticker(request, pk, username): 
    user = User.objects.get(username=username)
    if request.method == 'GET':
        user_stickers = UserStickers.objects.get(username=user.id,id_complete=pk)
        if user_stickers.count == 0:
            return(redirect('home'))
        user_stickers.count -= 1
        if user_stickers.count > 1:
            user_stickers.repeated = True
        if user_stickers.count <= 1:
            user_stickers.repeated = False        
        user_stickers.save()
        if request.session['page_number'] == None:
            url = reverse('home') + '?search_sticker=' + request.session['search_sticker']
        if request.session['page_number'] != None:
            url = reverse('home') + '?page=' + str(request.session['page_number'])        
        return redirect(url)
        

def loginURL(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')           
            
    context = {}
    return render(request,'base/login.html', context)

def register(request):
    countries = [

    'QAT','ECU','SEN','NED','ENG','IRN','USA','WAL','ARG','KSA','MEX','POL','FRA','AUS','DEN','TUN','ESP',
    'CRC','GER','JPN','BEL','CAN','MAR','CRO','BRA','SRB','SUI','CMR','POR',
    'GHA','URU','KOR'

    ]

    id_completed = []

    for country in countries:
        for i in range(1,20):
            id = country + ' ' +str(i)
            id_completed.append(id)

    for i in range(0,30):
            id =  'FWC ' +str(i)
            id_completed.append(id)    

    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            time.sleep(1)
            print(request)
            user = User.objects.get(username=request.POST.get('username'))            
            for figurita in id_completed:
                country = figurita[:3]
                objecto = UserStickers(id_complete=figurita,username=user, country = country)
                objecto.save()
            messages.success(request,'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('login')
    context = {'form':form}
    return render(request,'base/register.html',context)
        
        
def logoutUser(request):
    logout(request)
    return redirect('login')

def getUser(request):
    if request.method == 'POST':
        search_user = request.POST.get('search_user')
        users = User.objects.filter(username__icontains=search_user)
        return render(request,'base/user_finder.html', {'users':users})
    return render(request,'base/user_finder.html')
        

def userPublicProfile(request, username):
    countries1 = [
    'FWC','QAT','ECU','SEN','NED','ENG','IRN','USA','WAL','ARG','KSA','MEX','POL','FRA','AUS','DEN','TUN'
    ]  

    countries2 = [
    'ESP','CRC','GER','JPN','BEL','CAN','MAR','CRO','BRA','SRB','SUI','CMR','POR','GHA','URU','KOR'
    ]   
    if request.method == "GET":
        #Search view
        try:            
            search_text = request.GET.get('search_sticker')              
            request.session['search_sticker'] = search_text            
            user = User.objects.get(username=username)
            user_stickers = UserStickers.objects.filter(country__icontains=search_text,username=user.id).order_by('id')
            if search_text.upper() == 'FWC':
                paginator = Paginator(user_stickers, 30)
            if search_text.upper() != 'FWC':
                paginator = Paginator(user_stickers, 19)       
            page_number = request.GET.get('page')            
            page_obj = paginator.get_page(page_number)
            request.session['page_number'] = None
            return render(request,'base/profile.html', {'page_obj':page_obj, 'user':user, 'countries1':countries1, 'countries2':countries2})
        #Default view
        except:        
            user = User.objects.get(username=username)
            user_stickers = UserStickers.objects.filter(username=user.id).order_by('id')
            paginator = Paginator(user_stickers, 19)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            if page_number is None:
                page_number = '1'
            request.session['page_number'] = page_number
            return render(request,'base/profile.html', {'page_obj':page_obj, 'user':user, 'countries1':countries1, 'countries2':countries2})


def getExchangeStickers(request, username):
    user1 = User.objects.get(username=request.user)
    user_stickers1 = UserStickers.objects.filter(username=user1.id,count__exact=0).values('id_complete')
    user2 = User.objects.get(username=username)    
    user_stickers2 = UserStickers.objects.filter(username=user2.id, count__gte=2, id_complete__in = user_stickers1)    
    context = {'user_stickers2':user_stickers2,'user2':user2}
    return render(request,'base/exchange.html', context)

def getSticker(request):
    search_sticker = request.POST.get('search_sticker')
    search_checkbox = request.POST.get('checkbox-nolas')
    print(search_checkbox)    
    if (request.method == 'POST') & (search_sticker != None) & (search_checkbox == None):
        print('1 if')
        try:            
            new_list = request.session['stickers_to_find']
            new_list.append(search_sticker)
            request.session['stickers_to_find'] = new_list
        except:
            request.session['stickers_to_find'] = [search_sticker]
        return render(request,'base/sticker_finder.html', {'sticker_session':request.session['stickers_to_find']})
    if (request.method == 'POST') & (search_sticker == None) & (search_checkbox == None):
        print('Second if')
        users = UserStickers.objects.filter(id_complete__in=request.session['stickers_to_find'], count__gte=2)
        usernamesWithStickers = {}
        for user in users:
            print('for')
            print('id complete',user.id_complete)
            print('keys',usernamesWithStickers.keys())
            if user.username not in usernamesWithStickers.keys():
                usernamesWithStickers[user.username] = {}
                usernamesWithStickers[user.username]['count'] = 1
                usernamesWithStickers[user.username]['stickers'] = [user.id_complete]
            else:
                usernamesWithStickers[user.username]['count'] += 1
                usernamesWithStickers[user.username]['stickers'].append(user.id_complete)
        request.session['stickers_to_find'] = []        
        list_of_sorted_keys = sorted(usernamesWithStickers, key=lambda x: usernamesWithStickers[x]['count'], reverse=True)
        return render(request,'base/sticker_finder.html', {'users':usernamesWithStickers, 'sortedKeys':list_of_sorted_keys})
    if (request.method == 'POST') & (search_sticker == None) & (search_checkbox == 'on'):
        print('3 if')
        stickers_to_find = UserStickers.objects.filter(username=request.user, count=0).values('id_complete')
        print(stickers_to_find)
        users = UserStickers.objects.filter(id_complete__in=stickers_to_find, count__gte=2)
        print(users)
        usernamesWithStickers = {}
        for user in users:
            print('for')
            print('id complete',user.id_complete)
            print('keys',usernamesWithStickers.keys())
            if user.username not in usernamesWithStickers.keys():
                usernamesWithStickers[user.username] = {}
                usernamesWithStickers[user.username]['count'] = 1
                usernamesWithStickers[user.username]['stickers'] = [user.id_complete]
            else:
                usernamesWithStickers[user.username]['count'] += 1
                usernamesWithStickers[user.username]['stickers'].append(user.id_complete)
        request.session['stickers_to_find'] = []        
        list_of_sorted_keys = sorted(usernamesWithStickers, key=lambda x: usernamesWithStickers[x]['count'], reverse=True)
        return render(request,'base/sticker_finder.html', {'users':usernamesWithStickers, 'sortedKeys':list_of_sorted_keys})

    return render(request,'base/sticker_finder.html')


def importBulk(request):
    bulk_import = request.POST.get('bulk_import')    
    if request.method == 'POST':        
        user = User.objects.get(username=request.user)
        for sticker in bulk_import.split(','):
            print(sticker)
            user_sticker = UserStickers.objects.get(username=user.id,id_complete=sticker)
            user_sticker.count += 1
            if user_sticker.count > 1:
                user_sticker.repeated = True
            user_sticker.save()
        messages.success(request,'Stickers imported sucessfully')
        return redirect('bulk')

    return render(request,'base/bulk_import.html',{})

def exchangeRequest(request,username):
    user1 = User.objects.get(username=request.user)
    user_stickers1 = UserStickers.objects.filter(username=user1.id,count__exact=0).values('id_complete')
    user2 = User.objects.get(username=username)    
    user_stickers2 = UserStickers.objects.filter(username=user2.id, count__gte=2, id_complete__in = user_stickers1)    
    context = {'user_stickers2':user_stickers2,'user2':user2}
    return render(request, 'base/exchange_request.html', context)

def lobbyChat(request):
    return render(request, 'base/lobby.html')

    