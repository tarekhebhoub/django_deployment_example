from django.urls import path
from django.conf.urls import url, include
from basic_app import views

app_name='basic_app'

urlpatterns=[
	path('school_list/',views.SchoolListView.as_view(),name='list'),
	path('detail/<int:pk>',views.SchoolDetailView.as_view(),name='detail'),
	path('create/',views.SchoolCreateView.as_view(),name='create'),
	path('update/<int:pk>',views.SchoolUpdateView.as_view(),name='update'),
	path('createst/',views.StudentCreateView.as_view(),name='createst'),
	path('delete/<int:pk>',views.SchoolDeleteView.as_view(),name='delete')
]