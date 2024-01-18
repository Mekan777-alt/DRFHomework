from django_filters import rest_framework
from projects.api.views.project import get_client_ip
from projects.models import Project
from projects.service.search_ip import get_country_user

class ProjectFilters(rest_framework.FilterSet):
    min_total_amount = rest_framework.NumberFilter(field_name="total_amount", lookup_expr="gte")

    has_pledges = rest_framework.BooleanFilter(
        method='filter_by_has_pledges'
    )

    from_my_country = rest_framework.BooleanFilter(
        method='filter_by_from_my_country',
        label='From My Country'
    )

    def filter_by_has_pledges(self, queryset, name, value):
        return queryset.exclude(pledges__isnull=value)

    def filter_by_from_my_country(self, queryset, name, value):
        if value:
            client_ip = get_client_ip(self.request)
            user_info = get_country_user(client_ip)
            user_country = user_info.get('countryName', None) if user_info else None

            if user_country is not None:
                user_country = user_country.lowor()

            if user_country:
                return queryset.filter(country__country_name=user_country)

        return queryset

    class Meta:
        model = Project
        fields = ['min_total_amount', 'has_pledges', 'from_my_country']
