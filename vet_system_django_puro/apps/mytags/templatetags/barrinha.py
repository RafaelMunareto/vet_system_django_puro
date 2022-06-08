from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(needs_autoescape=True)
def barrinha(dado, autoescape=True):
    if dado  == '':
        dado = 0.00

    barrinha = f"<span class='size90 cor'>{dado}</span>\
                <div class='flex-column align-itens'>\
                    <div class='progress barra d-flex margin-0'>\
                        <div class='cor_back transparente' style='width:{dado}%'>{dado}</div>\
                    </div>\
                </div>"

    return mark_safe(barrinha)


@register.filter(needs_autoescape=True)
def barrinha_sem_nota(dado, autoescape=True):
    if dado  == '':
        dado = 0.00

    barrinha = f"<div class='flex-column align-itens' title='{dado}'>\
                    <div class='progress barra d-flex margin-0'>\
                        <div class='cor_back transparente' style='width:{dado}%'>{dado}</div>\
                    </div>\
                </div>"

    return mark_safe(barrinha)