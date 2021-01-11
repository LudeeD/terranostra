from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.files import File
from django.contrib.auth.decorators import login_required

from events.models import Report, ImageUploads, Votes, Profile
from events.forms import CreateReport

from datetime import datetime
import geohash 
from PIL import Image
from io import BytesIO, StringIO
import string
import random
import requests
# Create your views here.

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@login_required
def create_report(request):
    if request.method == 'POST':

        form = CreateReport(request.POST)

        if form.is_valid() == False:
            return redirect(reports)

        now = datetime.now()
        new_report = Report(
            creation_date=now, 
            title=form.cleaned_data['title'], 
            description=form.cleaned_data['description'],
            location_lat=form.cleaned_data['lat'],
            location_lng=form.cleaned_data['lng'],
            location_geohash=geohash.encode(form.cleaned_data['lat'], form.cleaned_data['lng'], precision=12),
            value=0)

        try:
            blob = BytesIO()
            im = Image.open(request.FILES['uploadfile'])
            im.thumbnail((250,250))
            im.save(blob, 'JPEG')
            image_id = id_generator()
            #print(image_id)
            data = blob.getvalue()
            #print(data)
            image_upload = ImageUploads(slug=image_id, data=data)
            image_upload.save()
            new_report.uploadimage =image_id 
        except Exception as e:
            # print(e)
            pass

        new_report.save()

        return redirect(reports)
    else:
        return render(request, "create_report.html")


def uploadedimage(request, slug):
    try:
        ob = ImageUploads.objects.get(slug=slug)
        img = Image.open(BytesIO(ob.data))
        response = HttpResponse(content_type='image/jpeg')
        img.save(response, 'JPEG')
        return response
    except Exception as e:
        # print(e)
        pass
    return HttpResponse(status=404)
    
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


def detail_report(request, id):
    report = Report.objects.get(id=id)
    return render(request, 'detail.html' , {'report': report})

@login_required
def endorse_report(request, id):
    report = Report.objects.get(id=id)
    report.value += 1
    report.save()
    return render(request, 'detail.html' , {'report': report})

@login_required
def reject_report(request, id):
    report = Report.objects.get(id=id)
    if report.value > 0:
        report.value -= 1
    report.save()
    return render(request, 'detail.html' , {'report': report})


@login_required
def profile(request):
    return render(request, 'account/profile.html')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def map_page(request):
    lat = request.GET.get('lat', None)
    lng = request.GET.get('lng', None)

    if lat == None or lng == None:
        return redirect(f"/map/?lat=41.1579&lng=-8.6291")


    location_geohash=geohash.encode(float(lat), float(lng), precision=4)
    reports = Report.objects.filter(location_geohash__startswith=location_geohash)

    result = []
    for report in reports:
        result.append({
            "id" : report.id,
            "lng" : report.location_lng,
            "lat" : report.location_lat,
            "title" : report.title,
            "type" : "Report",
            "votes" :  report.value
        })

    return render(request, 'map.html', {"lng": lng, "lat": lat, "reports": result})


def events(request):
    return render(request, 'todo.html')