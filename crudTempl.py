from rest_framework import status


def readWget(model, argumentForModel,modelSrializer,message, alreadyList = False):
    try:
        ratingOfProduct = model.objects.filter(**argumentForModel)
        serializer = modelSrializer(ratingOfProduct, many=True)
        return (
            {"Message": message,
                "Status": "Success", "Data": serializer.data if alreadyList else [serializer.data]},
            status.HTTP_200_OK
        )
    except Exception as e:
        return (
            {"Message": "An unexpected error occurred",
                "Status": "Failed", "Data": [], "Errors": str(e)},
            status.HTTP_500_INTERNAL_SERVER_ERROR
        )

def createWpost(data, AppSerializer, message):
    try:
        serializer = AppSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return ({"Message": message, "Status": "Success", "Data": [serializer.data]}, status.HTTP_200_OK)
        else:
            return ({"Message": "Error occurred", "Status": "Failed","Data": [], "Errors": serializer.errors}, status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return ({"Message": "An unexpected error occurred",
                "Status": "Failed", "Data": [], "Errors": str(e)},status.HTTP_500_INTERNAL_SERVER_ERROR)

def deleteWdelete(model,pk,message):
    try:
        obj = model.objects.get(pk=pk)
        obj.delete()
        return (
            {"Message": message,
                "Status": "Success", "Data": []},status.HTTP_200_OK
        )

    except model.DoesNotExist as e:
        return (
            {"Message": "Does not exists", "Status": "Failed",
                "Data": [], "Errors": str(e)},
            status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return (
            {"Message": "An unexpected error occurred",
                "Status": "Failed", "Data": [], "Errors": str(e)},
            status.HTTP_500_INTERNAL_SERVER_ERROR
        )

def updateWpatch(model,pk,modelSerializer,data,message,valid_payload=[]):
    try:
        data = {key: data[key] for key in valid_payload if key in data}
        if not data:
            return ({"Message": "Invalid data", "Status": "Failed", "Data": [],"Errors":f"Payload does not have any of {', '.join(valid_payload)} parameters to update the rating"},status.HTTP_400_BAD_REQUEST)

        category = model.objects.get(pk=pk)
        serializer = modelSerializer(category, data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return ({"Message": message, "Status": "Success", "Data": serializer.data},status.HTTP_200_OK)
        else:
            return ({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Errors": serializer.errors}, status.HTTP_400_BAD_REQUEST)

    except model.DoesNotExist as e:
        return ({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": str(e)}, status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return ({"Message": f"Error occurd", "Status": "Failed", "Data": [], "Error": str(e)},status.HTTP_500_INTERNAL_SERVER_ERROR)

def response_generator(message, Status,data=[],errors=[]):
    if errors:
        return {"Message":message,"Status":Status,"Data":data,"Errors":errors}

    return {"Message":message,"Status":Status,"Data":data}