# coding: UTF-8
from django.urls import path

from calls import views

app_name = 'calls'

urlpatterns = [
    path('new_call/', views.new_call, name="new_call"),
    path('update-calls/', views.update_calls, name="update_calls"),
    path('update-call-<int:call_id>/', views.update_call, name="update_call"),
    path('customer-new-call/', views.customer_new_call, name="customer_new_call"),
    path('customer-my-calls/', views.customer_my_calls, name="customer_my_calls"),
    path('update-unresolve-call-<int:call_id>/', views.customer_update_unresolve_call, name="customer_update_unresolve_call"),
]