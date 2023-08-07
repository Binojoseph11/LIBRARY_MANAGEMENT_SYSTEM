from django.urls import path
from book import views
urlpatterns = [

    path("list/",views.ListbookAPIView.as_view(),name="library_list"),
    path("create/", views.CreatebookAPIView.as_view(),name="library_create"),
    path("update/<int:pk>/",views.UpdatebookAPIView.as_view(),name="update_library"),
    path("delete/<int:pk>/",views.DeletebookAPIView.as_view(),name="delete_library"),
    path('questions/', views.QuestionsAPIView.as_view())
]