from django.contrib import admin
from django.urls import path, include
from django.conf import settings

import users
import customer
import credits
import calls
import supports

urlpatterns = [
    path(r'users/', include('users.urls', namespace='users')),
    path(r'customer/', include('customer.urls', namespace='customer')),
    path(r'credits/', include('credits.urls', namespace='credits')),
    path(r'calls/', include('calls.urls', namespace='calls')),
    path(r'supports/', include('supports.urls', namespace='supports')),

    path('', users.views.login_view),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns