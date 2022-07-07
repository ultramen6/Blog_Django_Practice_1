from django.shortcuts import render


def posts_list(request):
    n = ['a','b','c','d']
    return render(request, 'blog/index.html', context={'names': n}) 
 