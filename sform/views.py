from django.shortcuts import render
from .forms import ColorfulContactForm, ContactForm

def home(request):
    if request.method == 'POST':
        # form = ColorfulContactForm(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        # form = ColorfulContactForm()
        form = ContactForm()
    return render(request, 'home.html', {'form': form})