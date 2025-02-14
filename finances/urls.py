from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_balance_sheet, name='create_balance_sheet'),
    path('view/<int:balance_sheet_id>/', views.view_balance_sheet, name='view_balance_sheet'),
    path('edit/<int:balance_sheet_id>/', views.edit_balance_sheet, name='edit_balance_sheet'),
    path('delete/<int:balance_sheet_id>/', views.delete_balance_sheet, name='delete_balance_sheet'),
    path('previous/', views.previous_balance_sheets, name='previous_balance_sheets'),  # New URL
    path('add/<int:balance_sheet_id>/', views.add_entry, name='add_entry'),
    path('edit-entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete-entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]