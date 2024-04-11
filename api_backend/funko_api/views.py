from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'heading': 'Bienvenido al home!',
        'content': 'Contenido del home',
    }
    return render(request, 'index.html', context)
def about(request):
    # Logic of your view
    return render(request, 'about.html')  # Render the new_template.html template