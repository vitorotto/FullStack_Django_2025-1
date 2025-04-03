from django.contrib import admin

# Register your models here.

from .models import Questao
from .models import Alternativa


@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    list_display = ("texto_questao", "data_publicacao")


@admin.register(Alternativa)
class AlternativaAdmin(admin.ModelAdmin):
    list_display = ("questao", "texto_alternativa", "votos")
    list_filter = ("questao",)
