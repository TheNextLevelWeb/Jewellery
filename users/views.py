from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import jwt
import datetime
import json
from .serializers import UserSerializer, LoginSerializer, ChangePasswordSerializer, ForgotPasswordSerializer, SOWSerializer
from users.models import Users
from bcrypt import hashpw, gensalt, checkpw

def jsonResponse(message = "", status="Success",data = [],errors = ""):
    return {
        "message": message,
        "status": status,
        "data": data,
        "errors": errors,
    }

def generate_token(username):
    ist_timezone = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    current_time_ist = datetime.datetime.now(ist_timezone)

    token = jwt.encode({
        'username': username,
        'exp': current_time_ist + datetime.timedelta(days=7)
    }, "app.config['SECRET_KEY']", algorithm='HS256')
    return token

class Register(APIView):

    def post(self, request):
        data = request.data
        print(data)
        data['password'] = hashpw(
            data.get('password').encode('utf-8'), gensalt()).decode('utf-8')
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Registered successfully", "Is_registered": True}, status=status.HTTP_201_CREATED)
        

        return Response(
            {
                "message": "Failed to Register",
                "Is_registered": False,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

class LoginView(APIView):
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                user = Users.objects.get(username=username)
            except Users.DoesNotExist:
                return Response({'Message': 'Username does not exists.','Is_loggedIn':False}, status=status.HTTP_401_UNAUTHORIZED)

            try:
                if checkpw(password.encode('utf-8'),
                           user.password.encode('utf-8')):
                    return Response({'Message': 'Authentication successful', 'Is_loggedIn': True, 'token': generate_token(username)}, status=status.HTTP_200_OK)
            except:
                return Response({'Message': 'Incorrect username or password', 'Is_loggedIn': False}, status=status.HTTP_401_UNAUTHORIZED)

            else:
                return Response({'Message': 'Incorrect username or password', 'Is_loggedIn': False}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"Message": "Error occurred", 'Is_loggedIn': False, "Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class TokenAuthenticationView(APIView):
    def post(self, request):
        token_key = request.data.get('token')

        if token_key:
            try:
                jwt.decode(token_key, "app.config['SECRET_KEY']", algorithms=['HS256'])
                return Response({"Message": "Authenticated successfully", "Is_authenticated": True}, status=status.HTTP_200_OK)
            except jwt.ExpiredSignatureError:
                return Response({"Message": "Signature expired. Please log in again.", "Is_authenticated": False}, status=status.HTTP_400_BAD_REQUEST)
            
            except jwt.InvalidTokenError:
                return Response({"Message": "Invalid token", "Is_authenticated": False},
                         status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({"Message": "Token not provided", "Is_authenticated": False}, status=status.HTTP_400_BAD_REQUEST)

class ChangePassword(APIView):

    def post(self, request):

        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():

            username = request.data.get('username')
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            try:
                user = Users.objects.get(username=username)
            except Users.DoesNotExist:
                return Response({'Message': 'User does not exist','Is_changed_password':False}, status=status.HTTP_404_NOT_FOUND)

            if user.check_password(old_password):
                user.set_password(new_password)
                return Response({'Message': 'Password changed successfully', 'Is_changed_password': True}, status=status.HTTP_200_OK)
            else:
                return Response({'Message': 'Incorrect old password', 'Is_changed_password': False}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message": "Error occurred", 'Is_changed_password': False, "Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordView(APIView):
    
    def post(self,request):
        serializer = ForgotPasswordSerializer(data=request.data)

        if serializer.is_valid():

            new_password = serializer.validated_data['new_password']
            username = serializer.validated_data['username']

            try:
                user = Users.objects.get(username=username)
            except Users.DoesNotExist:
                return Response({'Message': 'User does not exist','Is_changed_password':False}, status=status.HTTP_404_NOT_FOUND)
            user.set_password(new_password)
            return Response({'Message': 'Password changed successfully', 'Is_changed_password': True}, status=status.HTTP_200_OK)
        else:
            return Response({"Message": "Error occurred", 'Is_changed_password': False, "Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class SOWListView(APIView):

    def get(self, request, username, fieldName):
        user = Users.objects.get(username=username)
        field_data = getattr(user, fieldName, None)
        if field_data is None:
            return Response(f"Field {fieldName} does not exist on user model", status=400)
        data = json.loads(str(field_data))
        return Response(data)

    def post(self, request, fieldName,username):
        user = Users.objects.get(username=username)
        new_data = request.data.get(fieldName)
        if not new_data:
            return Response(f"Provided post data is incorrect.", status=500)
        field_data = getattr(user, fieldName, None)
        if field_data is None:
            return Response(f"Field {fieldName} does not exist on user model", status=400)

        data_list = json.loads(str(field_data))
        data_list.append(new_data)
        updated_data = json.dumps(data_list)

        serializer = SOWSerializer(
            user, data={fieldName: updated_data}, partial=True)
        try:
            if serializer.is_valid():
                setattr(user, fieldName, updated_data)
                user.save()
                return Response("Added data")
            else:
                return Response(f"Cannot add data,\n\n {serializer.errors}", status=400)
        except Exception as e:
            return Response(f"Cannot add {e}", status=500)

    def delete(self, request, username, fieldName):
        user = Users.objects.get(username=username)

        index = request.data.get('index')

        if not index and index != 0:
            return Response(f"Provided post data is incorrect.", status=500)

        field_data = getattr(user, fieldName, None)
        if field_data is None:
            return Response(f"Field {fieldName} does not exist on user model", status=400)

        data_list = json.loads(str(field_data))
        if index < 0 or index >= len(data_list):
            return Response(f"Index {index} is out of bounds", status=400)
        data_list.pop(index)
        updated_data = json.dumps(data_list)

        serializer = SOWSerializer(
            user, data={fieldName: updated_data}, partial=True)
        try:
            if serializer.is_valid():
                setattr(user, fieldName, updated_data)
                user.save()
                return Response("Deleted Address")
            else:
                return Response(f"Cannot delete address,\n\n {serializer.errors}", status=400)
        except Exception as e:
            return Response(f"Cannot delete {e}", status=500)

    def patch(self, request, username, fieldName):
        try:
            user = Users.objects.get(username=username)

            index = request.data.get('index')
            new_data = request.data.get('new')

            if not index and index != 0 or not new_data:
                return Response(f"Provided post data is incorrect.", status=500)

            if index is None or new_data is None:
                return Response("There is an issue with the index or new_data key provided.", status=400)

            field_data = getattr(user, fieldName, None)
            if field_data is None:
                return Response(f"Field {fieldName} does not exist on user model", status=400)

            data_list = json.loads(str(field_data))
            if index < 0 or index >= len(data_list):
                return Response(f"Index {index} is out of bounds", status=400)
            data_list[index] = new_data
            updated_data = json.dumps(data_list)

            serializer = SOWSerializer(
                user, data={fieldName: updated_data}, partial=True)
            try:
                if serializer.is_valid():
                    setattr(user, fieldName, updated_data)
                    user.save()
                    return Response("Updated data")
                else:
                    return Response(f"Cannot update data,\n\n {serializer.errors}", status=400)
            except Exception as e:
                return Response(f"Cannot update {e}", status=500)
        except Exception as e:
            return Response(f"Error occurred: {e}", status=500)

class ProfileView(APIView):

    def get(self, request, username):
        try:
            user = Users.objects.get(username=username)
            profile_data = {
                "Name": user.name,
                "Phone_number": user.phone_number,
                "Email": user.email,
                "Location": user.location
            }
            return Response(profile_data, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response({"Message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Message": f"An error occurred: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self,request, username):
        try:
            user = Users.objects.get(username=username)
            user.delete()
            return Response({"Message": "Deleted successfully", "Is_user_delete": True})
        except Users.DoesNotExist:
            return Response({"Message": "User does not exists", "Is_user_delete": False})

    def patch(self, request, username):
        try:
            user = Users.objects.get(username=username)
            data = request.data
            
            if not data or not any(map(lambda each: each in data.keys(), [
                    'name', 'phone_number', 'email', 'location'])):
                return Response({"Message": f"No parameter given", "Is_profile_update": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            if 'name' in data:
                user.name = data['name']
            if 'phone_number' in data:
                user.phone_number = data['phone_number']
            if 'email' in data:
                user.email = data['email']
            if 'location' in data:
                user.location = data['location']

            user.save()
            return Response({"Message": "Profile updated successfully", "Is_profile_update": True}, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response({"Message": "User not found", "Is_profile_update": False}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            if "users_users.email" in str(e):
                return Response({"Message": f"Email is already taken","Is_profile_update":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
            if "users_users.phone_number" in str(e):
                return Response({"Message": f"Email is already taken","Is_profile_update":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({"Message": f"An error occurred: {e}", "Is_profile_update": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
