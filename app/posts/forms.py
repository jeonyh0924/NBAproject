from django import forms

from posts.models import Post, Comment


class PostCreateForm(forms.Form):
    title = forms.CharField(
        label='글 제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    photo = forms.ImageField(
        label='사진',
        widget=forms.FileInput(
            attrs={
                'class': ' form-control-file',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        # 반드시 채워질 필요는 없다.
        required=False,
        # html 렌더링 위젯 textarea
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    tag = forms.CharField(
        label='보류',
        # 반드시 채워져 있을 필요는 없음
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    def save(self, author):
        post = Post.objects.create(
            user=author,
            title=self.cleaned_data['title'],
            image=self.cleaned_data['photo'],
            content=self.cleaned_data['content'],
            tag=self.cleaned_data['tag'],
        )
        comment_content = self.cleaned_data.get('comment')
        if comment_content:
            post.comments.create(
                author=post.user,
                content=comment_content,
            )
        # 1. post 생성 시 , comment 생성 (선택적)
        # 만약에 comment 항목이 있다면,
        # 생성한 Post에 연결되는 Comment 를 생성
        # author = 생성한 Post에 연결되는 author와 동일
        # Post = 생성한 Post

        return post


class CommentCreateForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 2,
            }
        ),
    )

    def save(self, post, **kwargs):
        content = self.cleaned_data['content']

        return post.comments.create(
            content=content,
            **kwargs,
        )


class PostForm(forms.ModelForm):
    # 1. posts.views.post_create
    # 2. templates/posts/post_create.html
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'tag',
        ]

        widgets = {
            'title': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 1,
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control-file',
                }
            ),
            'tag': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 1,
                }
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
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
