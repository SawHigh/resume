from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .exceptions import ParamError, ModelNeededError, FormNeededError

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
    
class CurrentUserMixin(object):
    def query(self, request, *args, **kwargs):
        self.query_condiction.update({"user":request.user})
        return self.query_condiction

class GetOwnerMixin(object):  
    def extend_data(self, request):
        return {"user":request.user}
    
class FileUploadMixin(object):
    form = None
    
    def get_obj(self):
        if not self.model:
            raise ModelNeededError('Pass Me A Fucking Model')
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(self.model, pk=pk)
        return obj
    
    def get_form(self, request):
        if not self.form:
            raise FormNeededError('Pass Me A Fucking Form')
        return self.form(request.POST, request.FILES, instance=self.get_obj())
               
    def do_post(self, request, *args, **kwargs):               
        try:
            form = self.get_form(request)
            if form.is_valid():
                form.save()              
                return {"status":"success"}
            else:
                return {"status":"fail", "reason":"form invalid"}
        except:# from .mixins import *
            return {"status":"fail", "reason":"who the hell knows"}