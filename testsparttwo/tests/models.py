from django.db import models


class UserData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    language = models.CharField(max_length=2, choices=(('RU', 'Russian'), ('KZ', 'Kazakh')))

    # New fields
    GRADE_CHOICES = [(i, str(i)) for i in range(1, 13)]  # Generates pairs of grade numbers for choices
    grade = models.IntegerField(choices=GRADE_CHOICES, null=True, blank=True, default=None)
    parent_first_name = models.CharField(max_length=100, default='', blank=True)
    parent_last_name = models.CharField(max_length=100, default='', blank=True)
    parent_phone_number = models.CharField(max_length=100, default='', blank=True)

    CITY_CHOICES = [
        ('Almaty', 'Алматы'),
        ('Astana', 'Астана'),
        ('Shymkent', 'Шымкент'),

    ]
    city = models.CharField(max_length=50, choices=CITY_CHOICES, blank=True, null=True)

    class Meta:
        verbose_name = 'Данные клиента'
        verbose_name_plural = 'Данные клиентов'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Test(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class TestResult(models.Model):
    user_data = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name='test_results')
    test_name = models.CharField(max_length=100)
    result = models.TextField()  # You can adjust the fields based on the type of result you need to store
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Результат теста'
        verbose_name_plural = 'Результаты тестов'

    def __str__(self):
        return f"{self.test_name} result for {self.user_data}"
