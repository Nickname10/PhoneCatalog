from django.shortcuts import render

from .models import CatalogTable


def index(request):
    return render(request, "index.html", context={"table_phone": CatalogTable.objects.all()})
