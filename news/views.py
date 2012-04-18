# Ricardo Soares (ricardo@dengun.com) - Dengun 2011


from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from news.models import NewsArticle


def article(request, id):
    article = get_object_or_404(NewsArticle, pk=id)
    return render_to_response('article.html', {'article': article}, context_instance=RequestContext(request))


def subscibe(request):
    """  """
