from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.

def home(request):
    url = "http://182.18.144.140:14000/status?password="
    response = requests.get(url)
    if response.status_code == 200:
        status_data =response.text
      # Split the data into lines for rendering in the template
        status_lines = status_data.split('\n')
        conditions="queued 0 msgs"
        select_line=[line for line in status_lines if conditions not in line]
    else:
        status_lines = ["Error: Unable to fetch data from the server."]
    return render(request, 'home.html', {'select_line':select_line})


def kannel(request):
    url = "http://103.119.220.71:1503/status?password="
    response = requests.get(url)
    if response.status_code == 200:
        status_data =response.text
        # Split the data into lines for rendering in the template
        status_lines = status_data.split('\n')
        conditions="queued 0 msgs"
        select_line=[line for line in status_lines if conditions not in line]
        
    else:
        status_lines = ["Error: Unable to fetch data from the server."]
    return render(request, 'home.html', {'select_line':select_line})
