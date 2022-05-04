from django.urls import include, path
from rest_framework.routers import SimpleRouter
from api.views import HomeCreateView, HomeListView, HomeRetrieveUpdateDestroyView

router = SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('add-home/', HomeCreateView.as_view(), name='add-home'),
    path('list-all-homes/', HomeListView.as_view(), name='home-list'),
    path('<str:uuid>/', HomeRetrieveUpdateDestroyView.as_view(), name='retrieve-update-delete-home'),
]
