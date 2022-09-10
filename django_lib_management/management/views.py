from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from . import models
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django/views.generic import UpdateView, Deleteview
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

# Create your views here.

# Providing choices while register
def create_user(request):
	choice = ['Admin', 'Student']
	choice = {'choice':choice}

	return render(request, 'management/create_user.html', choice)


# Login view will automatically handle the login with email as in models
# class LoginView(auth_views.LoginView):
#     form_class = LoginForm
#     template_name = 'management/adminlogin.html'
#     success_url = reverse_lazy('homepage')

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def loginView(request):
	if request.method == 'POST':
		username = request.POST['email']
		password = request.POST['password']
		user = authenticate(request, username=email, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			if user.is_admin:
				return redirect('homepage')
			elif user.is_student:
				return redirect('#')
		else:
		    messages.info(request, "Please register")
		    return redirect('register')
'''
after successfull registration user can login 
if the user is registered as admin it will redirected to hompage
'''


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'management/register.html'
    success_url = reverse_lazy('login')


def logout(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@user_passes_test(is_admin)
def hompageview(request):
	if request.user.is_authenticated:
		return render(request, 'management/homepage.html')
"""
After log in home page is only accessible ny admin with more functionalities
like adding new book, updating existing book, deleting book
"""

@login_required(login_url='login')
def addbook_view(request):
    form=forms.BookForm()
    if request.method=='POST':
        form=forms.BookForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'management/bookadded.html')
    return render(request,'management/addbook.html',{'form':form})
"""
This view will add books which admin creates
"""

@login_required(login_url='login')
def listbookview(request):
"""
listing all the books added by admin
"""	
	book = Book.objects.all().count()

	context = {'book':book}

	return render(request, 'management/viewbook.html', context)


class EditBook(LoginRequiredMixin, UpdateView):
	model = Book
	form_class = BookForm
	template_name = 'management/editbook.html'
	success_url = reverse_lazy('homepage')
	success_message = "Book Updated Successfully"


class DeleteBook(LoginRequiredMixin, DeleteView):
	model = Book
	form_class = BookForm
	template_name = 'management/deletebook.html'
	success_url = reverse_lazy('hompage')
	success_message = 'Book Deleted'













