from django.shortcuts import render
from django.views.generic import DetailView

from blog.models import Article
from email_sender.models import Mailing, Client


# Create your views here.
def main_page(request):
    mailing_count = Mailing.objects.count()
    client_count = Client.objects.count()
    mailing_active_count = Mailing.objects.filter(status='start').count()
    article_rand = Article.objects.order_by('?')[:3]
    context = {'mailing_count': mailing_count,
               'client_count': client_count,
               'mailing_active_count': mailing_active_count,
               'article_rand_list': article_rand
               }
    return render(request, 'blog/main_page.html', context)

class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


