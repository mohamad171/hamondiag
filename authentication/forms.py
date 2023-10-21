from django.contrib.auth import get_user_model
from django import forms
class AuthForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["mobile"]
        widgets = {
            "mobile" : forms.TextInput(attrs={
                "type":"number",
                "placeholder": "شماره موبایل",
                "class": "form-group-input"
            })
        }
    def clean(self):
        mobile = self.cleaned_data.get("mobile")
        if len(str(mobile)) <11:
            self.add_error("mobile","شماره معتبر نمی باشد")
        if not str(mobile).startswith("09"):
            self.add_error("mobile","شماره معتبر نمی باشد")
class VerifyForm(forms.Form):
    verify_code = forms.IntegerField(widget=forms.TextInput(attrs={
        "type": "number",
        "placeholder": "کد تایید",
        "class": "form-group-input",
    }))
    def clean(self):
        code = str(self.cleaned_data.get("verify_code"))
        if len(code) > 4 and len(code) < 4 :
            self.add_error("verify_code","کد نامعتبر می باشد ")