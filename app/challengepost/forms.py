from django import forms

from .models import challengePost, challengeComment


class challengeCreateForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control-file',
            }
        )
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control-file',
            }
        )
    )

    def save(self, *args, **kwargs):
        post = challengePost.objects.create(
            title=self.cleaned_data['title'],
            text=self.cleaned_data['text'],
            **kwargs,
        )

        return post


class challengeCommentForm(forms.ModelForm):
    class Meta:
        model = challengeComment
        fields = [
            'content',

        ]
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 2,
                }
            )
        }
