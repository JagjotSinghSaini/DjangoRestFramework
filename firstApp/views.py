from django.shortcuts import render
from django.http import JsonResponse 
from firstApp.models import Employee
#JsonResponse is a serializer which will serialize our dictionary into Json when response goes back
# Create your views here.
def employeeView(request):
    emp={
        'id':123,
        'name':'john',
        'sal':1000000
    }

    data=Employee.objects.all();
    response={'employees':list(data.values('name','sal'))}

    return JsonResponse(response)
