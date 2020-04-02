from __future__ import unicode_literals

from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from . import models

# Register your models here.
@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'description', 'image_tag')
    prepopulated_fields = {'slug': ('course',)}


class IngredientInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.Ingredient
    extra = 0


class CookingStepInline(SortableInlineAdminMixin,admin.TabularInline):
    model = models.CookingStep
    extra = 0


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    #list_per_page = 12
    list_display = ['title','image_tag']
    list_display_links = ['title']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [IngredientInline, CookingStepInline]


# @admin.register(models.CookingStep)
# class CookingStepAdmin(SortableAdminMixin, admin.ModelAdmin):
#     list_display = ['step', 'image_tag']
    # ordering = ['step']

