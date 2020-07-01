import csv

from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.views import View
from .models import Bank, Branch
from .serializers import BranchSerializer

# Create your views here.
class ViewImport(View):
    def get(self,request):
        return render(request, 'view_import.html')

    def post(self, request):
        csv_data = request.FILES.get('csv_data')
        decoded_data = csv_data.read().decode('utf-8').splitlines()
        dict_reader = csv.DictReader(decoded_data)
        count = 0
        for row in dict_reader:
            bankName = row.get('bank_name')
            ifsc_code = row.get('ifsc')
            branchName = row.get('branch')
            bankAddress = row.get('address')
            bankCity = row.get('city')
            bankDistrict = row.get('district')
            bankState = row.get('state')
            print("IFSC code: {}".format(ifsc_code))
            if not ifsc_code:
                break
            bankObject, created = Bank.objects.get_or_create(
                name= bankName
            )
            defaults_branch = {
                'name': branchName,
                'bank': bankObject,
                'address': bankAddress,
                'city': bankCity,
                'district': bankDistrict,
                'state': bankState
            }

            branchObject, created = Branch.objects.update_or_create(
                ifsc_code=ifsc_code, defaults=defaults_branch
            )
            if created:
                print("row created{}".format(defaults_branch))

            count += 1
        messages.success(request, "{} rows imported.".format(count))

        return render(request, 'view_import.html')

class ViewDetails(View):
    def get(self, request, ifsc_code):
        branch = Branch.objects.filter(ifsc_iexact=ifsc_code).first()
        serializer = BranchSerializer(branch)
        return JsonResponse(serializer.data, safe=False)

class ViewList(View):
    def get(self, request, bankCity, bankName):
        branch_qset = Branch.objects.filter(bankCity_iexact=bankCity, bankName_icontains=bankName)
        serializer = BranchSerializer(branch_qset, many=True)
        return JsonResponse(serializer.data, safe=False)