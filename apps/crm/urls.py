from django.urls import path

from .views import create_view, IndexView, detail_view, update_view, delete_view, fund_wallet

app_name = 'crm'

urlpatterns = [
    path('', IndexView.as_view(), name='client-list'),
    path('create-client', create_view, name='client-create'),
    path('detail/<str:cid>', detail_view, name='client-detail'),
    path('update/<str:cid>', update_view, name='client-update'),
    path('delete/<str:cid>', delete_view, name='client-delete'),
    path('fund/<str:cid>', fund_wallet, name='fund-wallet'),
]
