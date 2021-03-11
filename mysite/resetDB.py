from polls.models import Choice, Question

Choice.objects.all().delete()
Question.objects.all().delete()
from django.utils import timezone
q1 = Question(question_text="What is the weather?", pub_date=timezone.now())
q1.save()
q1.choice_set.create(choice_text='Sunny', votes=0)
q1.choice_set.create(choice_text='Rainy', votes=0)
q1.choice_set.create(choice_text='Snowing', votes=0)

q2 = Question(question_text="What is 5 + 3 equal to?", pub_date=timezone.now())
q2.save()
q2.choice_set.create(choice_text='8', votes=0)
q2.choice_set.create(choice_text='7', votes=0)
q2.choice_set.create(choice_text='4', votes=0)

q3 = Question(question_text="Is a car a type of vehicle?", pub_date=timezone.now())
q3.save()
q3.choice_set.create(choice_text='Yes', votes=0)
q3.choice_set.create(choice_text='No', votes=0)


