from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)   #max_length参数检查字段长度
    email = forms.EmailField(required=False, label='Your email address')
    message = forms.CharField(widget=forms.Textarea)    #修改字段显示方式

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())    #判断有几个单词
        if num_words < 4:
            raise forms.ValidationError('not enough words')
        return message

