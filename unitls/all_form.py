from django import forms
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    commen_text = forms.CharField(widget=CKEditorWidget(config_name= 'comment_ckeditor'))


class WriteForm(forms.Form):
    blog_text = forms.CharField(widget=CKEditorWidget(config_name='blog_ckeditor'))


class BbsForm(forms.Form):
    bbs_text = forms.CharField(widget=CKEditorWidget(config_name='comment_ckeditor'))