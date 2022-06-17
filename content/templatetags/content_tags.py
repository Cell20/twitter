from django.template.defaulttags import register
import calendar

@register.filter
def get_month(n):
    return calendar.month_name[n]

@register.filter
def latest(tweets):
    return tweets.order_by('-created_at')
