from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from receipts.models import Receipt


# Create your views here.
@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_list": receipts,
    }
    return render(request, "receipts/receipt_list.html", context)
