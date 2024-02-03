from django import views
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

class LoginView(TemplateView):
    template_name = 'login.html'

class StudentView(TemplateView):
    template_name = 'studenthome.html'

#def login_view(request):
#    return render(request, 'login.html')

class FacultyView(TemplateView):
    template_name = 'facultyhome.html'

class AdminView(TemplateView):
    template_name = 'adminlogin.html'

class AdminHome(TemplateView):
    template_name = 'adminhome.html'

class DarkTheme(TemplateView):
    template_name = 'layout-static.html'

class LightTheme(TemplateView):
    template_name = 'layout-sidenav-light.html'

class FacultyResources(TemplateView):
    template_name = 'facultyresource.html'

from .models import Resource
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import ResourceUploadForm
@login_required
def upload_resource(request):
    if request.method == 'POST':
        # Check if the form is valid and the file has been uploaded
        form = ResourceUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the form data
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            resource_file = form.cleaned_data['resource_file']
            
            # Create a new Resource object and save it to the database
            resource = Resource(title=title, description=description, faculty=request.user, resource_file=resource_file)
            resource.save()
            
            return JsonResponse({'message': 'Resource uploaded successfully'})
        else:
            # Return an error response if the form is invalid
            return JsonResponse({'error': 'Resource upload failed. Please check the form data.'}, status=400)
    else:
        # Return an error response for GET requests
        return JsonResponse({'error': 'Invalid request method'}, status=400)

