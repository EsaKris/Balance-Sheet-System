from django.contrib import admin # type: ignore
from .models import BalanceSheet, Entry

@admin.register(BalanceSheet)
class BalanceSheetAdmin(admin.ModelAdmin):
    list_display = ('month', 'year')  # Fields to display in the list view
    search_fields = ('month', 'year')  # Fields to search by

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'is_income', 'date_time', 'balance_sheet')
    list_filter = ('is_income', 'balance_sheet')  # Filters for the list view
    search_fields = ('description', 'amount')  # Fields to search by