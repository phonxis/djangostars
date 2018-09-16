from django.db import models


class BaseDates(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    modified_dt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SavedRequest(models.Model):
    created_dt = models.DateTimeField(
        "Created",
        auto_now_add=True
    )
    request_method = models.CharField(
        "Request method",
        max_length=16,
        blank=True
    )
    http_host = models.CharField(
        "HTTP host",
        max_length=16,
        blank=True
    )
    http_user_agent = models.TextField(
        "HTTP user agent",
        blank=True
    )
    server_protocol = models.CharField(
        "Server protocol",
        max_length=32,
        blank=True
    )
    tz = models.CharField(
        "Timezone",
        max_length=32,
        blank=True
    )
    path_info = models.CharField(
        "Path info",
        max_length=64,
        blank=True
    )
    user = models.CharField(
        "User",
        max_length=150,
        default="Anonymous"
    )

    class Meta:
        verbose_name = "Saved request"
        verbose_name_plural = "Saved requests"
        ordering = ('-created_dt',)

    def __str__(self):
        return "%s %s %s" % (self.user, self.path_info, self.request_method)
