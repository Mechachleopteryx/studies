from django import forms

from post.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('views',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post', )

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if "donald" in full_name.lower():
            raise forms.ValidationError("You cannot comment on this blog!")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return full_name
