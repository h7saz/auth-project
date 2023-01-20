from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')

def loginpage(request):
    return render(request,'login.html')        

@login_required(login_url='login')
def about(request):
    return render(request,'about.html') 

def ucrt(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        username=request.POST['uname']
        password=request.POST['pwd']
        cpassword=request.POST['cpwd']
        email=request.POST['email']

        if password==cpassword: 
            if User.objects.filter(username=username).exists(): 
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    firstname=firstname,
                    lastname=lastname,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                
                print("Successed...")
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('login')
    else:
        return render(request,'signup.html')

def login(request):
	if request.method == 'POST':
		usname = request.POST['uname']
		prwd = request.POST['pwd']
		user = auth.authenticate(username=usname, password=prwd)
		if user is not None:
			auth.login(request, user)
			messages.info(request, f'Welcome {usname}')
			return redirect('about')
		else:
			messages.info(request, 'Invalid Username or Password. Try Again.')
			return redirect('loginpage')
	else:
		
		return redirect('loginpage')


@login_required(login_url='login')
def logout(request):
	auth.logout(request)
	return redirect('home')

