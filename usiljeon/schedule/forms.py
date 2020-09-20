from django import forms
from .models import Content,DateTime,UserTemp
import datetime

class ContentForm(forms.Form):
    creator=forms.CharField(max_length=50)
    contact=forms.CharField(widget=forms.Textarea)

    title=forms.CharField(max_length=50)
    department=forms.CharField(max_length=50)
    
    date=forms.DateTimeField(initial=datetime.datetime.now())
    runningdate=forms.IntegerField()

    runningtime=forms.IntegerField()
    location=forms.CharField(max_length=50)

    num_people=forms.IntegerField()
    reward=forms.CharField(max_length=50)

    condition=forms.CharField(widget=forms.Textarea)
    detail=forms.CharField(widget=forms.Textarea)

    password=forms.IntegerField()


class UserTempForm(forms.ModelForm):

    class Meta:
        model=UserTemp
        fields=('name','major','num_student','num_phone','num_account','password')

