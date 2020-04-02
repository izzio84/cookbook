from django.db import models
from django.utils.translation import ugettext as _
from django_better_admin_arrayfield.models.fields import ArrayField
from django.utils.safestring import mark_safe
from filer.fields.image import FilerImageField
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
# Create your models here.

class Test(models.Model):
    ingredients = ArrayField(models.CharField(max_length=20), blank=True, null=True)

class Recipe(models.Model):

    # pk = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    preparation_time = models.CharField(max_length=200)
    cooking_time = models.CharField(max_length=200)
    course = models.ForeignKey('recipes.course', null=True, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    recipe_image = FilerImageField(null=True, blank=True, related_name="recipe_image",on_delete= models.CASCADE)
    class Meta:
        verbose_name = _("Recipe")
        verbose_name_plural = _("Recipes")

    def image_tag(self):
        if self.recipe_image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.recipe_image.url)
        else:
            return mark_safe('<img src="data:image/gif;base64,R0lGODlhAQABAIAAAP7//wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" style="width: 45px; height:45px;" />')
    image_tag.short_description = 'Image' 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"pk": self.pk})


class Course(models.Model):
    course_id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    course = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='author',auto_created=True)
    logo = FilerImageField(null=True, blank=True, related_name="logo_company",on_delete= models.CASCADE)
    class Meta:
        ordering = ['-course']

    def __str__(self):
        return self.course
    
    def image_tag(self):
        if self.logo:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.logo.url)
        else:
            return mark_safe('<img src="data:image/gif;base64,R0lGODlhAQABAIAAAP7//wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" style="width: 45px; height:45px;" />')
    image_tag.short_description = 'Thumb'    

class Ingredient(models.Model):
    #pk = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    qty = models.CharField(max_length=200,blank=True)
    ingredient = models.CharField(max_length=200,blank=True)
    order = models.PositiveIntegerField(blank=False, null=False)
    recipe = models.ForeignKey(Recipe, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return 'Ingredient: {0}'.format(self.ingredient)

    def __unicode__(self):
        return 'Ingredient: {0}'.format(self.ingredient)


    class Meta:
        ordering = ['order']
        verbose_name = _("Ingredient")
        verbose_name_plural = _("Ingredients")

    def __str__(self):
        return self.ingredient

    def get_absolute_url(self):
        return reverse("ingredient_detail", kwargs={"pk": self.pk})


class CookingStep(models.Model):

    step = models.CharField(max_length=200)
    step_image = FilerImageField(null=True, blank=True, related_name="step_image",on_delete= models.CASCADE)
    order = models.PositiveIntegerField(blank=False, null=False)
    recipe = models.ForeignKey(Recipe, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return 'Step: {0}'.format(self.step)

    def __unicode__(self):
        return 'Step: {0}'.format(self.step)
    
    def image_tag(self):
        if self.step_image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.step_image.url)
        else: 
            return mark_safe('<img src="data:image/gif;base64,R0lGODlhAQABAIAAAP7//wAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" style="width: 45px; height:45px;" />')
    image_tag.short_description = 'Step Image'

    class Meta:
        ordering = ['order']
        verbose_name = _("Cooking Step")
        verbose_name_plural = _("Cooking Steps")

    def __str__(self):
        return self.step

    def get_absolute_url(self):
        return reverse("cookingstep_detail", kwargs={"pk": self.pk})





