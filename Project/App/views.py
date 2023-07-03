# from django.shortcuts import render, redirect
# from .forms import EmployeeForm

# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .forms import EmployeeForm

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         if email == 'kiran@gmail.com' and password == '1234567890':
#             # Perform any additional actions if needed
#             return redirect('employee_details')  # Redirect to employee_details view
#         else:
#             # Handle invalid login credentials
#             error_message = 'Invalid email or password'
#             return render(request, 'login.html', {'error_message': error_message})

#     return render(request, 'login.html')


# def employee_details(request):
#     if request.session.get('logged_in'):  # Check if user is logged in
#         if request.method == 'POST':
#             form = EmployeeForm(request.POST)
#             if form.is_valid():
#                 form.save()  # Save the form data to the database
#                 return redirect('success')  # Redirect to a success page
#         else:
#             form = EmployeeForm()

#         return render(request, 'employee_form.html', {'form': form})
#     else:
#         return redirect('login')  # Redirect to login page if not logged in

# def success(request):
#     return render(request, 'success.html')



# views.py

from django.shortcuts import render, redirect
from .forms import EmployeeForm


def employee_details(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = EmployeeForm()

    return render(request, 'employee_form.html', {'form': form})

    

from django.shortcuts import render

def success(request):
    return render(request, 'success.html')
