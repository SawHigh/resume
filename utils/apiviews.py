#_*_ coding:utf-8 _*_
from .base_views import WebListApiView, WebCreateApiView, WebUpdateApiView, WebDeleteApiView

from .mixins import CurrentUserMixin, ManagerApiMixin, GetOwnerMixin, OwnerPassMixin, \
CommonApiMixin, QueryFromUrlMixin

class CommonListView(CommonApiMixin, QueryFromUrlMixin, WebListApiView):
    pass

class ManagerListView(
#                      UserIdMixin, 
                      CurrentUserMixin, 
                      ManagerApiMixin, 
                      WebListApiView):
    pass

class ManagerCreatView(GetOwnerMixin, ManagerApiMixin, WebCreateApiView):
    pass

class ManagerUpdateView(OwnerPassMixin,WebUpdateApiView):
    pass

class ManagerDeleteView(OwnerPassMixin,WebDeleteApiView):
    pass

class MustLoginListView(ManagerApiMixin, WebListApiView):
    pass

class MustLoginCreateView(ManagerApiMixin, WebCreateApiView):
    pass

class MustLoginUpdateView(ManagerApiMixin, WebUpdateApiView):
    pass

class MustLoginDeleteView(ManagerApiMixin, WebDeleteApiView):
    pass
