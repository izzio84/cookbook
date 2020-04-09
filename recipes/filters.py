import django_filters
from . import models

def course(request):
    if request is None:
        return models.Course.objects.none()
    return models.Course.objects.order_by('course').all()

class RecipeFilter(django_filters.FilterSet):
     title = django_filters.CharFilter(lookup_expr='icontains')
     course = django_filters.ModelChoiceFilter(queryset=course)
    # class Meta:
    #     model = models.Recipe
    #     fields = ['course__course','title__icontains']