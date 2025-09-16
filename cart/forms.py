from django import forms
from .models import CheckoutFeedback

class CheckoutFeedbackForm(forms.ModelForm):
    class Meta:
        model = CheckoutFeedback
        fields = ["name", "feedback"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your name (optional)",
                "maxlength": "100"
            }),
            "feedback": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Tell us about your checkout experience...",
                "rows": "4",
                "required": True
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['feedback'].required = True
        self.fields['name'].required = False