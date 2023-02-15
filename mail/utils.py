from django.forms import ModelMultipleChoiceField


class UserModelMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
         return str(obj.email)