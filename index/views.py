from django.shortcuts import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from serializers import UserSerializer
from serializers import GroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
#  import pdb


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# auth is available function
@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def DjangoUsers(request, id=None):
    """docstring for DjangoUsers"""
    data = request.POST
    print data
    if request.method == 'POST':
        user_obj = UserSerializer(data=data)
        if user_obj.is_valid():
            print "ok"
            user_obj.save()
            return HttpResponse("good")
        else:
            print "bad"
            return HttpResponse(user_obj.errors)
    elif request.method == 'PUT':
        #  pdb.set_trace()
        user_object = User.objects.get(id=id)
        user_obj = UserSerializer(user_object, data=data)
        if user_obj.is_valid():
            print "ok"
            user_obj.save()
            return HttpResponse("good")
        else:
            return Response(user_obj.errors, status=404)
