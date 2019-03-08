# from django.conf.urls import url,path
from django.urls import include, path
from .views import * 

urlpatterns = [
    
    path('tollcmp', TollCmpReg, name='tollcmp'),
    path('taxpayer', TaxpayerReg, name='taxpayer'),
    path('display', display, name='display'),
        
]