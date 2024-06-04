from django.shortcuts import render, get_object_or_404, redirect
from .models import Test, Answer, TestResult
from .forms import TestForm, UserDataForm


def collect_user_data_view(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            user_data = form.save()
            # Determine the submit text based on the user's language selection
            if user_data.language == 'KZ':
                request.session['submit_text'] = 'Жіберу'  # Kazakh
            else:
                request.session['submit_text'] = 'ПОЛУЧИТЬ РЕЗУЛЬТАТ'  # Default to Russian
            return redirect('home', user_data_id=user_data.id)

    else:
        form = UserDataForm()

    return render(request, 'tests/userform.html', {'form': form})


def test_list(request, user_data_id):
    tests = Test.objects.all()
    return render(request, 'tests/test_list.html', {'tests': tests, 'user_data_id': user_data_id})


def test_detail(request, test_id, user_data_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.prefetch_related('answers').all()

    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                selected_answer = Answer.objects.get(id=selected_answer_id)
                if selected_answer.is_correct:
                    score += 1

        TestResult.objects.create(
            user_data_id=user_data_id,
            test_name=test.title,
            result=f"Score: {score}",
        )
        return render(request, 'tests/test_result.html', {'test': test, 'user_data_id': user_data_id, 'score': score})

    submit_text = request.session.get('submit_text', 'Submit')
    return render(request, 'tests/test_detail.html',
                  {'test': test, 'questions': questions, 'user_data_id': user_data_id, 'submit_text': submit_text})


def test_result(request, test_id, user_data_id):
    test = get_object_or_404(Test, id=test_id)
    return render(request, 'tests/test_result.html', {'test': test, 'user_data_id': user_data_id})
