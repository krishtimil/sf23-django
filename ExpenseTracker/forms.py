from django.forms import ModelForm
from ExpenseTracker.models import ExpenseRecord
from django.forms.widgets import DateInput, TextInput


class ExpenseForm(ModelForm):
    class Meta:
        model = ExpenseRecord
        fields = [
            "amount",
            "date",
            "category",
            "expense_type",
            "mode_of_payment",
            "remarks",
        ]
        widgets = {
            "date": DateInput(attrs={"type": "date"}),
            "remarks": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Name",
                }
            )
        }
        