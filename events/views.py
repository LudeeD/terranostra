from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from events.models import Report
from events.forms import CreateReport

from datetime import datetime
import geohash 
# Create your views here.

def create_report(request):
    if request.method == 'POST':

        form = CreateReport(request.POST)

        if form.is_valid() == False:
            return redirect(reports)

        print(form.cleaned_data)

        now = datetime.now()
        new_report = Report(
            creation_date=now, 
            title=form.cleaned_data['title'], 
            description=form.cleaned_data['description'],
            location_lat=form.cleaned_data['lat'],
            location_lng=form.cleaned_data['lng'],
            location_geohash=geohash.encode(form.cleaned_data['lat'], form.cleaned_data['lng'], precision=12),
            value=0)

        new_report.save()

        print(form.cleaned_data['uploadfile'])

        return redirect(reports)
    else:
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