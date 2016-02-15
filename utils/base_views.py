#_*_ coding:utf-8 _*_
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied, ValidationError
from django.middleware.csrf import rotate_token
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .exceptions import MethonNotDefineError, JsonParseError, ModelNeededError
from django.shortcuts import get_object_or_404

class WebApiView(View):
    
    def parse(self, request):
        try:
            return json.loads(request.body)
        except:
            raise JsonParseError
    
    def user_pass_test(self, request):
        """
        override this method and
        return True/False
        """
        raise MethonNotDefineError("Override the user_pass_test method first")
        
    def dispatch(self, request, *args, **kwargs):
        if not self.user_pass_test(request):
            raise PermissionDenied
#         if not request.is_ajax():
#             raise PermissionDenied
        rotate_token(request)
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
        
    def do_get(self, request, *args, **kwargs):
        """
        override this method 
        and return a dictionary
        """
        raise MethonNotDefineError("Override the do_get method first")
    
    def do_post(self, request):
        """
        override this method 
        and return a dictionary
        """
        raise MethonNotDefineError("Override the do_post method first")
    
    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps(self.do_get(request),ensure_ascii=False), content_type="application/json; charset=utf-8")
    
    def post(self, request, *args, **kwargs):      
        return HttpResponse(json.dumps(self.do_post(request),ensure_ascii=False), content_type="application/json; charset=utf-8")
    
    
class WebListApiView(WebApiView):
    """
    必须参数：
    paginate:是否分页，默认False
    page:每页显示条目数，默认0，即不分页返回全部
    model:查询模型，必须提供
    query_condition：查询条件，字典，不提供则不筛选返回全部
    method:GET
    fields:列表,列举查询的字段名,若查询外键传入列表，依次列举属性 不传入则返回所有字段值
    
    访问方法：get
    可选参数：
    page:数字，页码
    sort:字段名
    """
    paginate = False
    page = 0
    model = None
    query_condiction = {}
    fields = []
    file_fields = []
    
    def query(self, request, *args, **kwargs):
        return self.query_condiction
    
    def sort_list(self, request):
        if not self.model:
            raise ModelNeededError('Pass Me A Fucking Model')
        try:
            query_set = self.model.objects.filter(**self.query(request))
        except:
            raise ModelNeededError('query condition does not match model fields')       
        if 'sort' in request.GET and request.GET['sort']:
            return query_set.order_by("-s" % request.GET['sort'])
        else:
            return query_set
    
    def get_fields(self):  
        if not self.fields:
            return self.model._meta.get_all_field_names()
        return self.fields
            
    def construct_data(self, request):
        data = []
        for i in self.sort_list(request):
            dic = {}
            for j in self.get_fields():
        
                try:
                    if type(j) == list:
                        a = [i]
                        a.extend(j)
                        dic.update({j[0]:unicode(reduce(lambda x, y:getattr(x, y), a))}, encoding='utf-8')
                    else:
                        dic.update({j:unicode(getattr(i, j))}, encoding='utf-8')
                except:
                    raise ModelNeededError("Model %s May Have Not Field %s" % (self.model.__name__, j))
            data.append(dic)
        return data
                
    
    def the_page(self, request):
        if not self.paginate:
            return self.construct_data(request)
        else:
            if not self.page:
                return self.construct_data(request)       
            paginator = Paginator(self.construct_data(request), self.page)
            page = request.GET.get('page')
            try:
                items = paginator.page(page)
            except PageNotAnInteger:
                items = paginator.page(1)
            except EmptyPage:
                items = paginator.page(paginator.num_pages)
            return items
        
    def do_get(self, request, *args, **kwargs):
        return {'status':'success','data':self.the_page(request)}
            
class WebDetailApiView(SingleObjectMixin, WebApiView):
    """
    必须参数：

    model:查询模型，必须提供
    query_condition：查询条件，字典，不提供则不筛选返回全部

    fields:列表,列举查询的字段名,若查询外键传入列表，依次列举属性 不传入则返回所有字段值
    
    对应URL必须加上变量<pk>
    pk_url_kwarg:URL的pk变量名称
    访问方法：get
    
    model = None
    queryset = None
    slug_field = 'slug'
    context_object_name = None
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    query_pk_and_slug = False
    """
    fields = []
    
    def get_fields(self):  
        if not self.fields:
            return self.model._meta.get_all_field_names()
        return self.fields
    
    def do_get(self, request, *args, **kwargs):
        if not self.model:
            raise ModelNeededError('Pass Me A Fucking Model')
        obj = self.get_object()
        data = {}
        for i in self.get_fields():
            if type(i) == list:
                data.update({i[0]:reduce(lambda x, y:getattr(x, y), [obj].extend(i))})
            else:   
                data.update({i:getattr(obj, i)})
        return {'status':'success','data':data}
    
class WebCreateApiView(WebApiView):  
    """
    必须参数：

    model:查询模型，必须提供
    fields_names:列表,从客户端更新的字段名
    extend_dic:字典,创建对象需要的除fields_names外的键值对
    """
    model = None
    field_names = []
    extend_dic = {}
    
    def extend_data(self,request):
        return self.extend_dic
    
    def check_post(self,request):
        if sorted(self.parse(request).keys()) == sorted(self.field_names):
            return True
        return False
         
    def do_post(self, request):
        if not self.model:
            raise ModelNeededError('Pass Me A Fucking Model')
        if not self.check_post(request):
            return {"status":"fail", "reason":"invalid struture1"}
        try:
            dic = self.parse(request)
            dic.update(self.extend_data(request))
            if "encoding" in dic:
                del dic["encoding"]
            i = self.model.objects.create(**dic)
            i.save()
            return {"status":"success"}
        except:
            return {"status":"fail", "reason":"invalid struture2"}
        
class WebUpdateApiView(WebApiView):
    """
    必须参数：

    model:查询模型，必须提供
    
    对应URL必须加上变量<pk>
    pk_url_kwarg:URL的pk变量名称
    extend_dic:字典,修改对象需要的除fields_names外的自定义键值对
    访问方法：post
    """
    model = None
    pk_url_kwarg = 'pk'
    extend_dic = {}
    
    def do_post(self, request, *args, **kwargs):    
        if not self.model:
            raise ModelNeededError('Pass Me A Fucking Model')    
        try:
            dic = self.parse(request)
            dic.update(self.extend_dic)
            if "encoding" in dic:
                del dic["encoding"]
            pk = self.kwargs.get(self.pk_url_kwarg)
            query_set = self.model.objects.filter(pk=pk)
            query_set.update(**dic)
            return {"status":"success"}
        except:
            return {"status":"fail", "reason":"invalid struture2"}
        
class WebDeleteApiView(WebApiView):
    """
    必须参数：

    model:查询模型，必须提供
    
    对应URL必须加上变量<pk>
    pk_url_kwarg:URL的pk变量名称
    访问方法：post
    """
    model = None
    pk_url_kwarg = 'pk'
    
    def do_post(self, request, *args, **kwargs):    
        if not self.model:
            raise ModelNeededError('Pass Me A Fucking Model')    
        try:
            pk = self.kwargs.get(self.pk_url_kwarg)
            obj = get_object_or_404(self.model, pk=pk)
            obj.delete()
            return {"status":"success"}
        except:
            return {"status":"server error"}