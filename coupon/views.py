from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Coupon
from .serializers import CouponSerializer
from crudTempl import readWget, createWpost, response_generator

class CouponCheckView(APIView):

    def post(self, request):
        code = request.data.get('code')
        if not code:
            return Response(response_generator("Code not provided","Failed"),status=status.HTTP_400_BAD_REQUEST)
        try:
            coupon = Coupon.objects.get(code=code)
            serializer = CouponSerializer(coupon)
            if coupon.is_expired():
                return Response(response_generator("Coupon is expired", "Failed", serializer.data), status=status.HTTP_200_OK)
            else:
                return Response(response_generator("Coupon applied successfully","Success",serializer.data), status=status.HTTP_200_OK)
        except Coupon.DoesNotExist:
            return Response(response_generator("Invalid coupon","Failed",[],"Coupon does not exists"), status=status.HTTP_404_NOT_FOUND)

class CouponView(APIView):
    
    def get(self,request):
        res, status = readWget(Coupon,{},CouponSerializer,"List of all coupons")
        return Response(res,status=status)
    
    # Discarded adding coupon using API, It should be done from Admin dashboard
    
    # def post(self,resquest):
    #     res, status = createWpost(resquest.data,CouponSerializer,"Coupon added successfully")
    #     return Response(res, status=status)