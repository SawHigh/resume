#_*_ coding:utf-8 _*_
from .base_views import WebListApiView, WebCreateApiView, WebUpdateApiView, WebDeleteApiView

from .mixins import UserIdMixin, CurrentUserMixin, ManagerApiMixin, GetOwnerMixin, OwnerPassMixin, \
CommonApiMixin, QueryFromUrlMixin


class ManagerListView(UserIdMixin, CurrentUserMixin, ManagerApiMixin, WebListApiView):
    pass

class ManagerCreatView(GetOwnerMixin, ManagerApiMixin, WebCreateApiView):
    pass

class ManagerUpdateView(OwnerPassMixin,WebUpdateApiView):
    pass

class ManagerDeleteView(OwnerPassMixin,WebDeleteApiView):
    pass

class CommonListView(CommonApiMixin, QueryFromUrlMixin, WebListApiView):
    pass