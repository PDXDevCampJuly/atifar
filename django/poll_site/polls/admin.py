from django.contrib import admin

from .models import Question
from .models import Choice

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
