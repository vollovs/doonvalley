from django import forms
from models import Member
from captcha.fields import CaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Button, Submit

class MemberForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field(
                'chinese_name',
                placeholder = 'Your Name',
            ),
            Field(
                'english_name',
                placeholder = 'Your Name',
            ),
            Field(
                'email',
                placeholder = 'name@gmail.com',
            ),
            Field(
                'phone',
                placeholder = '(519)-xxx-xxxx',
            ),
            Field(
                'club',
                placeholder = 'Please leave use a message here',
            ),
            Field(
                'captcha',
            ),                                                                      
            Submit('save', 'Save changes'),
            
        )
        
    chinese_name = forms.CharField(
        label = "Chinese Name",
        max_length=60, 
        required=True, 
    )
    
    english_name = forms.CharField(
        label = "English Name",
        max_length=60, 
        required=True, 
    )
    
    email = forms.EmailField(max_length=60, required=True)
    phone = forms.CharField(max_length=20)
    club = forms.CharField(max_length=20)
    captcha = CaptchaField()

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Member
        fields = ('chinese_name', 'english_name', 'email', 'phone', 'club')