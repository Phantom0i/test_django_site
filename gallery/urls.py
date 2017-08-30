from django.conf.urls import url

from gallery.views import IndexView

app_name = 'gallery'
urlpatterns = [
    url('^$', IndexView.as_view(), name='index'),
]
