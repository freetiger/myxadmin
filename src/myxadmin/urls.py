# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = patterns('',
    url(r'^', include(xadmin.site.urls))
)
