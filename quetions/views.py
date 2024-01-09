from django.shortcuts import render, redirect, get_object_or_404
from .models import SubjectChapterForm, QuestionSet, Question, Topic
from .forms import SelectSubjectChapterForm

def subject_chapter_form(request):
    if request.method == 'POST':
        group = request.POST.get('group')
        subject = request.POST.get('subject')
        chapter = request.POST.get('chapter')
        board_question = request.POST.get('board_question')
        topics_choice = request.POST.get('topics_choice')  

        existing_form, created = SubjectChapterForm.objects.get_or_create(
            group=group,
            subject=subject,
            chapter=chapter,
            board_question=board_question
        )

        # Check the choice for topics
        if topics_choice == 'Yes':
            # If "Yes" is selected, redirect to the page for adding topics
            return redirect('add_topics', form_id=existing_form.id)  # Ensure existing_form.id is valid
        else:
            # If "No" is selected, proceed to the question set creation page
            return redirect('question_set', form_id=existing_form.id)  # Ensure existing_form.id is valid

    return render(request, 'subject_chapter_form.html')

def add_topics(request, form_id):
    subject_chapter_form = get_object_or_404(SubjectChapterForm, pk=form_id)
    
    # Get the existing topics for the form
    existing_topics = Topic.objects.filter(subject_chapter_form=subject_chapter_form)

    if request.method == 'POST':
       
        topic_text = request.POST.get('topic_text')
        
   
        existing_topic = existing_topics.filter(title=topic_text).first()
        
        if existing_topic:
            topic = existing_topic
        else:
            topic = Topic(subject_chapter_form=subject_chapter_form, title=topic_text)
            topic.save()

       
        return redirect('question_set', form_id=subject_chapter_form.id)

    return render(request, 'add_topics.html', {'form_id': form_id, 'existing_topics': existing_topics})



def question_set(request, form_id):
    subject_chapter_form = get_object_or_404(SubjectChapterForm, pk=form_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        header = request.POST.get('header')
        thumbnail = request.FILES.get('thumbnail')

        question_set = QuestionSet(
            form=subject_chapter_form,
            title=title,
            header=header,
            thumbnail=thumbnail
        )
        question_set.save()

        return redirect('add_questions', question_set_id=question_set.id)

    return render(request, 'question_set.html')



# View for adding questions to a QuestionSet
def add_questions(request, question_set_id):
    question_set = get_object_or_404(QuestionSet, pk=question_set_id)

    if request.method == 'POST':
        question_texts = request.POST.getlist('question_text[]')
        option1 = request.POST.getlist('option1[]')
        option2 = request.POST.getlist('option2[]')
        option3 = request.POST.getlist('option3[]')
        option4 = request.POST.getlist('option4[]')
        correct_answers = request.POST.getlist('correct_answer[]')
        solution_types = request.POST.getlist('solution_type[]')
        photo_solutions = request.FILES.getlist('photo_solution[]')
        text_solutions = request.POST.getlist('text_solution[]')

        for i in range(len(question_texts)):
            question = Question(
                question_set=question_set,
                question_text=question_texts[i],
                option1=option1[i],
                option2=option2[i],
                option3=option3[i],
                option4=option4[i],
                correct_answer=correct_answers[i],
                solution_type=solution_types[i],
                photo_solution=photo_solutions[i] if solution_types[i] == 'photo' else None,
                text_solution=text_solutions[i] if solution_types[i] == 'text' else None,
            )
            question.save()

        return redirect('add_questions', question_set_id=question_set_id)

    return render(request, 'add_questions.html', {'question_set': question_set})


def select_group_subject_chapter(request):
    if request.method == 'POST':
        form = SelectSubjectChapterForm(request.POST)
        if form.is_valid():
            group = form.cleaned_data['group']
            subject = form.cleaned_data['subject']
            board_question = form.cleaned_data['board_question']
            chapter = form.cleaned_data['chapter']

            # Create a dictionary to hold filter parameters, including optional ones
            filter_params = {
                'group': group,
                'subject': subject,
            }

            if board_question:
                filter_params['board_question'] = board_question

            if chapter:
                filter_params['chapter'] = chapter

            # Filter subject chapter forms based on selected fields
            subject_chapter_forms = SubjectChapterForm.objects.filter(**filter_params)

            return render(request, 'subject_chapter_list.html', {'subject_chapter_forms': subject_chapter_forms})

    else:
        form = SelectSubjectChapterForm()

    return render(request, 'select_group_subject_chapter.html', {'form': form})

# View for listing question sets for a selected subject chapter form
def list_question_sets(request, form_id):
    subject_chapter_form = get_object_or_404(SubjectChapterForm, pk=form_id)
    question_sets = subject_chapter_form.questionsets.all()

    return render(request, 'question_set_list.html', {'subject_chapter_form': subject_chapter_form, 'question_sets': question_sets})

# View for listing questions for a selected question set
def list_questions(request, question_set_id):
    question_set = get_object_or_404(QuestionSet, pk=question_set_id)
    questions = question_set.questions.all()

    return render(request, 'question_list.html', {'question_set': question_set, 'questions': questions})