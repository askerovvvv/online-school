import django.dispatch
from django.contrib.auth import get_user_model
from django.core.signals import request_finished
from django.db import models

from teacher.signals import is_teacher

User = get_user_model()

t = django.dispatch.Signal()


class TeacherInformation(models.Model):
    telephone_number = models.CharField(max_length=25)
    image = models.ImageField(upload_to='teacherimage/')
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    name_of_lesson = models.CharField(max_length=50)
    teacher = models.BooleanField()

    def __str__(self):
        return f"{self.user} teaches {self.name_of_lesson}"
    # experince

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_self = TeacherInformation.objects.get(pk=self.pk)
            if self.teacher != old_self.teacher:
                is_teacher(self)
                print('__________________')
        return super(TeacherInformation, self).save(*args, **kwargs)
