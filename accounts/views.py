from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import AccountUser
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        internal_id = request.POST['internal_id']
        password = request.POST['password']

        account_user = AccountUser.objects.get(internal_id=internal_id)

        if account_user.verified:
            user = account_user.user
            print(user)
            user = authenticate(username=user.username, password=password)

            if user:
                login(request, user)
                return HttpResponseRedirect('/bookmarks/')
            else:
                return HttpResponse("You didn't get passed the final if statement")

        else:
          return HttpResponse("You didn't passed the second if statement")

    else:
        return render(request, 'accounts/login.html')
