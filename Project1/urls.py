from django.urls import path
from.import views
from .views import FAQViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'faqs', FAQViewSet)
urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos")
    path('',views.getData),
    path('', include(router.urls)),
     path('ckeditor/', include('ckeditor_uploader.urls')),
]