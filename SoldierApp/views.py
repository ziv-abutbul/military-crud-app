from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from SoldierApp.serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from SoldierApp.models import Soldier
@csrf_exempt
def soldiersApi(request,id=0):
    if request.method=='GET':
        soldier = Soldier.objects.all()
        soldier_serializer=StudentSerializer(soldier,many=True)
        return JsonResponse(soldier_serializer.data,safe=False)
    elif request.method=='POST':
        soldier_data=JSONParser().parse(request)
        soldier_serializer=StudentSerializer(data=soldier_data)
        if soldier_serializer.is_valid():
            soldier_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        soldier_data=JSONParser().parse(request)
        soldier=Soldier.objects.get(id=id)
        soldier_serializer=StudentSerializer(soldier,data=soldier_data)
        if soldier_serializer.is_valid():
            soldier_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        soldier=Soldier.objects.get(id=id)
        soldier.delete()
        return JsonResponse("Deleted Successfully",safe=False)