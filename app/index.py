from django import template
register = template.Library()

@register.filter
def getIndex(indexable, i):
    return indexable[i]