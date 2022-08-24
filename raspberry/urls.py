from django.contrib import admin
from django.urls import path

import raspberry.views
from views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("machines/", MachineAPI.as_view(), name="machines"),
    # path("machines/<int:pk>/", MachineAPI.as_view(), name="machinesParameters"),
    path(r'^$', raspberry.views.index(), name='home')
]
