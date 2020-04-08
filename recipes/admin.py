from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from django_summernote.admin import SummernoteModelAdmin
from django.db import models as m
from django.forms import  Textarea
from . import models

# Register your models here.
@admin.register(models.Course)
class CourseAdmin(SummernoteModelAdmin):
    list_display = ('course', 'description', 'image_tag')
    prepopulated_fields = {'slug': ('course',)}
    summernote_fields = '__all__'


class IngredientInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.Ingredient
    extra = 0


class CookingStepInline(SortableInlineAdminMixin,admin.TabularInline):
    model = models.CookingStep
    formfield_overrides = {
        m.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    extra = 0


@admin.register(models.Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    #list_per_page = 12
    list_display = ['title','short_description','course','image_tag','status']
    #list_select_related = ('course')
    list_display_links = ['title']
    list_filter = ('status', 'created_on','course')
    search_fields = ('title', 'short_description', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [IngredientInline, CookingStepInline]
    actions = ['approve_comments']
    save_as = True
    save_on_top = True
    summernote_fields = '__all__'





# @admin.register(models.CookingStep)
# class CookingStepAdmin(SortableAdminMixin, admin.ModelAdmin):
#     list_display = ['step', 'image_tag']
    # ordering = ['step']

