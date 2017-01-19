from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', 'megashop.views.home', name='home'),
]
