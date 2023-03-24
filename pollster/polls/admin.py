from django.contrib import admin
from django.forms.models import BaseInlineFormSet

from .models import Question, Choice

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster admin area"


class ChoiceInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        kwargs['initial'] = [
            {'choice_text': 'JA'}, {'choice_text': 'NEJ'}
        ]
        super(ChoiceInlineFormSet, self).__init__(*args, **kwargs)


class ChoiceInline(admin.TabularInline):
    model = Choice
    max_num = 2
    formset = ChoiceInlineFormSet


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 (None, {'fields': ['image']}),]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Answer)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
