from django.contrib import admin
from .models import UnitUniversityForm, QuestionSets, Mcqpart, QuestionMcq, Writtenpart, QuestionWritten

@admin.register(UnitUniversityForm)
class UnitUniversityFormAdmin(admin.ModelAdmin):
    list_display = ('unit', 'university')
    # Add any other configurations as needed

@admin.register(QuestionSets)
class QuestionSetsAdmin(admin.ModelAdmin):
    list_display = ('unit_university_form', 'question_year', 'timer')
    # Add any other configurations as needed

@admin.register(Mcqpart)
class McqpartAdmin(admin.ModelAdmin):
    list_display = ('subject', 'question_set')
    # Add any other configurations as needed

@admin.register(QuestionMcq)
class QuestionMcqAdmin(admin.ModelAdmin):
    list_display = ('Mcq_part', 'question_text', 'option1', 'option2', 'option3', 'option4', 'correct_answer', 'solution_type')
    # Add any other configurations as needed

@admin.register(Writtenpart)
class WrittenpartAdmin(admin.ModelAdmin):
    list_display = ('subject', 'question_set')
    # Add any other configurations as needed

@admin.register(QuestionWritten)
class QuestionWrittenAdmin(admin.ModelAdmin):
    list_display = ('Written_part', 'question_text', 'solution_type')
    # Add any other configurations as needed
