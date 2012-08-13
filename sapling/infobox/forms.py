from django import forms
from eav.forms import BaseDynamicEntityForm


class InfoboxForm(BaseDynamicEntityForm):
    def __init__(self, data=None, *args, **kwargs):
        super(BaseDynamicEntityForm, self).__init__(data, *args, **kwargs)
        config_cls = self.instance._eav_config_cls
        self.entity = getattr(self.instance, config_cls.eav_attr)
        self._build_dynamic_fields()

    def save(self, commit=True):
        # we don't want to save the model instance, just the EAV attributes
        super(InfoboxForm, self).save(commit=False)
        self.entity.save()