from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import Category, News
from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.

def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list': news_list
    }

    return render(request, "news/news_list.html", context=context)

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, status=News.Status.Published)

    news_list = News.published.exclude(id=news.id)[:4]
    
    context = {
        'news': news,
        'news_list': news_list
    }
    return render(request, "news/news_detail.html", context)


# def home_page(request):
#     news_list = News.objects.filter(status=News.Status.Published)
#
#     minix_news = News.published.order_by('-publish_time')[:3]
#     uzb_news = News.published.filter(category__name="Uzbekiston").order_by('-publish_time')[:4]
#     jahon_news = News.published.filter(category__name="Jahon").order_by('-publish_time')[:4]
#     sport_news = News.published.filter(category__name="Sport").order_by('-publish_time')[:2]
#
#
#     fan_news = News.published.filter(
#         category__name="Fan-texnika"
#     ).order_by('-publish_time')
#
#     fan_news1 = fan_news[0] if fan_news.count() > 0 else None
#     fan_news2 = fan_news[1] if fan_news.count() > 1 else None
#     fan_news3 = fan_news[2] if fan_news.count() > 2 else None
#     fan_news4 = fan_news[3] if fan_news.count() > 3 else None
#
#     context = {
#         'news_list': news_list,
#         'minix_news': minix_news,
#         'uzb_news': uzb_news,
#         'jahon_news': jahon_news,
#         'fan_news1': fan_news1,
#         'fan_news2': fan_news2,
#         'fan_news3': fan_news3,
#         'fan_news4': fan_news4,
#     }
#
#     return render(request, "news/index.html", context)

