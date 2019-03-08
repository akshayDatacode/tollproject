from django.forms import ModelForm
from .models import *

class TollCmpReg_form(ModelForm):
    class Meta:
        model = TollCmpReg_Model
        fields = '__all__'

class TaxpayerReg_form(ModelForm):
    class Meta:
        model = TaxpayerReg_Model
        fields = '__all__'

