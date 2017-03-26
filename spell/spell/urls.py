from django.conf.urls import include, url
from django.contrib import admin
from api.views import SpellCorrectorView

urlpatterns = [
    # Examples:
    # url(r'^$', 'spell.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^spell/', SpellCorrectorView.as_view()),
]
