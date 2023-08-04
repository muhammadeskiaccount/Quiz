from django.contrib import admin
from .models import Category, Question, Option, Result, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_correct', 'option')


class OptionInlineAdmin(admin.TabularInline):
    model = Option
    readonly_fields = ('id', )
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInlineAdmin]
    list_display = ('id', 'category', 'question')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'account',  'result', 'category', 'get_questions')

    def get_questions(self, obj):
        return ", ".join([question.question for question in obj.questions.all()])


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')
