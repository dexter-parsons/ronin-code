from django.conf.urls import patterns, include, url
import goals.views


urlpatterns = patterns('',
    url(r'^$', goals.views.ListGoalsView.as_view(),
        name='goals-list',),

    url(r'^new$', goals.views.CreateGoalsView.as_view(),
        name='goals-create',),
)