from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if user_name=='' or email=='' or password=='':
            messages.warning(request, 'ຂໍ້ມູນບໍ່ຄົບ')
            return redirect('/register')
        else:
            if User.objects.filter(username = user_name).exists():
                messages.warning(request, 'ຜູ້ໃຊ້ນີ້ລົງທະບຽນແລ້ວ')
                return redirect('/register')
            else:
                obj_user = User.objects.create_user(
                username = user_name,
                email = email,
                password = password,
                # is_staff = True,
                # is_superuser = True
            )
            obj_user.save()
            
            messages.success(request, 'ລົງທະບຽນສຳເລັດແລ້ວ')
            return redirect('/register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        
        if user_name=='' or password=='':
            messages.warning(request, 'ຂໍ້ມູນບໍ່ຄົບ')
            return redirect('/login')
        else:
            user = auth.authenticate(username = user_name, password = password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.warning(request, 'ຊື່ຜູ້ໃຊ້ ຫລື ລະຫັດຜ່ານບໍ່ຖຶກຕ້ອງ')
                return redirect('/login')
        
    else:
        return render(request, 'login.html')

def loguot(request):
    auth.logout(request)
    return redirect('/login')