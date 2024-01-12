from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from NewsPortal.models import PostCategory
from NewsPortal.tasks import send_email_task


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(instance, **kwargs):
    if kwargs['action'] == 'post_add':
        send_email_task.delay(instance.pk)