class HomePageView(TemplateView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['categories'] = Category.objects.all()
        contex['minix_news'] = News.published.all().order_by('-publish_time')[:4]
        contex['uzb_news'] = News.published.all().filter(category__name="Uzbekiston").order_by('-publish_time')
        contex['jahon_news'] = News.published.all().filter(category__name="Jahon")[:4]
        contex['sport_news'] = News.published.all().filter(category__name="Sport").order_by("-publish_time")
        contex['fan_news'] = News.published.all().filter(category__name="Fan-texnika").order_by("-publish_time")

        return contex

# def uzb_page(request):
#     news_list = News.objects.filter(status=News.Status.Published)
#     uzbek_news = News.objects.filter(category__name="Uzbekiston")
#     uzb_news_1 = News.published.filter(category__name="Uzbekiston").order_by('-publish_time')[0]
#     uzb_news_2 = News.published.filter(category__name="Uzbekiston").order_by('-publish_time')[1]
#     uzb_news_3 = News.published.filter(category__name="Uzbekiston").order_by('-publish_time')[2]
#     uzb_news_4 = News.published.filter(category__name="Uzbekiston").order_by('-publish_time')[3]
#
#     context = {
#         'news_list': news_list,
#         'uzb_news_1': uzb_news_1,
#         'uzb_news_2': uzb_news_2,
#         'uzb_news_3': uzb_news_3,
#         'uzb_news_4': uzb_news_4,
#         'uzbek_news': uzbek_news,
#     }
#
#     return render(request, "news/uzb.html", context=context)

class UzbPageView(ListView):
    model = News
    template_name = "news/uzb.html"
    context_object_name = "news_list"
    def get_queryset(self):
        return News.objects.filter(status=News.Status.Published)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uzbek_news = News.objects.filter(category__name="Uzbekiston").order_by('-publish_time')
        context['uzbek_news'] = uzbek_news
        context['uzb_news_1'] = uzbek_news[0] if len(uzbek_news) > 0 else None
        context['uzb_news_2'] = uzbek_news[1] if len(uzbek_news) > 1 else None
        context['uzb_news_3'] = uzbek_news[2] if len(uzbek_news) > 2 else None
        context['uzb_news_4'] = uzbek_news[3] if len(uzbek_news) > 3 else None

        return context

# def jahon_page(request):
#     jahon_news_list = News.objects.filter(status=News.Status.Published)
#     jahon_news = News.objects.filter(category__name="Jahon")
#     jahon_news_1 = News.published.filter(category__name="Jahon").order_by('-publish_time')[0]
#     jahon_news_2 = News.published.filter(category__name="Jahon").order_by('-publish_time')[1]
#     jahon_news_3 = News.published.filter(category__name="Jahon").order_by('-publish_time')[2]
#     jahon_news_4 = News.published.filter(category__name="Jahon").order_by('-publish_time')[3]
#
#
#     context = {
#         'jahon_news_1': jahon_news_1,
#         'jahon_news_2': jahon_news_2,
#         'jahon_news_3': jahon_news_3,
#         'jahon_news_4': jahon_news_4,
#         'jahon_news_list': jahon_news_list,
#         'jahon_news': jahon_news,
#     }
#
#     return render(request, "news/single.html", context=context)

class WorldNewsView(ListView):
    model = News
    template_name = "news/single.html"
    context_object_name = "jahon_news_list"

    def get_queryset(self):
        return News.objects.filter(status=News.Status.Published)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jahon_news = News.objects.filter(category__name="Jahon").order_by('-publish_time')
        context['jahon_news'] = jahon_news
        context['jahon_news_1'] = jahon_news[0] if len(jahon_news) > 0 else None
        context['jahon_news_2'] = jahon_news[1] if len(jahon_news) > 1 else None
        context['jahon_news_3'] = jahon_news[2] if len(jahon_news) > 2 else None
        context['jahon_news_4'] = jahon_news[3] if len(jahon_news) > 3 else None

        return context

# def sport_page(request):
#     sport_news_list = News.objects.filter(status=News.Status.Published)
#     sport_news = News.objects.filter(category__name="Sport")
#     sport_news_1 = News.published.filter(category__name="Sport").order_by('-publish_time')[0]
#     sport_news_2 = News.published.filter(category__name="Sport").order_by('-publish_time')[1]
#     sport_news_3 = News.published.filter(category__name="Sport").order_by('-publish_time')[2]
#     sport_news_4 = News.published.filter(category__name="Sport").order_by('-publish_time')[3]
#
#
#
#     context = {
#         'sport_news_1': sport_news_1,
#         'sport_news_2': sport_news_2,
#         'sport_news_3': sport_news_3,
#         'sport_news_4': sport_news_4,
#         'sport_news_list': sport_news_list,
#         'sport_news': sport_news,
#     }
#
#     return render(request, "news/sport.html", context=context)

class SportNewsView(ListView):
    model = News
    template_name = "news/sport.html"
    context_object_name = "sport_news_list"

    def get_queryset(self):
        return News.objects.filter(status=News.Status.Published)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sport_news = News.objects.filter(category__name="Sport").order_by('-publish_time')
        context['sport_news'] = sport_news
        context['sport_news_1'] = sport_news[0] if len(sport_news) > 0 else None
        context['sport_news_2'] = sport_news[1] if len(sport_news) > 1 else None
        context['sport_news_3'] = sport_news[2] if len(sport_news) > 2 else None
        context['sport_news_4'] = sport_news[3] if len(sport_news) > 3 else None

        return context

# def fan_page(request):
#     fan_news_list = News.objects.filter(status=News.Status.Published)
#     fan_news = News.objects.filter(category__name="Fan-texnika")
#     fan_news_1 = News.published.filter(category__name="Fan-texnika").order_by('-publish_time')[0]
#     fan_news_2 = News.published.filter(category__name="Fan-texnika").order_by('-publish_time')[1]
#     fan_news_3 = News.published.filter(category__name="Fan-texnika").order_by('-publish_time')[2]
#     fan_news_4 = News.published.filter(category__name="Fan-texnika").order_by('-publish_time')[3]
#
#
#
#     context = {
#         'fan_news_1': fan_news_1,
#         'fan_news_2': fan_news_2,
#         'fan_news_3': fan_news_3,
#         'fan_news_4': fan_news_4,
#         'fan_news_list': fan_news_list,
#         'fan_news': fan_news,
#     }
#
#     return render(request, "news/fan.html", context=context)

class SubjectNewsView(ListView):
    model = News
    template_name = "news/fan.html"
    context_object_name = "fan_news_list"

    def get_queryset(self):
        return News.objects.filter(status=News.Status.Published)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fan_news = News.objects.filter(category__name="Fan-texnika").order_by('-publish_time')
        context['fan_news'] = fan_news
        context['fan_news_1'] = fan_news[0] if len(fan_news) > 0 else None
        context['fan_news_2'] = fan_news[1] if len(fan_news) > 1 else None
        context['fan_news_3'] = fan_news[2] if len(fan_news) > 2 else None
        context['fan_news_4'] = fan_news[3] if len(fan_news) > 3 else None

        return context


# def contact_page(request):
#     news_list = News.objects.filter(status=News.Status.Published)
#
#     context = {
#         'news_list': news_list
#     }
#
#     return render(request, "news/contact.html", context=context)
#
#
#
# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         subject = request.POST.get("subject")
#         message = request.POST.get("message")
#
#         Contact.objects.create(
#             name=name,
#             email=email,
#             subject=subject,
#             message=message
#         )
#
#         return redirect("home")
#
#     return render(request, "news/contact.html")

class ContactView(View):
    template_name = "news/contact.html"

    def get(self, request):
        news_list = News.objects.filter(status=News.Status.Published)
        context = {
            'news_list': news_list
        }
        return render(request, self.template_name, context)

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect("home")

