from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ViewDetails, ViewList

urlpatterns = {
    url(r'^ifsc/(?P<ifsc_code>[A-Za-z]{4}\w{7})$', ViewDetails.as_view()),
    url(r'^branches/(?P<branchCity>.*)/(?P<branchName>.*)$', ViewList.as_view())
}

urlpatterns = format_suffix_patterns(urlpatterns)