"""dj_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
# from rest_framework.authtoken.views import ObtainAuthToken
# from users.views import UserViewSet

from service.views import ServiceViewSet,ServiceSecondViewSet,ServiceMeinTitleViewSet,ServiceImgViewSet
from work.views import WorkViewSet
from team.views import TeamViewSet
from blog.views import ArticleBlogViewSet,CommentsBlogViewSet
from contact.views import QuestionViewSet
from subscribe.views import SubscribeViewSet

router = routers.DefaultRouter()
router.register(r'service/title', ServiceMeinTitleViewSet)
router.register(r'service/img', ServiceImgViewSet)
router.register(r'service/second', ServiceSecondViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'work', WorkViewSet)
router.register(r'team', TeamViewSet)
router.register(r'blog', ArticleBlogViewSet)
router.register(r'comments', CommentsBlogViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'subscribe', SubscribeViewSet)
# router.register(r'blog/sidebar', ArticleBlogBySidebarViewSet)






# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', ObtainAuthToken.as_view()),

    # path('api-auth/', include('rest_framework.urls')),
    # path('api/token',TokenObtainPairView.as_view()),
    # path('api/token/refresh',TokenRefreshView.as_view()),

    # path('?P<^events/{pk}/$',EventsIdViewSet.as_view()),

    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls.jwt')),
]\
               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
