from django import forms

class postform(forms.Form):
    content = forms.CharField(label="content",widget=forms.Textarea(attrs={'class':'form-control','cols': 60, 'rows': 5}))
    sources = forms.CharField(label="sources",widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 5}))
    category = forms.CharField(label="category",widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 5}))
    languages = forms.CharField(label="languages",widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 5}))
    country = forms.CharField(label="country", widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 5}))
