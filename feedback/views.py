from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackView(APIView):

    def get(self,request):

        try:
            feedbacks = Feedback.objects.all()
            serializer = FeedbackSerializer(feedbacks,many=True)
            return Response(
                {"Message": "All feedbacks", "Status": "Success", "Data": [serializer.data]},
                status=status.HTTP_200_OK
            )
    
            
        except Exception as e:
            return Response(
                {"Message": "An unexpected error occurred",
                    "Status": "Failed", "Data": [], "Errors": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self,rquest):
        try:
            serializer = FeedbackSerializer(data=rquest.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"Message": "Feedback sent successfully", "Status": "Success",
                        "Data": [serializer.data]},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"Message": "Error occurred", "Status": "Failed",
                    "Data": [], "Errors": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"Message": "An unexpected error occurred",
                    "Status": "Failed", "Data": [], "Errors": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self,request,pk):

        try:
            feedback = Feedback.objects.get(id=pk)
            feedback.delete()
            return Response(
                {"Message": "Successfully deleted",
                    "Status": "Success", "Data": []},
                status=status.HTTP_200_OK
            )
        except Feedback.DoesNotExist:
            return Response(
                {"Message": "Does not exists", "Status": "Failed", "Data": [],
                 "Errors": "Specified id of feedback does not exists"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"Message": "An unexpected error occurred",
                    "Status": "Failed", "Data": [], "Errors": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
