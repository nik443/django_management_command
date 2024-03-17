from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=255, verbose_name="name_of_poll")
    opened = models.BooleanField(verbose_name="opened", default=False)