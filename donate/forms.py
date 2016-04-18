from django import forms

class StripeForm(forms.Form):
    stripe_token = forms.CharField()
    occupation = forms.CharField()
    employer = forms.CharField()
    amount = forms.CharField()
    #token_data = forms.CharField()


class BackerForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    email = forms.CharField(label='Email', max_length=200, required=False)
    street1 = forms.CharField(label='Street 1', max_length=200)
    street2 = forms.CharField(label='Street 2', max_length=200, required=False)
    city = forms.CharField(label='City', max_length=200)
    state = forms.CharField(label='State', max_length=200)
    zipcode = forms.CharField(label='Zip Code', max_length=200)
    phone = forms.CharField(label='Phone', max_length=200, required=False)


class DonateForm(forms.Form):
	stripe_token = forms.CharField()
	occupation = forms.CharField()
	employer = forms.CharField()
