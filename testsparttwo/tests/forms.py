from django import forms
from .models import Answer, UserData


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'language',
                  'grade', 'parent_first_name', 'parent_last_name', 'parent_phone_number', 'city']


class TestForm(forms.Form):
    def __init__(self, test, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.test = test
        questions = test.questions.all()
        for question in questions:
            choices = [(answer.id, answer.text) for answer in question.answers.all()]
            self.fields[f'question_{question.id}'] = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)

    def calculate_score(self):
        score = 0
        for question in self.test.questions.all():
            field_name = f'question_{question.id}'
            answer_id = self.cleaned_data[field_name]
            answer = Answer.objects.get(id=answer_id)
            if answer.is_correct:
                score += 1
        return score
