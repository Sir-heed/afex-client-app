from cgitb import lookup
from http import client
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from apps.crm.utils import get_random_string

from .models import Client, ClientWallet
from .forms import ClientForm, FundWalletForm
 
 
def create_view(request):
    context = {}
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form_inst = form.save(commit=False)
        random_code = get_random_string(6)
        while Client.objects.filter(cid=random_code).exists():
            random_code = get_random_string(6)
        if request.user.is_authenticated:
            form_inst.created_by = request.user
        form_inst.cid = random_code
        form_inst.save()
        ClientWallet.objects.create(client=form_inst)
        return redirect("crm:client-list")
    context['form']= form
    return render(request, "crm/create_client.html", context)


def update_view(request, cid):
    context ={}
    obj = get_object_or_404(Client, cid = cid)
    form = ClientForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("crm:client-list")
    context["form"] = form
    return render(request, "crm/edit_client.html", context)


class IndexView(generic.ListView):
    template_name = 'crm/client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        """Return the last five published questions."""
        return Client.objects.all()


def detail_view(request, cid):
    try:
        client = Client.objects.get(cid=cid)
    except Client.DoesNotExist:
        raise Http404('Client does not exist')
    return render(request, 'crm/client_detail.html', context={'client': client})


def delete_view(request, cid):
    try:
        client = Client.objects.get(cid=cid)
    except Client.DoesNotExist:
        raise Http404('Client does not exist')
    client.delete()
    return redirect("crm:client-list")


def fund_wallet(request, cid):
    context = {}
    try:
        client = Client.objects.get(cid=cid)
    except Client.DoesNotExist:
        raise Http404('Client does not exist')
    form = FundWalletForm(request.POST or None)
    if form.is_valid():
        print('HERe')
        amount = form.cleaned_data['amount']
        client_wallet = client.clientwallet
        client_wallet.total_balance += amount
        client_wallet.available_balance += amount
        client_wallet.save()
        return HttpResponseRedirect(reverse('crm:client-detail', args=(client.cid,)))
    context['form']= form
    return render(request, "crm/fund_wallet.html", context)