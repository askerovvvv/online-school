from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver

# from teacher.models import TeacherInformation
from teacher.send_response_for_teacher import response_if_agreed, response_if_deleted


def is_teacher(obj):
    user = obj.user
    user.is_teacher = True
    user.save()
    response_if_agreed(user.email)


@receiver(pre_delete, sender="teacher.TeacherInformation")
def deleted(sender, instance, **kwargs):
    user = instance.user
    user.is_teacher = False
    user.save()
    response_if_deleted(user.email)

