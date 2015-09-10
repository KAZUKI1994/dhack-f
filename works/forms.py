from django import forms
from .models import Works

WHERE = (
    (0, '京田辺'), 
    (1, '今出川'), 
)

CATEGORY = (
        (0,'生協バイト'),
        (1,'被験者バイト'),
        (2,'イベント'),
        (3,'PCバイト'),
        (4,'その他'),
)






class UserForm(forms.Form):
    title = forms.CharField(label="タイトル", max_length=100)
    name = forms.CharField(label="名前", max_length=100)
    phone = forms.CharField(label="電話番号", max_length=100)
    mail = forms.EmailField(label="メールアドレス", max_length=100)
    where = forms.ChoiceField(label="募集校地",choices=WHERE)
    #radio_choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    #multiple_choice = forms.MultipleChoiceField(choices=CHOICES)
    #multiple_checkbox = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)
    #file_fied = forms.FileField()
    #password_field = forms.CharField(widget=forms.PasswordInput)
    chategory = forms.ChoiceField(label="職種",choices=CATEGORY)
    need = forms.CharField(label="募集条件", max_length=100)
    what = forms.CharField(label="説明", widget=forms.Textarea)
    #boolean_field = forms.BooleanField()
