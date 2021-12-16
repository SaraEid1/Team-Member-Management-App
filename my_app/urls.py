from django.urls import path
from . import views 

urlpatterns = [
    path('', views.main, name='main'),
    path ('specific', views.specific, name='specific'),
    path ('addMemberForm', views.addMemberForm, name='addForm'),
    path ('addMember', views.addMember, name='addMember'),
    path ('editMemberForm/<int:member_id>', views.editMemberForm, name='editMemberForm'),
    path ('editMember', views.editMember, name='editMember'),
    path ('deleteMember/<int:member_id>', views.deleteMember, name='deleteMember')


]