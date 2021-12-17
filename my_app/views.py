from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TeamMember
from .forms import AddPageForm

def main (request):
    #displaying all the team members and the count
    form = TeamMember.objects.all()
    total_members = form.count()
    context = {'form':form,'total_members':total_members} 
    return render (request, 'my_app/index.html',context)


def addMemberForm (request):
    form = AddPageForm(initial={'role':' '})
    #the request must be POST request
    if request.method == "POST":
        form=AddPageForm(request.POST)
        #checking the validity of the form to save
        if form.is_valid():
            form.save()
            return redirect ('main')
    context = {'form': form}
    return render (request, 'my_app/addpage.html', context)

def editMemberForm (request, member_id):
    member = TeamMember.objects.get (pk=member_id)
    form = AddPageForm (instance = member)
    #the request must be POST request
    if request.method == "POST":
        form = AddPageForm(request.POST, instance = member)
        #checking the validity of the form to save
        if form.is_valid():
            form.save()
            return redirect ('main')

    context = {'form': form, 'member': member}
    return render (request, 'my_app/editpage.html', context)

def deleteMember (request, member_id):
    form = TeamMember.objects.get (pk=member_id)
    form.delete()
    return redirect ('main')


