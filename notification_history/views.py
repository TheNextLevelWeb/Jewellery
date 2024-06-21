from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notification_history
from .serializers import NHSerializer
from rest_framework import status
class NHView(APIView):
    
    def get(self, request,username):
        try:
            notifications = Notification_history.objects.filter(
                username=username)
            serializer = NHSerializer(notifications,many=True)
            return Response({"Message": f"Notification history for '{username}'", "Status": "Success", "Data": serializer.data})
        
        except Notification_history.DoesNotExist:
            return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": "Username does not exists"})

        except Exception as e:
            return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": str(e)})

    def post(self,request,username):
        
        try:
            data = {'username':username,**request.data}
            serializer = NHSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"Message": "Successfully notification added",
                        "Status": "Success", "Data": [serializer.data]},
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
    
    def delete(self, request, username,pk):
        try:
            notification = Notification_history.objects.get(
                username=username,id=pk)
            notification.delete()
            return Response(
                {"Message": "Successfully deleted notification",
                    "Status": "Success", "Data": []},
                status=status.HTTP_200_OK
            )
            
        except Notification_history.DoesNotExist:
            return Response(
                {"Message": "User or notification not found", "Status": "Failed", "Data": [],
                 "Errors": "User or notification not found(Make sure you entered correct username and notification id)"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"Message": "An unexpected error occurred",
                    "Status": "Failed", "Data": [], "Errors": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
