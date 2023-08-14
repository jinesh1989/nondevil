from .models import Task
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'note', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }