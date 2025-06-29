# views.py
from django.shortcuts import render, redirect
from .models import JuiceItem, Feedback
from .forms import FeedbackForm, NewsletterForm, RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    juices = JuiceItem.objects.all()
    best_sellers = JuiceItem.objects.filter(is_best_seller=True)
    feedback_form = FeedbackForm()
    newsletter_form = NewsletterForm()

    context = {
        'juices': juices,
        'best_sellers': best_sellers,
        'feedback_form': feedback_form,
        'newsletter_form': newsletter_form
    }
    return render(request, 'home/homepage.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # or your login page
    else:
        form = RegisterForm()
    return render(request, 'home/register.html', {'form': form})

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Or wherever you want
    return redirect('home')

def subscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('home')

def add_to_cart(request, item_id):
    # Logic for adding item to cart (session or DB)
    print("Adding item to cart:", item_id)
    return redirect('home')  # Redirect after adding to cart