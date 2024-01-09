from django.db import models

class SubjectChapterForm(models.Model):
    group = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)
    board_question = models.CharField(max_length=100)
    

    TOPICS_CHOICES = [
        ('None', 'None'),
        ('Yes', 'Yes'),
    ]
    topics = models.CharField(max_length=4, choices=TOPICS_CHOICES, default='None')
    
    def __str__(self):
        return f"{self.group} - {self.subject} - {self.chapter}"


class Topic(models.Model):
    subject_chapter_form = models.ForeignKey(SubjectChapterForm, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # Add a title field for topics
    
    def __str__(self):
        return self.title

class QuestionSet(models.Model):
    form = models.ForeignKey(SubjectChapterForm, on_delete=models.CASCADE, related_name='questionsets')
    title = models.CharField(max_length=200)
    header = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    question_set = models.ForeignKey(QuestionSet, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.IntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')])
    solution_type = models.CharField(max_length=10, choices=[('photo', 'Photo'), ('text', 'Text')])  # Corrected line
    photo_solution = models.ImageField(upload_to='solutions/', blank=True, null=True)
    text_solution = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question_text
