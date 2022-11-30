from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

# router = routers.DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.api_root),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += format_suffix_patterns([
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
])
