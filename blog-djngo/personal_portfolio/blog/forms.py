from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
#widgets also take an argument attrs, which is a dictionary and allows us
#  to specify some CSS classes, which will help with formatting the
#  template for this view later. It also allows us to add some placeholder
#  text.

