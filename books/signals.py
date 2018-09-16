from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from common.middleware import get_current_user
from .models import Book, LogBookAction


@receiver(post_save, sender=Book)
def log_create_edit(sender, instance, **kwargs):

    log_data_dict = {"user": get_current_user()}  # get user from request

    if kwargs['created']:
        # set values for book creation log
        for field in instance.fields_for_logging():
            log_data_dict[field] = getattr(instance, field)

        log_data_dict["action_type"] = LogBookAction.CREATE
    else:
        # set previous and current values for book updating log
        for field in instance.fields_for_logging():
            prev_field = 'prev_%s' % field
            log_data_dict[prev_field] = getattr(instance, prev_field)
            log_data_dict[field] = getattr(instance, field)

        log_data_dict["action_type"] = LogBookAction.UPDATE

    LogBookAction.objects.create(**log_data_dict)


@receiver(post_delete, sender=Book)
def log_delete(sender, instance, **kwargs):
    log_data_dict = {"user": get_current_user()}  # get user from request

    # set values for book deletion log
    for field in instance.fields_for_logging():
        prev_field = 'prev_%s' % field
        log_data_dict[prev_field] = getattr(instance, prev_field)

    log_data_dict["action_type"] = LogBookAction.DELETE

    LogBookAction.objects.create(**log_data_dict)
