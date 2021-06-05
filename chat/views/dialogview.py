from django.contrib.auth import mixins
from django.contrib.auth.models import User
from django.http import QueryDict
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from ..models import Dialog, Message, Blacklist
from django.core import exceptions


class DialogListView(mixins.LoginRequiredMixin, generic.ListView):
    template_name = 'chat/dialog.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Dialog.objects.filter(users=self.request.user.id)

        #  TODO: is that possible to filter not empty dialogs using something built-in (without cycles here)
        messages = Message.objects.all()
        queryset_with_messages = []
        for dialog in queryset:
            for message in messages:
                if message.dialog == dialog:
                    blacklist = Blacklist.objects.get(owner=self.request.user)

                    dialog_with_block_info = {
                        'dialog': dialog,
                        'blocked': False
                    }

                    for blocked_user in blacklist.blocked_users.all():
                        if blocked_user in dialog.users.all():
                            dialog_with_block_info['blocked'] = True
                            break

                    queryset_with_messages.append(dialog_with_block_info)
                    break
        return queryset_with_messages


class DialogSearchDetailView(mixins.LoginRequiredMixin, generic.ListView):
    pass


#     model = Dialog
#
#     def get_object(self, queryset=None):
#         queryset = Dialog.objects.filter(users=self.request.user)
#         print(queryset)
#         return None


def dialog_search_or_create_view(request):
    print('dialog_search_view()')
    print('request.user:', request.user)
    print('other_users_id:', request.GET.get('other_users_id'))
    # print(request.GET.get('other_user').get('username'))
    # print(request.GET.get('other_user').get('username'))
    dialogs = Dialog.objects.filter(users=request.user)
    try:
        print('searching particular dialog...')
        dialog = dialogs.get(users__id=request.GET.get('other_users_id'))
    except exceptions.ObjectDoesNotExist:
        print('there is no such dialog yet')

        # query_dictionary = QueryDict('', mutable=True)
        # query_dictionary.update(
        #     {
        #         # 'username': request.user.username,
        #         'other_username': request.GET.get('other_user'),
        #     }
        # )
        # url = '{base_url}?{querystring}'.format(
        #     base_url=reverse(viewname='new_dialog_name'),
        #     querystring=query_dictionary.urlencode()
        # )
        print('creating such dialog')
        dialog = Dialog.objects.create()
        dialog.users.add(request.user)
        dialog.users.add(User.objects.get(id=request.GET.get('other_users_id')))
        print('after creation dialog')
        # return redirect(url)

        # return redirect(reverse(viewname='dialogs_name'))

    # print(dialogs)
    # print(dialog)
    # context = {'object_list': dialogs}
    # return render(request, 'chat/dialog.html', context)

    query_dictionary = QueryDict('', mutable=True)
    query_dictionary.update(
        {
            'dialog_id': dialog.id,
        }
    )
    url = '{base_url}?{querystring}'.format(
        base_url=reverse(viewname="messages_name"),
        querystring=query_dictionary.urlencode()
    )

    return redirect(url)


# class DialogSearchResultView(mixins.LoginRequiredMixin, generic.DetailView):
#     def get_object(self, queryset=None):
#         queryset = Dialog

class DialogCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    pass
    # model = Dialog
    # fields = '__all__'

    # def post(self, request, *args, **kwargs):
    #     print('post')
    #     print(request.POST.get('other_username'))
    #     # other_user = User.objects.get(username=request.POST.get('other_user'))
    #     print('create')
    #     print(request.user)
    #     # self.object = Dialog.objects.create(users=(request.user, other_user))
    #     return super().post(request, *args, **kwargs)
