from django.db.models import  Sum
from ExpenseTracker.models import ExpenseRecord


fields=["mode_of_payment","expense_type","category","date"]
def get_data():
    for field_str in fields:
        qs = ExpenseRecord.objects.all().values(field_str).annotate(total=Sum("amount"))
        result_x = []
        result_y = []
        for item in qs:
            result_x.append(str(item[field_str])) #str cast chai datetime datatype ko laagi
            result_y.append(item["total"])
        yield {"x_values": result_x, "y_values": result_y}