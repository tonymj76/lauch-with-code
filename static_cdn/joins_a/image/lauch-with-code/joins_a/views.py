from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.http.response import Http404
from .models import Join
from .forms import JoinForm
import uuid

# from extra_views.generic import GenericInlineFormSet
# from extra_views import CreateWithInlinesView, InlineFormSet
    


# Create your views here.


def get_ref_addr():
    ref = str(uuid.uuid4())[:11].upper()
    return ref

def get_ip(request):
    """ function to get the ip address of the user """
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip

def join_reg(request):
    try: 
        join_id = request.session['join_id_ref']
        obj = Join.objects.get(id_join=join_id)
    except:
        obj = None
    form = JoinForm()
    if request.method == 'POST':
        join_data = JoinForm(request.POST or None)
        if join_data.is_valid():
            _ = join_data.save(commit=False)
            email = join_data.cleaned_data['email_address']
            first_name = join_data.cleaned_data['first_name']
            new_join, created = Join.objects.get_or_create(email_address=email)
            if created:
                if not obj == None:
                    new_join.friend = obj
                new_join.first_name = first_name
                new_join.ip_address = get_ip(request)
                new_join.ref_address = get_ref_addr()
                new_join.save()
                messages.success(request, "Sucessfully Created new email", extra_tags='somet')
            else:
                messages.info(request, f"Welcome: {first_name}")
            # print(Join.objects.filter(friend=obj).count())
            # print(obj.referral.all().count())
            # print(obj.referral.get(first_name='mr steal'))
            return redirect("joins_a:detail_view", new_join.ref_address)
            # return redirect("joins_a:detail_view", new_join.slug, new_join.ref_address)
        else:
            messages.error(request, "check to see if the email is well enter")

    return render(request, "joins_a/join_form.html", {"form": form})

# class UserFormCreateView(InlineFormSet):
#     model = User
#     form_class = UserForm

class RefFriendList(ListView):
    model = Join
    def get_queryset(self):
        return Join.ref_friend.all()

def join_detail_view(request,ref_address):
    join_obj = get_object_or_404(Join, ref_address=ref_address)
    share_url = settings.SHARE_URL + str(join_obj.ref_address)
    friends_referred = Join.objects.filter(friend=join_obj)
    count = join_obj.referral.all().count()
    return render(request, "joins_a/join_details.html", 
                                            {'join': join_obj, "share_url": share_url,
                                            "friends_referred": friends_referred, "count": count,
                                            
                                            }
                                         )


    
# class JoinFromCreateView(CreateView):
#     model = Join
#     form_class = JoinForm
#     # slug_field = 'anthony'
#     # slug_url_kwarg = 'anthony'
    

#     def get_ip(self, request):
#         """ function to get the ip address of the user """
#         try:
#             x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
#             if x_forward:
#                 ip = x_forward.split(",")[0]
#             else:
#                 ip = request.META.get("REMOTE_ADDR")
#         except:
#             ip = ""
#         return ip
        

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         email = self.object.email_address
#         new_email = Join.objects.filter(email_address=email)
#         if new_email.exists():
#             my_object = get_object_or_404(Join, slug='anthony')
#             self.object.slug = my_object
#             # return reverse("joins_a:somewhere", self.slug_url_kwarg)
#             return self.object.get_absolute_url(self.slug_field)
#         else:
#             self.object.ip_address = self.get_ip(self.request)
#             self.object.ref_address = get_ref_addr()
#             self.object.save()
#             return super(JoinFromCreateView, self).form_valid(form)
            
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(slug=self.kwargs.get('slug'))


