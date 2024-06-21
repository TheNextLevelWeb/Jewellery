from crudTempl import readWget, createWpost
from .serializers import SupporSerialzer
from .models import Support
from rest_framework.views import APIView
from rest_framework.response import Response

class SupportView(APIView):

    def get(self,request):
        res, status = readWget(Support,{},SupporSerialzer,"List of support reqeusts")
        return Response(res, status=status)
    
    def post(self,request):
        res, status = createWpost(request.data,SupporSerialzer,"We will conatct you soon")
        return Response(res, status=status)
    