from django.urls import path

from . import views

app_name = 'polls'
# urlpatterns coordinate coordinate views with paths requests
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/delete/', views.DeleteQuestionView.as_view(), name='delete'),
    path('newQuestion/', views.NewQuestionView.as_view(), name='newQuestion'),
    path('addNewQuestion/', views.add_new_question, name='addNewQuestion'),
]
