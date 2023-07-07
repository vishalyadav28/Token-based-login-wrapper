from functools import wraps
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status

def login_required_viewset(view_func):
    """
    Decorator to enforce login_required for each view function within a ViewSet.
    If the user is not authenticated, returns an HTTP 405 Method Not Allowed response.
    """
    @wraps(view_func)
    def wrapper(viewset, request, *args, **kwargs):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # Return HTTP 405 Method Not Allowed response
            return viewset.http_method_not_allowed(request)
        # Execute the view function
        return view_func(viewset, request, *args, **kwargs)
    return wrapper

# To use this decorator, 
# you can apply it to each view function within your viewsets.ViewSet subclass:
# in views
class MyViewSet(viewsets.ViewSet):
    @login_required_viewset
    def list(self, request):
        """
        API endpoint to retrieve a list of resources.
        Requires the user to be authenticated.
        """
        # Your list view function logic here
        ...

    @login_required_viewset
    def create(self, request):
        """
        API endpoint to create a new resource.
        Requires the user to be authenticated.
        """
        # Your create view function logic here
        ...

    @login_required_viewset
    def retrieve(self, request, pk=None):
        """
        API endpoint to retrieve a specific resource.
        Requires the user to be authenticated.
        """
        # Your retrieve view function logic here
        ...

    @login_required_viewset
    def update(self, request, pk=None):
        """
        API endpoint to update a specific resource.
        Requires the user to be authenticated.
        """
        # Your update view function logic here
        ...

    @login_required_viewset
    def partial_update(self, request, pk=None):
        """
        API endpoint to perform a partial update on a specific resource.
        Requires the user to be authenticated.
        """
        # Your partial update view function logic here
        ...

    @login_required_viewset
    def destroy(self, request, pk=None):
        """
        API endpoint to delete a specific resource.
        Requires the user to be authenticated.
        """
        # Your destroy view function logic hereUsing the login_required_viewset decorator on each view function within your viewsets.
# ViewSet ensures that the user must be authenticated to access those endpoints. 
# If the user is not authenticated, 
Using the login_required_viewset decorator on each view function within your viewsets.
# ViewSet ensures that the user must be authenticated to access those endpoints. 
# If the user is not authenticated, 
# an HTTP 405 Method Not Allowed response will be returned,
# indicating that the requested method is not allowed for the resource.# an HTTP 405 Method Not Allowed response will be returned,
# indicating that the requested method is not allowed for the resource.
        # ...
# Using the login_required_viewset decorator on each view function within your viewsets.
# ViewSet ensures that the user must be authenticated to access those endpoints. 
# If the user is not authenticated, 
# an HTTP 405 Method Not Allowed response will be returned,
# indicating that the requested method is not allowed for the resource.
