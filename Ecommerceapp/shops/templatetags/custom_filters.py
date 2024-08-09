
from django import template

register = template.Library()

@register.filter
def first_two_sentences(value):
    sentences = value.split('. ')
    return '. '.join(sentences[:1]) + ('.' if len(sentences) > 1 else '')
#test 1 cümle ye düşür