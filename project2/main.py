import random


def usual_login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        OneTimeCode.objects.create(code=random.choice('adcde'), user=user)
        # send one-time code to email
        # redirect somewhere
    else:
        # Return an 'invalid login' error message

def login_with_code_view(request):
    username = request.POST['username']
    if OneTimeCode.objects.filter(code=code, user__username=username).exists():
        login(request, user)
    else:
        # error