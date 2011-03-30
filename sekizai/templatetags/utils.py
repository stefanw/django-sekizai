from classytags.arguments import MultiValueArgument
from classytags.values import StringValue
from django_load.core import load_object

def noop(value):
    return value

class LoadValue(StringValue):
    errors = {
        "invalid": "%(value)s is not a valid import path, should be of format "
                   "'mypackage.mymodule.mycallable'",
        "import": "Could not import %(value)s",
    }
    value_on_error = staticmethod(noop)
    
    def clean(self, value):
        try:
            return load_object(value)
        except TypeError:
            return self.error(value, "invalid")
        except (ImportError, AttributeError):
            return self.error(value, "import")
        

class LoadArgument(MultiValueArgument):
    value_class = LoadValue