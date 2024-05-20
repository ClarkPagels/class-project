from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def update_user_role(sender, instance, **kwargs):
    email = instance.email
    user = instance
    admin_emails = ["cs3240.super@gmail.com", "cbf6ah@virginia.edu",
                    "hnf8bgt@virginia.edu", "sn6cn@virginia.edu",
                    "xac7gz@virginia.edu", "cjp3jf@virginia.edu"]

    if email in admin_emails:
        user.is_admin_user = True
        post_save.disconnect(update_user_role, sender=CustomUser)
        user.save()
        post_save.connect(update_user_role, sender=CustomUser)
