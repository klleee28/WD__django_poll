from django.contrib import admin

# Register your models here.
from . models import Choice, Question

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

class ChoiceInLine2(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # Arrange fields shown in admin page
    field = ['pub_date', 'question_text']

class QuestionAdmin2(admin.ModelAdmin):
    # Create sets to separate the fields for better aesthetic
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields':['pub_date']}),
    ]
    inlines = [ChoiceInLine]

class QuestionAdmin3(admin.ModelAdmin):
    # Create a collapsed list to hide/unhide a field
    # Inlines also changes how data is displayed
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInLine2]

class QuestionAdmin4(admin.ModelAdmin):
    # Create a collapsed list to hide/unhide a field
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInLine2]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

class QuestionAdmin6(admin.ModelAdmin):
    # Create a filter list, and search field
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInLine2]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin6)

