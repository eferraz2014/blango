from django import template
from blog.models import Post
from django.contrib.auth import get_user_model

user_model=get_user_model()

register=template.Library()

@register.filter
def author_details(author):
  if not isinstance (author, user_model):
    return ""
  if author.first_name and author.last_name:
    return f"{{author.first_name}}{{author.last_name}}"
  else:
    return f"{author.username}"

