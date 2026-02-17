from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.hello_world_view, name="hello_world"),
    path("", views.hello_python_view, name="hello_python"),
    path("htmlrender", views.hello_html_view, name="hello_html"),
    path("helloname/<str:name>", views.hello_path, name="hello_path"),
    path("helloquery", views.hello_query, name="hello_query"),
    path("redirect", views.redirect_view, name="redirect"),
    path("post", views.post_view, name="post"),
    path("submit", views.submit_example_view, name="submit"),
    path("submit-django-form", views.submit_django_form, name="submit_django_form"),
    path("template", views.template_view, name="template"),
    path("todos", views.todos_view, name="todos"),
    path("person-details/<int:person_id>", views.person_details, name="person_details"),
    path("toggle-todo-done/<int:todo_id>", views.toggle_todo_done, name="toggle_todo_done"),    
    path("delete-todo/<int:todo_id>", views.person_details, name="person_details"),    

]
