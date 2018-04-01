from django.conf.urls import url
from .views import join_reg, join_detail_view, RefFriendList

app_name = "joins_a"

urlpatterns = [
    url(r'^$', join_reg, name='create_form'),
    url(r'^\?ref=(?P<ref_address>[-\w]+)$', join_detail_view, name="detail_view"),
    url(r'^list_ref', RefFriendList.as_view(), name='ref_list' ),
    # url(r'^(?P<slug>[-\w]+)/ref=(?P<ref_address>[-\w?]*)?$', join_detail_view, name="detail_view")
]
