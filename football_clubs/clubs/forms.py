from django import forms

from clubs.models import Clubs, Countries, Articles


class AddArticleForm(forms.ModelForm):
    club = forms.ModelChoiceField(queryset=Clubs.objects.all(), empty_label='Виберіть команду', label='Команда')
    country = forms.ModelChoiceField(queryset=Countries.objects.all(), empty_label='Виберіть країну', label='Країна')

    class Meta:
        model = Articles
        fields = ['title', 'content', 'photo', 'club', 'country']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 90, 'rows': 11}),
        }
