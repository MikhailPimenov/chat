from django.contrib.auth import mixins
from django.contrib.auth.models import User
from django.core import exceptions
from django.http import QueryDict
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic

from ..models import Blacklist, Dialog, Message


class DialogListView(mixins.LoginRequiredMixin, generic.ListView):
    template_name = "chat/dialog.html"

    def get_queryset(self, *args, **kwargs):
        queryset = Dialog.objects.filter(users=self.request.user.id)

        #  TODO: is that possible to filter not empty dialogs using something built-in (without cycles here)
        messages = Message.objects.all()
        queryset_with_messages = []
        for dialog in queryset:
            for message in messages:
                if message.dialog == dialog:
                    blacklist = Blacklist.objects.get(owner=self.request.user)

                    dialog_with_block_info = {"dialog": dialog, "blocked": False}

                    for blocked_user in blacklist.blocked_users.all():
                        if blocked_user in dialog.users.all():
                            dialog_with_block_info["blocked"] = True
                            break

                    queryset_with_messages.append(dialog_with_block_info)
                    break
        return queryset_with_messages


def dialog_search_or_create_view(request):
    dialogs = Dialog.objects.filter(users=request.user)
    try:
        dialog = dialogs.get(users__id=request.GET.get("other_users_id"))
    except exceptions.ObjectDoesNotExist:
        dialog = Dialog.objects.create()
        dialog.users.add(request.user)
        dialog.users.add(User.objects.get(id=request.GET.get("other_users_id")))

    query_dictionary = QueryDict("", mutable=True)
    query_dictionary.update(
        {
            "dialog_id": dialog.id,
        }
    )
    url = "{base_url}?{querystring}".format(
        base_url=reverse(viewname="messages_name"),
        querystring=query_dictionary.urlencode(),
    )

    return redirect(url)
