from django.shortcuts import render

# Home page
def home(request):
    return render(request, 'index.html')

# Category
def category_list(request):
    return render(request, 'category_list.html')