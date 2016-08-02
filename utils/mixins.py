# _*_ coding:utf-8 _*_
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .exceptions import ParamError, ModelNeededError, FormNeededError
from PIL import Image

class ManagerApiMixin(object):
    """
    login required.
    """
    def user_pass_test(self, request):
        if request.user.is_authenticated():
            return True
        return False
        
class CommonApiMixin(object):
    """
    login not required.
    """
    def user_pass_test(self, request):
        return True
    
class QueryFromUrlMixin(object):
    """
    get user form pk argument in url.
    """
    def query(self, request):
        try:
            pk = self.kwargs.get('pk')
            user = get_object_or_404(User,pk=pk)
            return {"user":user}
        except:
            raise ParamError("There should be a pk in url")
        
class OwnerPassMixin(object):
    """
    one can only modify the object he owns. 
    """
    def user_pass_test(self, request):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(self.model, pk=pk)
        if request.user.is_authenticated() and obj.user == request.user:
            return True
        return False
    
class CurrentUserMixin(object):
    """
    append current user to query conditions.
    """
    def query(self, request):
        self.query_condiction.update({"user":request.user})
        return self.query_condiction

class GetOwnerMixin(object):  
    """
    set current user as the owner of current  object(field name: 'user').
    """
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
        
class ImageResizeMixin(FileUploadMixin):
    image_field = None
    max_width = 0
    max_height = 0
    
    def get_image_field(self):
        if not self.image_field:
            raise FormNeededError('ImageField UnDefined')
        return self.image_field
    
    def get_factor(self, width, height):
        if self.max_width and ( width > self.max_width ):
            width_factor = float(self.max_width) / width
        else:
            width_factor = 1
        if self.max_height and ( height > self.max_height ): 
            height_factor = float(self.max_height) / height
        else:
            height_factor = 1
        return min([width_factor, height_factor])
            
    
    def do_post(self, request, *args, **kwargs):               
        try:
            form = self.get_form(request)
            if form.is_valid():
                i = form.save()   
                if getattr(i, self.get_image_field()):
                    image = Image.open(getattr(i, self.get_image_field()))
                    (width, height) = image.size   
                    if width > self.max_width or height > self.max_height:
                        factor = self.get_factor(width, height)
                        size = (int(width * factor), int(height * factor))
                        image = image.resize(size, Image.ANTIALIAS)
                        image.save(getattr(i, self.get_image_field()).path)           
                return {"status":"success"}
            else:
                return {"status":"fail", "reason":"form invalid"}
        except:# from .mixins import *
            return {"status":"fail", "reason":"who the hell knows"}
                       
