from django import forms

class CustomerForm(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)
    age = forms.IntegerField(label='age', min_value=18, max_value=99)
    gender = forms.CharField(label='gender')
    phone_no = forms.IntegerField(label='phone_no')
    email = forms.EmailField(label='email', max_length=50)
    address = forms.CharField(label='address', max_length=250)
    district = forms.CharField(label='district', max_length=50)
    branch = forms.CharField(label='branch', max_length=50)
    account_type = forms.CharField(label='account_type', max_length=50)
    materials_req = forms.CharField(label='materials_req', max_length=50)
