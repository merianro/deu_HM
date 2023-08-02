from django.urls import path
#from .views import AddressView
from .views import AddNoteView
from . import views
from users.views import profile, edit_user


urlpatterns = [
    #path('home', AddressView.as_view(), name='home'),
    path('home/', views.addNote, name='home'),
    path('notes/', AddNoteView.as_view(), name='notes'),
    path('new_address/', views.create, name='create'),
    path('get_ubicaciones/', views.get_ubicaciones, name='get_ubicaciones'),
    path('addresses/', views.get_ubics, name='get_ubics'),
    path('new_ent/', views.addEnt, name='createEnt'),
    path('notes/<int:note_id>', views.detail_page, name='detail'),
    path('profile/', profile, name='profile'),
    path('editar/', edit_user, name='edit_user'),
]