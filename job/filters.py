import django_filters
from .models import job  #   <=هنا يمكن ال (j) بالمكبر

class JobFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = job
        fields = '__all__'
        exclude = ['owner','publshed_at','image','salary','vacancy','slug']