from django.contrib import admin

# Register your models here.
from .models import Bank, Branch
from django.contrib import admin

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    search_fields = ('bankName',)
    list_filter = ('bankName', )

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = (
        'branchName', 'bank', 'branchCity', 'branchDistrict',
    )
    search_fields = ('branchName', 'branchCity')
    list_filter = ('bank', )
