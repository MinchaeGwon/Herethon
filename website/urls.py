from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import herby.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', herby.views.main , name='main'),
    path('search/', herby.views.search, name='search'),
    path('signup/', herby.views.signup, name='signup'),
    path('signin/', herby.views.signin, name='signin'),
    path('logout/', herby.views.logout, name='logout'),
    path('herby/<int:post_id>', herby.views.detail, name="detail"),
    path('openclass/', herby.views.new, name='new'),
    path('/create/', herby.views.create, name='create'),
    path('delete/<int:post_id>', herby.views.delete, name="delete"),
    path('', herby.views.start, name='start'),
    path('herby/<int:post_id>/comments/', herby.views.add_comment, name = 'add_comment'),
    path('searchresult/<str:myuni>/', herby.views.unifilter, name="unifilter"),    
]


