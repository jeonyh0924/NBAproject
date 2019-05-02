from django import forms


class PostCreateForm(forms.Form):
    photo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control-file',
            }
        )
    )
    comment = forms.CharField(
        # 반드시 채워질 필요는 없다.
        required=False,
        # html 렌더링 위젯 textarea
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
    )
