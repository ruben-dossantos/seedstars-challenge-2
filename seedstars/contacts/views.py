from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseRedirect
from django.core.validators import validate_email
from .models import Contact
from .forms import ContactForm

def index(request):
	return render(request, 'contacts/index.html', {})

def list(request):
	contacts = Contact.objects.order_by('id')
	context = { 'contacts': contacts }
	return render(request, 'contacts/list.html', context)

@requires_csrf_token
def add(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = request.POST['name']
			email = request.POST['email']
			if validate_email(email) and name.length <= 100:
				new_contact = Contact(name=name, email=email)
				new_contact.save()
			
			return HttpResponseRedirect('/')
			 

	else:
		form = ContactForm()
	
	return render(request, 'contacts/add.html', {'form': form})

