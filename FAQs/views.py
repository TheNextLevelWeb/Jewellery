from rest_framework.response import Response
from rest_framework.views import APIView
from crudTempl import readWget, createWpost, updateWpatch, deleteWdelete
from .models import FAQs, PrivacyPolicy
from .serializers import FAQsSerializer, PrivacyPolicySerializer

class FAQsView(APIView):

    def get(self,request):
        res, status = readWget(FAQs, {}, FAQsSerializer, "List of FAQs")
        return Response(res,status=status)

    def post(self,request):
        res, status = createWpost(request.data, FAQsSerializer,"FAQ created successfully")
        return Response(res,status=status)

    def patch(self,request,pk):
        res, status = updateWpatch(FAQs,pk, FAQsSerializer,request.data,"FAQ updated successfully",['quetion','answer'])
        return Response(res,status=status)

    def delete(self,request,pk):
        res, status = deleteWdelete(FAQs, pk,"FAQ deleted successfully")
        return Response(res,status=status)
    

class PrivacyPolicyView(APIView):

    def get(self, request):
        res, status = readWget(PrivacyPolicy, {}, PrivacyPolicySerializer,
                               "List of Privacy policy")
        return Response(res, status=status)

    def post(self, request):
        res, status = createWpost(
            request.data, PrivacyPolicySerializer, "Privacy policy created successfully")
        return Response(res, status=status)

    def patch(self, request, pk):
        res, status = updateWpatch(
            PrivacyPolicy, pk, PrivacyPolicySerializer, request.data, "Privacy policy updated successfully", ['PrivacyPolicy_Title', 'PrivacyPolicy_Detail'])
        return Response(res, status=status)

    def delete(self, request, pk):
        res, status = deleteWdelete(
            PrivacyPolicy, pk, "Privacy policy deleted successfully")
        return Response(res, status=status)
