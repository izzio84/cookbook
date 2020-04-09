from django.shortcuts import render
from django.views import generic
from . import models
from django_filters.views import FilterView
from . import filters
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_filters.views import BaseFilterView

class RecipeList(BaseFilterView,generic.ListView):
    queryset = models.Recipe.objects.filter(status=1).order_by('-created_on')
    
    model = models.Recipe
    template_name = 'index.html'
    paginate_by = 30
    courselist = models.Course.objects.order_by('course').all()
    filterset_class = filters.RecipeFilter
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(RecipeList, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['courselist'] = models.Course.objects.order_by('course')
    #     return context
    

class RecipeDetail(generic.DetailView):
    model = models.Recipe
    template_name = 'recipe_detail.html'