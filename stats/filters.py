from django import template


register = template.Library()

@register.filter(name='addclass')
def add_widget(value, class_hold, placeholder):
    return value.as_widget(attrs={'class': class_hold, 'placeholder': placeholder})