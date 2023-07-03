from django import forms
from .models import *

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee_Details
#         fields = ['Emp_Id','Name','Email','First_Name','Last_Name','Father_Name','Mother_Name',
#                   'Dob','Blood_Group','Contact_Number','Emergency_Number','Present_Address','Permanent_Address','Qualification' ]
    

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee_Details
        fields = ['Emp_Id', 'Name', 'Email', 'First_Name', 'Last_Name','Father_Name', 'Mother_Name', 'Dob', 'Blood_Group', 'Contact_Number', 'Emergency_Number', 'Present_Address', 'Permanent_Address', 'Qualification']

        widgets = {
                        'Emp_Id'            : forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Emp-Id',            'style': 'margin-bottom: 10px background-color: #e6ffff;'}),
                        'Name'              : forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Name',              'style': 'margin-bottom: 10px'}),
                        'Email'             : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail',            'style': 'margin-bottom: 10px'}),
                        'First_Name'        : forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'First Name',        'style': 'margin-bottom: 10px'}),
                        'Last_Name'         : forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Last Name',         'style': 'margin-bottom: 10px'}),
                        'Father_Name'       : forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Father Name',       'style': 'margin-bottom: 10px'}),
                        'Mother_Name'       : forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Mother Name',       'style': 'margin-bottom: 10px'}),
                        'Dob'               : forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Date of Birth',     'style': 'margin-bottom: 10px'}),
                        'Blood_Group'       : forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Blood Group',       'style': 'margin-bottom: 10px'}),
                        'Contact_Number'    : forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Contact Number',    'style': 'margin-bottom: 10px'}),
                        'Emergency_Number'  : forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Emergency Number',  'style': 'margin-bottom: 10px'}),
                        'Present_Address'   : forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Present Address',   'style': 'margin-bottom: 10px'}),
                        'Permanent_Address' : forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Permanent Address', 'style': 'margin-bottom: 10px'}),
                        'Qualification'     : forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Qualification',     'style': 'margin-bottom: 10px'}),
        }

    def as_table(self):
        "Return this form rendered as HTML <tr>s -- excluding the <table></table>."
        return self._html_output(
            normal_row='''
                        <table>
                        <tr%(html_class_attr)s></tr>
                        <tr><b>%(label)s</b>
                        <td>%(errors)s%(field)s%(help_text)s</td><br></tr>
                        </tr>
                        </table>
                       ''',
            error_row='<tr><td colspan="2">%s</td></tr>',
            row_ender='</td></tr>',
            help_text_html='<br><span class="helptext">%s</span>',
            errors_on_separate_row=False,
        )
