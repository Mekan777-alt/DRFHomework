from django.urls import path
from rest_framework.routers import DefaultRouter

from projects.api.views.project import ProjectListCreateView, ProjectRetrieveUpdateDestroyView
from projects.api.views.reward import RewardAPIView
from projects.api.views.project_update import ProjectUpdateViewSet
from projects.api.views.pledge import PledgeViewSet

router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend([
    path('projects', ProjectListCreateView.as_view(), name='projects_list'),
    path('projects/<int:pk>', ProjectRetrieveUpdateDestroyView.as_view(), name='projects_detail'),
    path('projects/<int:pk>/updates', ProjectUpdateViewSet.as_view({
        'post': 'create'
    }), name='projects_update'),
    path('projects/<int:pk>/pledges', PledgeViewSet.as_view({
        'post': 'create'
    }), name='pledges'),
    path('projects/reward', RewardAPIView.as_view(), name='reward'),
    path('projects/reward/<int:pk>', RewardAPIView.as_view())
])
