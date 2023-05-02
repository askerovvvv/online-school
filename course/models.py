from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    slug = models.SlugField()

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category of a course')
    title = models.CharField(max_length=80, verbose_name='course name')
    description = models.TextField(verbose_name='Description of a course')
    course_image = models.ImageField(upload_to='courseimage/', verbose_name='Сourse photo') #TOdo: image show

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title


class Saved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_saved')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_saved')
    saved = models.BooleanField(default=False, verbose_name='Save')

    def __str__(self):
        if self.saved == True:
            return f'{self.user} saved {self.course}'
        else:
            return f"{self.user} deleted {self.course} from saved"
