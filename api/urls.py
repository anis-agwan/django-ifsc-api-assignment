from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ViewDetails, ViewList

urlpatterns = {
    url(r'^ifsc/(?P<ifsc>[A-Za-z]{4}\w{7})$', ViewDetails.as_view()),
    url(r'^branches/(?P<city>.*)/(?P<bank>.*)$', ViewList.as_view())
}

urlpatterns = format_suffix_patterns(urlpatterns)