# coding: UTF-8
from django.urls import path

from calls import views

app_name = 'calls'

urlpatterns = [
    path('new_call/', views.new_call, name="new_call"),
    path('update-calls/', views.update_calls, name="update_calls"),
    path('update-call-<int:call_id>/', views.update_call, name="update_call"),
    path('customer-new-call/', views.customer_new_call, name="customer_new_call"),
      
    path('customer-my-calls-unsolved/', views.customer_my_calls_unsolved, name="customer_my_calls_unsolved"),
    path('customer-my-calls-solved/', views.customer_my_calls_solved, name="customer_my_calls_solved"),

    path('update-unresolve-call-<int:call_id>/', views.customer_update_unresolve_call, name="customer_update_unresolve_call"),
    path('update-resolved-call-<int:call_id>/', views.customer_update_resolved_call, name="customer_update_resolved_call"),

    path('calls-under-six/', views.calls_under_six, name="calls_under_six"),
]