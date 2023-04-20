from django.urls import path
from receipts.views import (
    receipt_list,
    create_receipt,
    expense_category_list,
    account_list,
)

app_name = "receipts"

urlpatterns = [
    path("categories/", expense_category_list, name="category_list"),
    path("accounts/", account_list, name="account_list"),
    path("create/", create_receipt, name="create_receipt"),
    path("", receipt_list, name="home"),
]
