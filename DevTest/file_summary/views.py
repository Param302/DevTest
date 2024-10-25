import pandas as pd
from django.shortcuts import render

# Create your views here.

def upload_file(request):
    if request.method == "GET":
        return render(request, 'upload_file.html')
    
    if not request.FILES:
        return render(request, 'upload_file.html', {"error": "Please upload excel file"})
    
    file = request.FILES['file']
    if not file.name.endswith('.xlsx'):
        return render(request, 'upload_file.html', {"error": "Please upload excel file"})
    
    data = pd.read_excel(file)
    return render(request, 'report.html', {"data": data.head()})
