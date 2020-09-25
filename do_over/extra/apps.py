from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExtraConfig(AppConfig):
    name = 'do_over.extra'
    verbose_name = _("Extra")
