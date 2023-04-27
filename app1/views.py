from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import DataConverter
from rest_framework.response import Response

# Create your views here.

# class based views
# Now we will perform CRUD(Create, Read, Update, Delete) operation
# Read
class GetUserData(APIView):
    def get(self,request):
        all_python_objs = User.objects.all()
        d1 = DataConverter(all_python_objs, many=True)
        # now all the data is converted in JSON format and now we are sending it as response
        return Response(d1.data)

# Create
class CreateUserData(APIView):
    def post(self, request):
        # data browser me se aa raha hai, aur wo JSON me aa raha hai. Hame use db me store karne ke liye python language me convert karna padega
        d1 = DataConverter(data = request.data)   # it convert JSON into Python
        if d1.is_valid():
            d1.save() # aa method call karvathi j db ma row create thase
            all_python_objs = User.objects.all()
            # now data in db are in python we are converting it into JSON
            d1 = DataConverter(all_python_objs, many=True)
            return Response(d1.data)
        else:
            return Response(d1.errors)
        

# Update
class EditUserData(APIView):
    def put(self,request,pk):
        single_python_obj = User.objects.get(id = pk)
        d1 = DataConverter(single_python_obj, data = request.data)
        if d1.is_valid():
            d1.save()
            all_python_objs = User.objects.all()
            d1 = DataConverter(all_python_objs,many=True)
            return Response(d1.data)
        else:
            return Response(d1.errors)
        

# Delete
class DeleteUserData(APIView):
    def delete(self, request, pk):
        single_python_obj = User.objects.get(id = pk)
        single_python_obj.delete()
        all_python_objs = User.objects.all()
        d1 = DataConverter(all_python_objs, many=True)
        return Response(d1.data)
            