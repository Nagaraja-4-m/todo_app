from django.shortcuts import render, redirect
from .models import *
from .auth_decorators import check_authentication


# Create your views here.
def is_email_exist(email):
    try:
        status=Users.objects.filter(email__iexact=email).exists()  #if not exsists RETURNS FALSE'
        return status #means email already exists
    except:
        return None


# =================== view functions =====================
def login(request):
    
    if 'ssk_logged_user_id' in request.session:
        return redirect('/')

    if request.method=='POST':
        user_data=request.POST.dict()
        data={'redirect_url':'/','message':None}
       
        # email_varification_status
        if not is_email_exist(user_data['email']):
            data['message']=f'{user_data["email"]} not found!'
            return render(request,'alert.html',data)
        
        try:
            user_obj=Users.objects.filter(email__iexact=user_data['email']).get()
            if user_data['password']==user_obj.password:
                request.session['ssk_logged_user_id'] = user_obj.id  #session created
                return redirect('/dashboard')
            else:
                data['message']='Invalid password !'
                return render(request,'alert.html',data)
        except:
            data['message']='Unable to verify your credentials at this time!'
            return render(request,'alert.html',data)
    else:
        return redirect('/')


def registration(request):

    if request.method=='POST':
        user_data=request.POST.dict()
        email_varification_status=is_email_exist(user_data['email'])
        data={'redirect_url':'/','message':None}
        if email_varification_status:
            data['message']=f'{user_data["email"]} already exists!'
            return render(request,'alert.html',data)
        elif email_varification_status is None:
            data['message']='Unable to verify your email!, try later'
            return render(request,'alert.html',data)
        try:
            user_object=Users(
                    email=user_data['email'],
                    fullname=user_data['fullname'],
                    password=user_data['password'] )
            user_object.save()
            request.session['ssk_logged_user_id'] = user_object.id  #session created

        except Exception as e:
            data['message']=f'Unable to complete the request, Error: {str(e)}'
            return render(request,'alert.html',data)
        return redirect('/dashboard')

    else:
        return redirect('/')

def logout(request):
    try:
        request.session.pop('ssk_logged_user_id')
    except:
        del request.session
    return redirect('/')
