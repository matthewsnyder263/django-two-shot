from django.urls import path
from receipts.views import (
    create_account,
    receipt_list,
    create_receipt,
    expense_category_list,
    account_list,
    create_expense_category,
)


urlpatterns = [
    path("accounts/create/", create_account, name="create_account"),
    path(
        "categories/create/",
        create_expense_category,
        name="create_expense_category",
    ),
    path("categories/", expense_category_list, name="expense_category_list"),
    path("accounts/", account_list, name="account_list"),
    path("create/", create_receipt, name="create_receipt"),
    path("", receipt_list, name="home"),
]
