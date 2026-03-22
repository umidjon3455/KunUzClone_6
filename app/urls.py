from django.contrib import admin
from django.urls import path, include
from . import views
from .views import HomePageView, news_list, news_detail, UzbPageView, WorldNewsView, SportNewsView, SubjectNewsView, ContactView

# from .views import news_list, news_detail, home_page, uzb_page, jahon_page, sport_page,fan_page,contact_page

# urlpatterns = [
#     path('', home_page.as_view(), name='home'),
#     path('maktab', sport_page.as_view(), name='maktab'),
#     path('jahon', jahon_page.as_view(), name='jahon'),
#     path('sport', sport_page.as_view(), name='sport'),
#     path('uzbekiston', uzb_page.as_view(), name='uzb'),
#     path('Fan-texnika', fan_page.as_view(), name='fan'),
#     path('contact', contact_page, name='contact'),
#     path("news/<slug:slug>/", news_detail, name='news_detail_page'),
#     path("contact/", views.contact, name="contact"),
# ]

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('news/', news_list, name='news_list'),
    path('news/<slug:slug>/', news_detail, name='news_detail_page'),
    path('uzb/', UzbPageView.as_view(), name='uzb'),
    path('jahon/', WorldNewsView.as_view(), name='jahon'),
    path('sport/', SportNewsView.as_view(), name='maktab'),
    path('fan/', SubjectNewsView.as_view(), name='fan'),
    path('contact/', ContactView.as_view(), name='contact'),
]