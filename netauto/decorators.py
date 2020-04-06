from django.shortcuts import redirect, render

def superadmin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == "superadmin":
            return view_func(request, *args, **kwargs)
        else:    
            return render(request, 'netauto/403.html')
    return wrapper_function
