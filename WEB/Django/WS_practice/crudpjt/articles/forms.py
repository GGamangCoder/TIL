from django import forms


# Create your forms here.
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=16)
    content = forms.CharField()
