import os
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from App_F.forms import User_Registration
from App_F.models import User, Post
from App_F.forms import User_Login
from App_F.forms import Post_Form
from App_F.models import Information
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return HttpResponse('Welcome Home')


def user_Registration(request):
    template = 'user/registration.html'
    form = User_Registration
    context = {'user': form}
    if request.method == "POST":
        users = User()
        users.first_name = request.POST.get('first_name')
        users.last_name = request.POST.get('last_name')
        users.email = request.POST.get('email')
        users.password = request.POST.get('password')
        users.contact = request.POST.get('contact')
        users.city = request.POST.get('city')
        users.save()
        context.setdefault('reg_suc', 'Succesfully registered')
        return render(request, template, context)
    else:
        return render(request, template,context)


def user_Login(request):
    form = User_Login
    if request.method == "POST":
        try:
            users = User.objects.get(email=request.POST.get('email'))
            if request.POST.get('password') == users.password:
                request.session['session_email'] = users.email

                if request.session.has_key('session_email'):
                    template = 'user/dashboard.html'
                    context = {'login': form}
                    return render(request, template, context)
                else:
                    template = 'user/login.html'
                    context = {'login': form, 'sess_unsuc': 'Access Forbidden'}
                    return render(request, template, context)
            else:
                template = 'user/login.html'
                context = {'login': form, 'log_unsuc': 'Email or Password does not match'}
                return render(request, template, context)
        except:
            template = 'user/login.html'
            context = {'login': form, 'invalid': 'Account does not Exist'}
            return render(request, template, context)
    else:
        template = 'user/login.html'
        context = {'login': form}
        return render(request, template, context)

def contact(request):
    if request.session.has_key('session_email'):
        if request.method == "POST":
            user = Information()
            user.fname = request.POST.get('fname')
            user.lname = request.POST.get('lname')
            user.gmail = request.POST.get('gmail')
            user.city = request.POST.get('city')
            user.phone = request.POST.get('phone')
            user.save()
            context = {'contact_suc': 'Succesfully Created'}
            context.setdefault("contact_unsuc", "Error")
            return render(request, 'user/contact.html', context)
        else:
            return render(request, 'user/contact.html')
    else:
        form = User_Login
        context = {'login': form, 'sess_unsuc': 'Access Forbidden'}
        return render(request, 'user/login.html', context)

def percentage(request):
    all = ''
    try:
        if request.method=="POST":
            fnum = eval(request.POST.get('num'))
            percent = eval(request.POST.get('percent'))
            all = fnum / 100 * percent
    except:
        pass
    return render(request, 'user/percentage.html', {'all': all})


def logout(request):
    form = User_Login
    if request.session.has_key('session_email'):
        del request.session['session_email']
        return HttpResponseRedirect('/login')
    else: 
        template = 'user/login.html'        
        context = {'login': form}
        return render(request, template, context)
        

def create_Post(request):
    if request.session.has_key('session_email'):
        template = 'post/create.html'
        form  = Post_Form
        context = {'post': form}
        if request.method == "POST":
            post = Post()
            if len(request.FILES) != 0:
                post.post_image = request.FILES['post_image']
            post.post_title = request.POST.get('post_title')
            post.post_description = request.POST.get('post_description')
            post.post_status = request.POST.get('post_status')
            post.save()
            return redirect('/index')
        else: 
            return render(request, template, context)
    else:
        template = 'user/login.html'
        form = User_Login
        context = {'login': form, 'sess_unsuc': 'Access Forbidden'}
        return render(request, template, context)


def dashboard(request):
    form = User_Login
    if request.session.has_key('session_email'):
        return render(request, 'user/dashboard.html')
    else:
        template = 'user/login.html'
        form = User_Login
        context = {'login': form, 'sess_unsuc': 'Access Forbidden'}
        return render(request, template, context)


def index_Post(request):
    if request.session.has_key('session_email'):
        template = 'post/index.html'
        form = Post.objects.all()
        context = {'post': form}
        return render(request, template, context)
    else:
        template = 'user/login.html'
        form = User_Login
        context = {'login': form, 'sess_unsuc': 'Access Forbidden'}
        return render(request, template, context)

def edit_Post(request, post_id):
    if request.session.has_key('session_email'):
        template = 'post/edit.html'
        ep = Post.objects.get(id=post_id)
        context = {'post': ep}
        return render(request, template, context)
    else:
        template = 'user/login.html'
        form = User_Login
        context = {'login': form, 'sess_unsuc': 'Access Forbidden'}
        return render(request, template, context)


def update_Post(request, post_id):
    template = 'post/edit.html'
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        if len(post.post_image) > 0:
            os.remove(post.post_image.path)
        post.post_title = request.POST.get('post_title')
        post.post_description = request.POST.get('post_description')
        post.post_status = request.POST.get('post_status')
        post.save()
        return redirect('/index')
    else:
        return render(request, template)

    
    

def show_Post(request, post_id):
    if request.session.has_key('session_email'):
        template = 'post/show.html'
        sp = Post.objects.get(id=post_id)
        context = {'post': sp}
        return render(request, template, context)
    else:
        template = 'user/login.html'
        form = User_Login
        context = {'login': form, 'sess_unsuc': 'Access Forbidden'}
        return render(request, template, context)

def delete_Post(request, post_id):
    if request.session.has_key('session_email'):
        template = 'post/index.html'
        dp = Post.objects.get(id=post_id)
        dp.delete()
        np = Post.objects.all()
        context = {'post': np}
        return render(request, template, context)
    else:
        template = 'user/login.html'
        form = User_Login
        context = {'login': form, 'sess_unsuc': 'Access Forbidden'}
        return render(request, template, context)

def search_Post(request):
        template = 'post/index.html'
        if request.session.has_key('session_email'):
            if request.method=="GET":
                query = request.GET['query']
                sp = Post.objects.filter(post_title__icontains = query)
                context = {'post': sp}
                return render(request, template, context)
            else:
                sp = Post.objects.all()
                context = {'post': sp}
                return render(request, template, context)
        else:
            template = 'user/login.html'
            form = User_Login
            context = {'login': form, 'sess_unsuc': 'Access Forbidden'}
            return render(request, template, context)




def calculator(request):
    if request.session.has_key('session_email'):
        total = ''
        try:
            if request.method=="POST":
                first = eval(request.POST.get('fnum'))
                last = eval(request.POST.get('lnum'))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                opr = request.POST.get('operator')
                if opr == "+":
                    total = first+last
                elif opr == "-":
                    total = first-last
                elif opr == "*":
                    total = first*+last
                elif opr == "/":
                    total = first/last
        except:
            pass
        return render(request,  'user/calculator.html', {'total': total})
    else:
        template = 'user/login.html'
        form = User_Login
        context = {'login': form, 'sess_unsuc': 'Access Forbidden'}
        return render(request, template, context)

 