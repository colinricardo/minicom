from django.shortcuts import render

from models import User

# Let's pretend we have logins, sessions and so on.
CURRENT_ADMIN_USER = 'eoghan@intercom.io'

def users(request):
  return render(request, 'users.html', {
    'admin': CURRENT_ADMIN_USER,
    'users': User.objects.all(),
  })
