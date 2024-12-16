from django.shortcuts import render

def weekly_report(request):
    return render(request, "reports/weekly.html")

def monthly_report(request):
    return render(request, "reports/monthly.html")

def yearly_report(request):
    return render(request, "reports/yearly.html")
