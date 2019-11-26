from django import forms

from users.forms import ModelFormWithSubmit
from .models import Call, CallTag

# Teammember or super user

class NewCallForm(ModelFormWithSubmit):

    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=CallTag.objects.all(),
        )

    class Meta:
        model = Call
        fields = ('title', 'customer', 'tags', 'content', 'solved', )

class ModifyCallForm(ModelFormWithSubmit):

    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=CallTag.objects.all(),
        )

    class Meta:
        model = Call
        fields = ('title', 'customer', 'tags', 'content', 'solved', )

# Customer

class CustomerCallForm(ModelFormWithSubmit):

    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=CallTag.objects.all(),
        )

    class Meta:
        model = Call
        fields = ('title', 'tags', 'content', )

class CustomerModifyCallForm(ModelFormWithSubmit):

    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=CallTag.objects.all(),
        )

    class Meta:
        model = Call
        fields = ('title','tags', 'content', )

class CustomerModifyCallFormSolved(ModelFormWithSubmit):
    class Meta:
        model = Call
        fields = ('note', )