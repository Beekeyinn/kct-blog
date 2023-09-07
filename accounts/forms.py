from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        help_text="Username should have at least 10 letters",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your user name"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Your user name"}
        ),
    )


class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        min_length=5,
        help_text="Username should have at least 10 letters",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your user name"}
        ),
    )
    password = forms.CharField(
        max_length=10,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Your user name"}
        ),
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        max_length=10,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Your user name"}
        ),
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Password Does not match.")
        return confirm_password
