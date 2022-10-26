from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from first.models import Store, Room, Messaging
from datetime import datetime
# Create your views here.


def check(request):
    try:
        request.session['logged']
    except Exception as e:
        request.session['logged'] = False
    try:
        request.session['usering']
    except Exception as e:
        request.session['usering'] = 'none'


def home(request):
    check(request)
    hell = 'Your'
    hell_sec = 'no'
    no_data = True
    if request.session['logged']:
        hell = request.session['usering']
        hell_sec = 'yes'
        finale = Store.objects.filter(userid=request.session['usering'])
        if len(finale) > 0:
            no_data = False
        context = {
            'use': hell,
            'use_sec': hell_sec,
            'datu': no_data,
            'dat': finale
        }
        return render(request, "home.html", context)
    context = {
        'use': hell,
    }
    return render(request, "home.html", context)


def profile(request):
    if request.session['logged']:
        context = {
            'kul': 'You Are Logged in'
        }
        return render(request, "users.html", context)
    return render(request, "users.html")


def login(request):
    check(request)
    if not request.session['logged']:
        dat = 'You Are One step behind using our services'
        if request.method == 'POST':
            name = request.POST.get('use')
            passu = request.POST.get('passed')

            user = authenticate(username=name, password=passu)
            if user is not None:
                request.session['logged'] = True
                request.session['usering'] = user.get_username()
                return redirect('home')
            else:
                dat = 'Invalid Password or Username'
        context = {
            'kul': dat
        }
        return render(request, "login.html", context)
    return HttpResponse("You Are Already Logged My Boy First Logout by going in profile")


def signup(request):
    check(request)
    if not request.session['logged']:
        dat = 'One Step Behind Joining Our Community'
        if request.method == 'POST':
            user_name = request.POST.get('use')
            password = request.POST.get('passed')
            pass_verify = request.POST.get('passed_v')
            if user_name == "" or password == "" or pass_verify == "":
                return render(request, "signup.html", {'kul': "All the fields must be filled"})
            if str(password) == str(pass_verify):
                myone = User.objects.create(
                    username=user_name, password=pass_verify)
                myone.first_name = user_name
                myone.set_password(str(password))
                myone.save()
                return redirect('login')
            else:
                dat = 'Both Password Fields Must Be Same'

        context = {
            'kul': dat
        }

        return render(request, "signup.html", context)
    return HttpResponse("You Are Already Logged in My Boy First Logout by going in profile")


def logout(request):
    del request.session['logged']
    del request.session['usering']
    return redirect('login')


def add_pass(request):
    check(request)
    dat = "One Step Behind Of Adding Your Password"
    if request.session['logged']:
        if request.method == 'POST':
            tit = request.POST.get('use')
            passes = request.POST.get('passed')

            if str(tit) != '' and str(passes) != '':
                finale = Store.objects.filter(title=tit)
                if len(finale) == 0:

                    adder = Store(userid=request.session['usering'], title=tit, passes=str(
                        passes), date=datetime.today())
                    adder.save()
                    return redirect('home')
                else:
                    dat = " Password with This Name Already Exist"
                    context = {
                        'kul': dat
                    }
                    return render(request, "add_pass.html", context)
            else:
                dat = "Both the Fields Must Be Filled !!!"
                context = {
                    'kul': dat
                }
                return render(request, "add_pass.html", context)
    else:
        redirect('profile')
    context = {
        'kul': dat
    }
    return render(request, "add_pass.html", context)


def del_pass(request):
    check(request)
    if request.session['logged']:
        if request.method == 'POST':
            title = request.POST.get('tiu')
            dat = Store.objects.get(title=str(title))
            dat.delete()
            return redirect('home')
    return redirect('home')


def edit_pass(request, slug):
    check(request)
    dat = "One Step Behind Of Editing Your Password"
    if request.session['logged']:
        if request.method == 'POST':
            title = request.POST.get('use')
            pasy = request.POST.get('passed')

            if str(title) != '' and str(pasy) != '':
                obj = Store.objects.filter(title=title)
                if len(obj) == 0:
                    dat = 'Password With this title does not Exist'
                    context = {
                        'kul': dat
                    }
                    return render(request, "editpass.html", context)
                else:
                    obj.update(title=title, passes=pasy)
                    dat = "Password Updated Successfully"
                    context = {
                        'kul': dat
                    }
                    return redirect('/')
            else:
                dat = "Both the Fields Must be Filled"
                context = {
                    'kul': dat
                }
                return render(request, "editpass.html", context)
        context = {
            'kul': dat,
            'slug_str': " ".join(str(slug).split("-"))
        }
        return render(request, "editpass.html", context)
    else:
        return redirect('profile',)


def room(request):
    check(request)
    if request.method == 'POST':
        roo = request.POST.get('roname')
        use = request.POST.get('yoname')
        if str(roo) != '' and str(use) != '':
            print(roo, use)
            if Room.objects.filter(name=roo).exists():
                myroom = Room.objects.get(name=roo)
                myroom.usenum += 1
                myroom.save()
                request.session['chat_name'] = str(use)
                return redirect(f'room/{roo}')
            else:
                myroom = Room.objects.create(name=roo)
                myroom.usenum += 1
                myroom.save()
                request.session['chat_name'] = str(use)
                return redirect(f'room/{roo}')
        return render(request, 'room.html')
    else:
        return render(request, 'room.html')


def sluggu(request, slug):
    legion = Room.objects.get(name=slug)
    mams = Messaging.objects.filter(roo_name=slug)
    context = {
        'gul': slug,
        'gul_sec': legion.usenum,
        'player': f"{request.session['chat_name']}-enter-your-message",
        'drax': mams
    }
    return render(request, 'chat.html', context)


def send(request):
    if request.method == 'POST':
        chattu = request.POST.get('chatdat')
        mamu = request.POST.get('garaj')
        if str(chattu) != '':
            mess = Messaging.objects.create(
                userid=request.session['chat_name'], message=chattu, date=datetime.today(), roo_name=mamu)
            mess.save()
            request.build_absolute_uri('')
            return redirect(f"/room/{mamu}")
        request.build_absolute_uri(f'')
        return redirect(f"/room/{mamu}")
