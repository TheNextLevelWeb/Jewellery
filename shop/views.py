from rest_framework import generics,filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryView(APIView):
    
    def get(self,request):
        try:
            queryset = Category.objects.all()
            serializer = CategorySerializer(queryset, many=True)
            return Response({"Message": "List of Categories", "Status": "Success", "Data": serializer.data})
        except Exception as e:
            return Response({"Message":f"Error occurd","Status":"Failed","Data": [],"Error":str(e)})
    
    def post(self,request):
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Message": "New category created", "Status": "Success", "Data": serializer.data})
            else:
                return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Errors": serializer.errors})

        except Exception as e:
            return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": str(e)})

    def patch(self,request,pk):
        try:
            category = Category.objects.get(id=pk)            
            serializer = CategorySerializer(category,request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Message": f"Category('{serializer.data['name']}') updated", "Status": "Success", "Data": serializer.data})
            else:
                return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Errors": serializer.errors})
        
        except Category.DoesNotExist:
            return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": "Category does not exists as per given id"})
        except Exception as e:
            return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": str(e)})

    def delete(self,request,pk):
        try:
            category = Category.objects.get(id=pk)
            category.delete()
            return Response({"Message": f"Category deleted", "Status": "Success", "Data": []})
        
        except Category.DoesNotExist:
                return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": "Category does not exists as per given id"})
        except Exception as e:
            return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": str(e)})



class ProductView(APIView):

    def get(self, request):
        try:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            return Response({"Message": "List of product", "Status": "Success", "Data": serializer.data})
        except Exception as e:
            return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": str(e)})

    def post(self, request):
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Message": "New product added", "Status": "Success", "Data": serializer.data})
            else:
                return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Errors": serializer.errors})

        except Exception as e:
            return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": str(e)})

    def patch(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
            serializer = ProductSerializer(product, request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"Message": f"Product('{serializer.data['name']}') updated", "Status": "Success", "Data": serializer.data})
            else:
                return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Errors": serializer.errors})
        
        except Product.DoesNotExist:
            return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": "Product does not exists as per given id"})
        except Exception as e:
            return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": str(e)})

    def delete(self, request, pk):
        try:
            category = Product.objects.get(id=pk)
            category.delete()
            return Response({"Message": f"Product deleted", "Status": "Success", "Data": []})

        except Product.DoesNotExist:
            return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": "Product does not exists as per given id"})
        except Exception as e:
            return Response({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": str(e)})


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']