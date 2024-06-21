from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NearByStores
from .serializers import NBSSerializer
from crudTempl import readWget, createWpost, deleteWdelete, updateWpatch

class NearByStoreView(APIView):

    def get(self, request):
        res, status = readWget(NearByStores, {}, NBSSerializer,
                               "List of Near by stores")
        return Response(res, status=status)

    def post(self, request):
        res, status = createWpost(
            request.data, NBSSerializer, "Store created successfully")
        return Response(res, status=status)

    def patch(self, request, pk):
        res, status = updateWpatch(
            NearByStores, pk, NBSSerializer, request.data, "Store updated successfully", ["name","phone_number","address","latitude","longitude","days","openAt","closeAt"])
        return Response(res, status=status)

    def delete(self, request, pk):
        res, status = deleteWdelete(
            NearByStores, pk, "Store deleted successfully")
        return Response(res, status=status)
