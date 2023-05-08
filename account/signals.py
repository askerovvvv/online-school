from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import MassEmails


@receiver(post_save, sender=MassEmails)
def clear_mass_email_db(sender, instance, created, **kwargs):
    try:
        data = MassEmails.objects.get(id=instance.id - 1).delete()
        print(data)
    except:
        pass


