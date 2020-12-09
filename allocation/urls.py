from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('allocation/',views.allocation,name='allocation'),
    path('changestatus/',views.changestatus,name='changestatus'),
    path('changestates/<int:id>/<int:status>/',views.changestates,name='changestates'),

    path('add/',views.add,name='add'),
    path('item/<int:id>',views.item_info,name='item_info'),

    path('request_item/',views.request_item,name='request_item'),
    path('reallocation/',views.reallocation,name='reallocation'),
    path('notification/',views.notification,name='notification'),
    path('accepted/<int:id>',views.accepted,name='accepted'),
    path('completed/<int:id>',views.completed,name='completed'),

    path('district_index/',views.district_index,name='district_index'),
    path('login/',views.Login.as_view(),name='login'),
    path('logout/',views.Logout.as_view(),name='logout'),
    path('district_info/<int:id>',views.district_info,name='district_info'),
    path('re/',views.re,name='re'),
    path('mnotification/',views.mnotification,name='mnotification'),

]
