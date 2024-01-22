from django.contrib import admin

# Register your models here.
from .models import Categoria, Flashcard, FlashcardDesafio, Desafio

admin.site.register(Categoria)
admin.site.register(Flashcard)
admin.site.register(FlashcardDesafio)
admin.site.register(Desafio)