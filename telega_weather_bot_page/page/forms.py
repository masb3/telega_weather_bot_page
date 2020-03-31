from django import forms

from page.models import Comment


class FeedbackForm(forms.ModelForm):
    # name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    # text = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Enter your comment here'}))
    class Meta:
        model = Comment
        fields = ('name', 'comment',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Enter your comment here'}),
        }
        labels = {
            'name': '',
            'comment': '',
        }