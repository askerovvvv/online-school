from django.contrib.auth import get_user_model
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver

# from teacher.models import TeacherInformation
from teacher.send_response_for_teacher import response_if_agreed, response_if_deleted

User = get_user_model()


def is_teacher(users_id, status):
    if status == 'approve':
        for user_id in users_id:
            user = User.objects.get(id=user_id['user_id'])
            user.is_teacher = True
            user.save()
            response_if_agreed(user.email) # TOdo: change to mass email send to all users without iteration
    else:
        for user_id in users_id:
            user = User.objects.get(id=user_id['user_id'])
            user.is_teacher = False
            user.save()
            response_if_deleted(user.email)


@receiver(pre_delete, sender="teacher.TeacherInformation")
def deleted(sender, instance, **kwargs):
    user = instance.user
    user.is_teacher = False
    user.save()
    response_if_deleted(user.email)

