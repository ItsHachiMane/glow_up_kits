from django.db.models import DecimalField, ExpressionWrapper, F, Sum
from django.shortcuts import render

from .models import Kit, Order


def dashboard(request):
    kits = Kit.objects.all()
    orders = Order.objects.select_related("kit").order_by("-created_at")[:5]
    low_stock = kits.filter(stock_qty__lte=5)
    total_inventory_value = kits.aggregate(
        value=Sum(
            ExpressionWrapper(
                F("stock_qty") * F("cost"),
                output_field=DecimalField(max_digits=12, decimal_places=2),
            )
        )
    )["value"] or 0

    context = {
        "kit_count": kits.count(),
        "active_kit_count": kits.filter(is_active=True).count(),
        "low_stock_count": low_stock.count(),
        "recent_orders": orders,
        "low_stock_kits": low_stock,
        "total_inventory_value": total_inventory_value,
    }
    return render(request, "catalog/dashboard.html", context)
