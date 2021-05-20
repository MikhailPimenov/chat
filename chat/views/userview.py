from django.contrib.auth import mixins
from django.contrib.auth.models import User
from django.views import generic
from django.core import exceptions

from ..forms.usersearchform import UserSearchForm
from ..models import Message
from ..forms import MessageModelForm


class UserSearchFormView(mixins.LoginRequiredMixin, generic.FormView):
    template_name = 'chat/users_search.html'
    form_class = UserSearchForm


class UserSearchResultView(mixins.LoginRequiredMixin, generic.DetailView):
    template_name = 'chat/users_search_results.html'
    model = User

    def get_object(self, queryset=None):
        try:
            user = User.objects.get(username=self.request.GET.get('username'))
        except exceptions.ObjectDoesNotExist:
            user = None
        return user


    # def get_context_data(self, **kwargs):

