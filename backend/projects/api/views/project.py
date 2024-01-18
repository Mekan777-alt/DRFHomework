from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from projects.api.serializers.project import ProjectCreateUpdateSerializer, ProjectListDetailSerializer
from projects.models import Project
from rest_framework.permissions import IsAuthenticated
from projects.service.search_ip import get_country_user


class ProjectListCreateView(ListCreateAPIView):
    queryset = Project.objects.filter(is_approved=True)
    serializer_class = ProjectCreateUpdateSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        from_my_country = self.request.GET.get('from_my_country', None)
        queryset = Project.objects.filter(is_approved=True)

        user_country = get_country_user(self.request)

        if user_country is not None:
            user_country = user_country.upper()

        if from_my_country == 'true' and user_country:
            queryset = queryset.filter(country__country_name=user_country)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProjectListDetailSerializer(queryset, many=True)

        return Response(serializer.data)


class ProjectRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.filter(is_approved=True)
    serializer_class = ProjectListDetailSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = ProjectCreateUpdateSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(self.get_serializer(instance).data)
