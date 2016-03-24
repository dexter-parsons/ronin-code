from django import forms
from django.core.exceptions import ValidationError

from goals.models import Goals


class GoalsForm(forms.ModelForm):

    query = forms.CharField(
        label="Input your query here",
        required=True,
    )

    class Meta:
        model = Goals

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            goal_text = kwargs['instance'].goal_text
            kwargs.setdefault('initial', {})['input goals'] = goal_text

        return super(GoalsForm, self).__init__(*args, **kwargs)

