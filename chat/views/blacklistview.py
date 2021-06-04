from django.contrib.auth import mixins
from django.contrib.auth.models import User
from django.http import QueryDict
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from ..models import Dialog, Message, Blacklist
from django.core import exceptions


class BlacklistCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = Blacklist
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        print('BlacklistCreateView.post():')
        return super().post(request, *args, **kwargs)

    def get_redirect_field_name(self):
        return redirect(reverse(viewname='index_name'))


class BlacklistDetailView(mixins.LoginRequiredMixin, generic.DetailView):
    template_name = 'chat/blacklist.html'

    def get_object(self, queryset=None):
        return Blacklist.objects.get(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = {
            'object_list': self.get_object().blocked_users.all(),
        }
        return context


class BlacklistUpdateView(mixins.LoginRequiredMixin, generic.UpdateView):
    pass
    # def get_object(self, queryset=None):
    #     return Blacklist.objects.get(owner=self.request.user)
    #
    # def post(self, request, *args, **kwargs):
    #     blacklist = self.get_object()
    #     user = User.objects.get(username=request.POST.get('username', None))
    #
    #     if request.POST.get('add', None):
    #         blacklist.blocked_users.add(user)
    #         return super().post(request, *args, **kwargs)
    #
    #     blacklist.blocked_users.delete(user)
    #     return super().post(request, *args, **kwargs)


def update_blacklist(request):
    blacklist = Blacklist.objects.get(owner=request.user)
    user = User.objects.get(username=request.GET.get('username', None))

    if bool(request.GET.get('add', None)):
        blacklist.blocked_users.add(user)
        return redirect(reverse(viewname="blacklist_name"))

    blacklist.blocked_users.remove(user)
    return redirect(reverse(viewname="blacklist_name"))
