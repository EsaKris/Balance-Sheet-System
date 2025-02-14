from django.shortcuts import render, redirect, get_object_or_404
from .models import BalanceSheet, Entry
from .forms import EntryForm

def home(request):
    balance_sheets = BalanceSheet.objects.all()
    recent_entries = Entry.objects.order_by('-date_time')[:5]
    return render(request, 'finances/home.html', {
        'balance_sheets': balance_sheets,
        'recent_entries': recent_entries
    })

def create_balance_sheet(request):
    if request.method == 'POST':
        month = request.POST.get('month')
        year = request.POST.get('year')
        balance_sheet = BalanceSheet.objects.create(month=month, year=year)
        return redirect('view_balance_sheet', balance_sheet.id)
    return render(request, 'finances/create_balance_sheet.html')

def view_balance_sheet(request, balance_sheet_id):
    balance_sheet = get_object_or_404(BalanceSheet, id=balance_sheet_id)
    entries = Entry.objects.filter(balance_sheet=balance_sheet)
    total_income = sum(entry.amount for entry in entries if entry.is_income)
    total_expenditure = sum(entry.amount for entry in entries if not entry.is_income)
    balance = total_income - total_expenditure
    return render(request, 'finances/view_balance_sheet.html', {
        'balance_sheet': balance_sheet,
        'entries': entries,
        'total_income': total_income,
        'total_expenditure': total_expenditure,
        'balance': balance
    })

def add_entry(request, balance_sheet_id):
    balance_sheet = get_object_or_404(BalanceSheet, id=balance_sheet_id)
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.balance_sheet = balance_sheet
            entry.save()
            return redirect('view_balance_sheet', balance_sheet_id)
    else:
        form = EntryForm()
    return render(request, 'finances/add_entry.html', {'form': form})

def edit_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('view_balance_sheet', entry.balance_sheet.id)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'finances/edit_entry.html', {'form': form})

def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    balance_sheet_id = entry.balance_sheet.id
    entry.delete()
    return redirect('view_balance_sheet', balance_sheet_id)

def edit_balance_sheet(request, balance_sheet_id):
    balance_sheet = get_object_or_404(BalanceSheet, id=balance_sheet_id)
    if request.method == 'POST':
        balance_sheet.month = request.POST.get('month')
        balance_sheet.year = request.POST.get('year')
        balance_sheet.save()
        return redirect('view_balance_sheet', balance_sheet.id)
    return render(request, 'finances/edit_balance_sheet.html', {
        'balance_sheet': balance_sheet
    })

def delete_balance_sheet(request, balance_sheet_id):
    balance_sheet = get_object_or_404(BalanceSheet, id=balance_sheet_id)
    balance_sheet.delete()
    return redirect('home')

def previous_balance_sheets(request):
    balance_sheets = BalanceSheet.objects.all()  # Fetch all balance sheets
    return render(request, 'finances/previous_balance_sheets.html', {
        'balance_sheets': balance_sheets
    })