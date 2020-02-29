from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class NewCommentForm(forms.Form):
    comment = forms.CharField(help_text='Enter a comment about blog post here.',widget=forms.Textarea)

    def clean_comment_data(self):
        data = self.cleaned_data['comment']

        if len(data)>1000:
            raise ValidationError(_('Comment is too long - must be less than 1000 character'))

        return data
    