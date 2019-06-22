from django.urls import path
from .views import (
	notes_list_view,
	notes_retieve_view,
	notes_update_view,
	notes_delete_view
	)
urlpatterns = [
    path('', notes_list_view),
    path('<str:slug>/', notes_retieve_view),
    path('<str:slug>/update', notes_update_view),
    path('<str:slug>/delete', notes_delete_view)
]