from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm


def contact_list(request):
    q = request.GET.get('q')
    if q:
        contacts = Contact.objects.filter(name__icontains=q)
    else:
        contacts = Contact.objects.all().order_by('name')
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user 
            contact.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})


def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form})


def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})

