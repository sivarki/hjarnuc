"""saltops_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from app_auth.views import Index
from django.urls import path,include
from django.views.decorators.cache import cache_page



urlpatterns = [
    path("",cache_page(30)(Index.as_view())),
    path("auth/",include("app_auth.urls")),
    path("asset/",include("app_asset.urls")),
    path("code/",include("app_code.urls")),
    path("sys/",include("app_sys.urls")),
    path("log/",include("app_log.urls")),
    path("tool/",include("app_tool.urls")),
    path("db/",include("app_db.urls")),
]
