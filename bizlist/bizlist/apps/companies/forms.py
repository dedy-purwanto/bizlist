from django import forms

from captcha.fields import ReCaptchaField

from .models import Inquiry

class InquiryForm(forms.ModelForm):

    captcha = ReCaptchaField()

    def save(self, *args, **kwargs):
        company = kwargs.pop('company')
        self.instance.company = company
        if 'product' in kwargs:
            product = kwargs.pop('product')
            self.instance.product = product

        return super(InquiryForm, self).save(*args, **kwargs)

    class Meta:
        model = Inquiry
        exclude = ('date_created', 'date_modified', 'company', 'product')

