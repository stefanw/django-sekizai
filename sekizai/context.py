from django import VERSION
from django.template import Context
from sekizai.context_processors import sekizai

if VERSION[0] == 1 and VERSION[1] < 11:
    BaseClass = Context
else:
    BaseClass = dict


class SekizaiContext(BaseClass):
    """
    An alternative context to be used instead of RequestContext in places where
    no request is available.
    """
    def __init__(self, *args, **kwargs):
        super(SekizaiContext, self).__init__(*args, **kwargs)
        self.update(sekizai())
