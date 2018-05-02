from django.shortcuts import render
from .forms import ColorfulContactForm, ContactForm

def home(request):
    if request.method == 'POST':
        form = ColorfulContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ColorfulContactForm()
    return render(request, 'home.html', {'form': form})