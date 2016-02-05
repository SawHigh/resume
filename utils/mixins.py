from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .exceptions import ParamError

class ManagerApiMixin(object):
    def user_pass_test(self, request):
        if request.user.is_authenticated():
            return True
        return False
        
class CommonApiMixin(object):
    def user_pass_test(self, request):
        return True
    
class QueryFromUrlMixin(object):
    def query(self, request):
        try:
            pk = self.kwargs.get('pk')
            user = get_object_or_404(User,pk=pk)
            return {"user":user}
        except:
            raise ParamError("There should be a pk in url")
        
class OwnerPassMixin(object):
    def user_pass_test(self, request):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(self.model, pk=pk)
        if request.user.is_authenticated() and obj.user == request.user:
            return True
        return False
    
class UserIdMixin(object):
    def get_fields(self):  
        if not self.fields:
            fields = self.model._meta.get_all_field_names().copy()
            fields.remove("user")
            fields.append(["user", "id"])
        return self.fields
    
class CurrentUserMixin(object):
    def query(self, request, *args, **kwargs):
        return {"user":request.user}

class GetOwnerMixin(object):  
    def extend_data(self, request):
        return {"user":request.user}