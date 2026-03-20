from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Job, Application

# Create your views here.
def home(request):
    query = request.GET.get('q')

    if query:
        jobs = Job.objects.filter(title__icontains=query)
    else:
        jobs=Job.objects.all()
    return render(request, 'home.html', {'jobs':jobs})

def apply_job(request, id):
    job = Job.objects.get(id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        resume = request.FILES.get('resume')

        Application.objects.create(
            job=job,
            name=name,
            email=email,
            resume=resume
        )

        return redirect('home')

    return render(request, 'apply.html', {'job': job})

def view_applications(request, id):
    job = Job.objects.get(id=id)
    applications = Application.objects.filter(job=job)
    return render(request, 'applications.html', {
        'job': job,
        'applications': applications
    })        
