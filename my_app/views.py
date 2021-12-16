from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import TeamMember
# Create your views here.
def main (request):
    #displaying all the team members
    members = TeamMember.objects.all()
    members.length = len (members) 
    return render (request, 'my_app/index.html', {'members': members})

def specific (request):
    return HttpResponse ("Specific url")

def addMemberForm (request):
    return render (request, 'my_app/addpage.html')

def addMember (request):
    if request.method == "POST": #the request must be POST request
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        admin = '(admin)'
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        role = request.POST.get('role')
        member = TeamMember()
        member.firstname = firstname
        member.lastname = lastname
        member.email = email
        member.phonenumber = phonenumber
        if role == "1":
            member.role = admin
        else:
            member.role = ''
        #adding member into database
        member.save()
        return redirect ('main')
    #in case the request isn't a POST request
    return redirect ('main')

def editMemberForm (request, member_id):
    member = TeamMember.objects.get (pk=member_id)
    return render (request, 'my_app/editpage.html', {'member': member})

def editMember (request):
    if request.method == "POST": #the request must be POST request
        admin = '(admin)'
        id = request.POST.get('id')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        role = request.POST.get('role')
        #get the old member info
        member = TeamMember.objects.get(pk=id)
        #update the member info
        member.firstname = firstname
        member.lastname = lastname
        member.email = email
        member.phonenumber = phonenumber
        if role == "1":
            member.role = admin
        else:
            member.role = ''
        #update the member info in database
        member.save()
        return redirect ('main')
    #in case the request isn't a POST request
    return redirect ('main')

def deleteMember (request, member_id):
    member = TeamMember.objects.get (pk=member_id)
    member.delete()
    return redirect ('main')


