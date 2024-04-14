from django.shortcuts import redirect, render, get_object_or_404
from .models import User
from .forms import UserForm
from  django.core.paginator import Paginator
#from django.contrib.auth.decorators import login_required




def users_list(request):
    list_users = User.objects.all()
    paginator = Paginator(list_users, 5)
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)
    
    return render(request, 'list_users.html', {'users': users})


def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    return render(request, 'detail_user.html', {'user': user})


def user_add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_users')    
    else:
        form = UserForm()
    
    return render(request, 'add_user.html', {'form': form})


def user_edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = UserForm(instance=user)
    
    return render(request, 'edit_user.html', {'form': form})


def user_delete(request, user_id):
    #user = get_object_or_404(User, pk=user_id)
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('list_users')
    #return render(request, 'delete_user.html', {'user': user})