from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from appAdmin.models import register
from appAdmin.forms import registerForm
# Create your views here.
def signup(request):
    title="Register"
    form=registerForm()
    context={'title':title,
        'form':form,
    }
    
    if request.method=='POST':
        form=registerForm(request.POST or None)
        
        if form.is_valid():
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'index.html',{'error':'Username already been taken'})
            except User.DoesNotExist:
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                
                mobile = form.cleaned_data['mobile']
                city = form.cleaned_data['city']
                address = form.cleaned_data['address']
                module = form.cleaned_data['module']
                userProfile = register(user=user, mobile=mobile, city=city, address=address, module=module)
                userProfile.save()
                saved=True
                print('status-------', userProfile.save())
                context={'saved':saved,'form':form}
                return render(request, 'index.html', context)
        else:
            print("Form invalid")
            saved=False
            form=registerForm()
            context={'saved':saved,'form':form,'error':'Something went wrong,fill the form correctly'}
            return render(request, 'index.html', context)
        
    else:
        return render(request, 'index.html', context)


def login(request):
    title="Login"
    context={'title':title}
    if request.method=='POST':
        user=auth.authenticate(username=request.POST.get('loginUsername'),password=request.POST.get('loginPassword'))
        
        userType=register.objects.filter(user=user)
        for userT in userType:
            print(userT.module)
        if user is not None:
            request.session['username']=request.POST.get('loginUsername')
            auth.login(request,user)
            if userT.module == "Owner":
                return redirect("owner:home")
            elif userT.module == "User":
                return redirect("user:home")
            elif userT.module=="tpa":
                return redirect("tpa:home")
            elif userT.module=="admin":
                return redirect('adminApp:adminHome')
            elif userT.module=="espdsp":
                return redirect('encdec:home')
            elif userT.module=="cloud":
                return redirect('cloud:home')
        else:
            return render(request,'index.html',{'error':'Username or password is incorrect'})
    else:
        return render(request,'index.html',context)

def logout(request):
    context={'title':'logout'}
    auth.logout(request)
    return redirect("adminApp:register")

   




    