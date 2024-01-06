from django_filters import rest_framework


class ProjectFilters(rest_framework.FilterSet):
    min_total_amount = rest_framework.NumberFilter(field_name="total_amount", lookup_expr="gte")

    has_pledges = rest_framework.BooleanFilter(
        method='filter_by_has_pledges'
    )

    def filter_by_has_pledges(self, queryset, name, value):
        return queryset.exclude(pledges__isnull=value)
