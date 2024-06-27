from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rating
from .serializers import RatingSerializer
from crudTempl import readWget, createWpost, deleteWdelete, updateWpatch

class RatingView(APIView):

    def get(self,request,product):
        res, status = readWget(Rating,{'product':product},RatingSerializer,f"List of {product}'s rating")
        return Response(res, status=status)
    
    def post(self,request,product):
        data = {'product': product, **request.data}
        res, status = createWpost(data, RatingSerializer, "Thanks for the efforts to write rating")
        return Response(res,status=status)

    def delete(self,request,pk):
        res, status = deleteWdelete(Rating,pk,"Rating has been deleted")
        return Response(res, status=status)
    
    def patch(self,request,pk):
        res, status = updateWpatch(
            Rating, pk, RatingSerializer, request.data, "Successfully updated", ['rating', 'review'])
        return Response(res, status=status)