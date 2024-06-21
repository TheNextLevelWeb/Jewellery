from rest_framework.views import APIView
from crudTempl import readWget, deleteWdelete
from .models import Cart
from .serializers import CartSerializers, AddToCartSerializers
from rest_framework.response import Response
from rest_framework import status
from users.models import Users
from shop.models import Product

class CartView(APIView):

    def get(self,request,username):
        res, status = readWget(
            Cart, {'username': username}, CartSerializers, "List of products in cart",True)
        return Response(res,status=status)
    
    def post(self,request,username):
        try:
            product = request.data.get('product')
            if product is None:
                raise Exception
        except:
            return Response({"Message": "Invalid data", "Status": "Failed", "Data": [], "Errors": f"Payload does not have product parameters"}, status.HTTP_400_BAD_REQUEST)

        try:
            user = Users.objects.get(username=username)
            prod = Product.objects.get(id=product)
            cart_item, isCreated = Cart.objects.get_or_create(
                username=user, product=prod)
            print(cart_item)
            if not isCreated:
                cart_item.quantity += 1
                cart_item.save()
                return Response({"Message": " Increased the quantity", "Status": "Success", "Data": [AddToCartSerializers(cart_item).data]}, status.HTTP_200_OK)
            else: 
                return Response({"Message": "Product added to cart", "Status": "Success", "Data": [AddToCartSerializers(cart_item).data]}, status.HTTP_200_OK)
        
        except Users.DoesNotExist:
            return Response({"Message": f"User does not exists", "Status": "Failed", "Data": [], "Error": "Given username does not exists"}, status.HTTP_400_BAD_REQUEST)
        
        except Product.DoesNotExist:
            return Response({"Message": f"Product does not exists", "Status": "Failed", "Data": [], "Error": "Given product does not exists"}, status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"Message": "An unexpected error occurred",
                    "Status": "Failed", "Data": [], "Errors": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        res, status = deleteWdelete(
            Cart, pk, "Removed product successfully")
        return Response(res, status=status)
