"""
    Django forms are very similar to models which consists of class attributes as form fields.
    Django comes with some built-in form fields that you can use to quickly create the form you need.
    This form will require author(CharField) and body(CharField) fields
    NOTE: If the CharField of your form == model CharField, make sure both have the same max_length value.
"""
from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name'
        })
    )
    
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Leave a comment'
        }
    ))

    # go to views.py and extend 'blog_detail' function