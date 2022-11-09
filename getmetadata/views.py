from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os


@api_view(['GET'])
def getmeta(request):
    data = []
    for i in os.listdir():
        d = {}
        d["name"] = i
        d["type"] = 'folder' if os.path.isdir(os.path.abspath(i)) else 'file'
        d["time"] = round(os.path.getctime(i))
        print(d["name"], d["type"], d["time"])
        data.append(d)

    return Response(data)
