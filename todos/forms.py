# forms.py

from django import forms
from .models import Todo, Category

class TodoForm(forms.ModelForm):

    type = forms.ChoiceField(
        choices=Todo.TYPES_CHOICES,
        required=True,
    )

    hungry = forms.ChoiceField(
        choices=Todo.HUNGRY_CHOICES,
        required=True,
    )

    time = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "time"}), 
        input_formats=["%H:%M"],
        required=False,
    )

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    directions = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),  
        required=False,
    )

    field_labels = {
        "type": "餐別",
        "hungry": "飽足感",
        "time": "用餐時間",
        "food":"餐點",
        "category": "種類",
        "directions": "描述",
    }
    

    class Meta:
        model = Todo
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        for field_name, label in self.field_labels.items():
            self.fields[field_name].label = label