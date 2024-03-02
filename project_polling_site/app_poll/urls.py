from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='url_detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='url_results'),
    path('<int:question_id>/vote/', views.vote, name='url_vote'),
]