from django import forms

from clubs.models import Clubs, Countries, Articles


class AddArticleForm(forms.ModelForm):
    club = forms.ModelChoiceField(queryset=Clubs.objects.all(), required=False, empty_label='Виберіть команду',
                                  label='Команда')

    # country = forms.ModelChoiceField(queryset=Countries.objects.all(), empty_label='Виберіть країну', label='Країна')

    class Meta:
        model = Articles
        fields = ['title', 'content', 'photo', 'club']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 90, 'rows': 8}),
        }


class EditClubsForm(forms.ModelForm):
    class Meta:
        model = Clubs
        fields = ['name', 'emblem', 'town', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'town': forms.TextInput(attrs={'class': 'form-input'})
        }
