from rest_framework.views import APIView
from .models import GiftCard
from .serializers import GiftCardSerializer
from rest_framework.response import Response
from rest_framework import status
from crudTempl import response_generator
from datetime import datetime

class GiftCardView(APIView):

    def post(self, request, code):

        username = request.data.get('username')
        if not username:
            return Response({"Message": "Invalid data", "Status": "Failed", "Data": [], "Errors": f"Payload does not have 'username' parameters"}, status.HTTP_400_BAD_REQUEST)
        
        try:

            giftcard = GiftCard.objects.get(code=code)
            if giftcard.is_redeemed:
                return Response(response_generator("Giftcard is expired !","Failed"), status=status.HTTP_200_OK)
            data = {
                "is_redeemed":True,
                "redeemed_at": datetime.now(),
                "redeemed_by": username
            }
            serializer = GiftCardSerializer(giftcard,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(response_generator("Congrats !", "Success", serializer.data))
            else:
                 return Response(serializer.errors)
        except GiftCard.DoesNotExist:
            return Response(response_generator("Invalid Giftcard", "Failed",errors="Giftcard does not exists."),status=status.HTTP_400_BAD_REQUEST)