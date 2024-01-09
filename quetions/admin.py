from django.contrib import admin
from .models import SubjectChapterForm, QuestionSet, Question, Topic

# Define a custom admin class for QuestionSet
class QuestionSetAdmin(admin.ModelAdmin):
    list_display = ('title', 'form_info', 'header', 'thumbnail')
    list_filter = ('form',)
    search_fields = ('title', 'form__group', 'form__subject', 'form__chapter', 'form__board_question')

    # Define a custom method to display SubjectChapterForm information
    def form_info(self, obj):
        subject_chapter_form = obj.form
        # Retrieve all related Topic objects for the SubjectChapterForm
        related_topics = Topic.objects.filter(subject_chapter_form=subject_chapter_form)
        # Create a list of topic titles
        topic_titles = [topic.title for topic in related_topics]
        # Join the topic titles into a comma-separated string
        topic_titles_str = ", ".join(topic_titles)

        return f"Group: {subject_chapter_form.group}, Subject: {subject_chapter_form.subject}, Chapter: {subject_chapter_form.chapter}, Topic Title(s): {topic_titles_str}"
    form_info.short_description = 'SubjectChapterForm Info'  # Set a custom column header

# Register the custom admin class for QuestionSet
admin.site.register(QuestionSet, QuestionSetAdmin)

# Register the other models and their respective admin classes as before
admin.site.register(SubjectChapterForm)
admin.site.register(Question)
admin.site.register(Topic)
