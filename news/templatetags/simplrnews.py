import re
from django import template
from news.models import NewsArticle


register = template.Library()

class NewsList(template.Node):
	"""
	Tag node, which implements render method.
	"""
	def __init__(self, limit, var_name):
		self.limit = int(limit)
		self.var_name = var_name
	
	def render(self, context):
		articles = NewsArticle.objects.filter(published=True)[:self.limit]
		if articles and self.limit == 1:
			context[self.var_name] = articles[0]
		else:
			context[self.var_name] = articles
		return ''


@register.tag
def get_news_list(parser, token):
	"""
	Parser to tag.
	"""
	try:
		tag_name, arg = token.contents.split(None, 1)
	except ValueError:
		raise template.TemplateSyntaxError("%r tag requires a single argument." % token.contents.split()[0])

	valid_format = re.search(r'(.*?) as (\w+)', arg)
	if not valid_format:
		raise template.TemplateSyntaxError("%r invalid tag arguments" % tag_name)
	format_string, var = valid_format.groups()

	return NewsList(format_string, var)

