from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=16)
    content = forms.CharField()
