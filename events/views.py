from django.shortcuts import render
from django.core.paginator import Paginator

from events.models import Report
from events.forms import CreateReport
# Create your views here.

def create_report(request):
    if request.method == 'POST':
        form = CreateReport(request.POST)

        print("daaaaaaaaamn")
        print(form.is_valid())

        if form.is_valid():
            return render(request, "base.html")

            

    return render(request, "create_report.html")

    
def reports(request):
    order = request.GET.get('order', None)

    queryset = []
    if order == "date":
        queryset = Report.objects.order_by('-creation_date')
    else:
        queryset = Report.objects.order_by('-value')

    pages = Paginator(queryset, 2)
    page_number = request.GET.get('page', 1)
    print(page_number)
    page_obj = pages.get_page(page_number)

    return render(request, 'events.html', {'type': 'Reports','page_obj': page_obj})