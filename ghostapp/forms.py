from django import forms
from ghostapp.models import GhostPost

post_choices = (
    ("True", "Boast"),
    ("False", "Roast")
)


class GhostForm(forms.ModelForm):
    post = forms.CharField(max_length=280)
    is_boast = forms.ChoiceField(choices=post_choices)

    class Meta:
        model = GhostPost
        fields = ['post']
        exclude = (['time_submitted', 'sec_key'])
