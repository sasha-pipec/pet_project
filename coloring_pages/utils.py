from .models import *


class DataMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['cats']=Category.objects.all()
        return context