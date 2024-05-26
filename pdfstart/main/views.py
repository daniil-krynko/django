from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets
from django.views.generic import CreateView, UpdateView, ListView
from .models import Accounts, Files
from .forms import AccountsForm, FilesForm
from .serializers import FileSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from .serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class AccountsCreateView(CreateView):
    model = Accounts
    fields = '__all__'

class AccountsUpdateView(UpdateView):
    model = Accounts
    form_class = AccountsForm
    template_name = 'main/account_update_form.html'

class AccountsListView(ListView):
    model = Accounts
    context_object_name = 'accounts'



class FilesCreateView(CreateView):
    model = Files
    fields = '__all__'

class FilesUpdateView(UpdateView):
    model = Files
    form_class = FilesForm
    template_name = 'main/files_update_form.html'

class FilesListView(ListView):
    model = Files
    context_object_name = 'files'
def index(request):
    return HttpResponse("Test")
def base(request):
    return render(request, 'main/accounts_form.html')

def get_file_by_id(request, file_id):
    if request.method == 'GET':
        file = get_object_or_404(Files, id=file_id)
        return render(request, 'main/files_id.html', {'file': file})
    else:
        return HttpResponse(status=405)

def get_account_files(request, account_id):
    if request.method == 'GET':
        account = get_object_or_404(Accounts, id=account_id)
        account_files = Files.objects.filter(author_file=account)
        serializer = FileSerializer(account_files, many=True)
        return render(request, 'main/account_files_id.html', {'files': account_files})
    else:
        return HttpResponse(status=405)

@login_required
def secure_page(request):
    return render(request, 'main/secure_page.html')
# Create your views here.
