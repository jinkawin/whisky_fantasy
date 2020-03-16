from django.shortcuts import render


from django.contrib.auth.decorators import login_required
from app.forms import ChangepwdForm

@login_required
def changePwd(request):
    if request.method == 'GET':
        form = ChangepwdForm()
        return render(request, 'app/changepwd.html', {'form': form, })
    else:
        form = ChangepwdForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword')
            user = auth.authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                user.set_password(newpassword)
                user.save()
                return render(reverse('app:myaccount'))
            else:
                return render(request, 'app/changepwd.html', {'form': form, 'oldpassword_is_wrong': True})
        else:
            return render(request, 'app/changepwd.html', {'form': form, })
