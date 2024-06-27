from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Rewards
from .serializers import RewardSerializer
from rest_framework import status


class RewardView(APIView):

    def get(self, request, username):
        try:
            notifications = Rewards.objects.filter(
                username=username)
            serializer = RewardSerializer(notifications, many=True)
            return Response({"Message": f"Reward of '{username}'", "Status": "Success", "Data": serializer.data})

        except Rewards.DoesNotExist:
            return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": "Username does not exists"})

        except Exception as e:
            return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": str(e)})

    def post(self, request, username):

        try:
            request.data.update(
                {"rewardsStatus": request.data['rewardsStatus'].upper()})
            data = {'username': username, **request.data}
            serializer = RewardSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"Message": "New reward created successfully",
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
