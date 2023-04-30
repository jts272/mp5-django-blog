from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        # Tell the comment form which model to use and which fields we
        # want displayed on our form
        # Trailing comma denontes a tuple
        model = Comment
        fields = ('body',)
