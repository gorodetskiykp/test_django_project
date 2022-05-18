from django.shortcuts import render


def hello(request):
    template = 'test_app/index.html'
    result = 16
    context = {
        'template_var': result,
        'numbers': [1, 2, 3, 4],
    }
    return render(request, template, context)
