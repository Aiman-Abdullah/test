from django.shortcuts import render
from my_django_app.models import Person
from my_django_app.resources import PersonResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

def index(request):
    return render(request, 'hello/index.html')


def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	value = Person(
        		data[0],
        		data[1],
        		 data[2],
        		 data[3]
        		)
        	value.save()       
        
        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'input.html')
