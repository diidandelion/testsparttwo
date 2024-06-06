from django.contrib import admin
from .models import Test, Question, Answer, UserData, TestResult
from import_export.admin import ExportActionMixin
from nested_admin import NestedTabularInline, NestedModelAdmin


class AnswerInline(NestedTabularInline):
    model = Answer
    extra = 4  # Optional: Set the number of extra answer forms to display


class QuestionInline(NestedTabularInline):
    model = Question
    extra = 1  # Optional: Set the number of extra question forms to display
    inlines = [AnswerInline]


class TestAdmin(NestedModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Test, TestAdmin)


@admin.register(UserData)
class UserDataAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'city')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('city',)
    fieldsets = (
        ('Personal Information', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        ('Other Details',
         {'fields': ('language', 'grade', 'parent_first_name', 'parent_last_name', 'parent_phone_number')}),
    )


@admin.register(TestResult)
class TestResultAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('user_data', 'test_name', 'result', 'created_at')
    list_filter = ('test_name', 'created_at')
    search_fields = ('user_data__first_name', 'user_data__last_name', 'test_name')
