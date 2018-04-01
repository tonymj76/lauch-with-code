from django.utils.deprecation import MiddlewareMixin
from joins_a.models import Join

# class ReferMiddleware(object):
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         return self.get_response(request)

#     def process_request(self, request):
#         print(request)



#      OR USE THIS BELOW this will work with other older versions of django


class ReferMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ref_id = request.GET.get("ref")
        try:
            obj = Join.objects.get(ref_address=ref_id)
        except:
            obj=None
        if obj:
            request.session['join_id_ref'] = obj.id_join