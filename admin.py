from django.contrib import admin

# Register your models here.
from .models import Category, JuiceItem, Feedback, NewsletterSubscriber

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(JuiceItem)
class JuiceItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_best_seller', 'badge')
    list_filter = ('category', 'is_best_seller')
    search_fields = ('name', 'description')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
