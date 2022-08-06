from django.shortcuts import render

# Create your views here.
'''
def show(request):
    return render(request , 'user/user.html' )


'''
from users.forms import courses

def course(request):
  form = courses()
  print(request.GET)
  return render(request,
          'user/user.html',
          {'form': form})