from django.urls import path
from . import views 

urlpatterns = [
    path('', views.main, name='main'),
    path ('addMemberForm', views.addMemberForm, name='addForm'),
    path ('editMemberForm/<int:member_id>', views.editMemberForm, name='editMemberForm'),
    path ('deleteMember/<int:member_id>', views.deleteMember, name='deleteMember')

]