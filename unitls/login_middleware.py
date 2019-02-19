from config.config import exclude_path
from django.utils.deprecation import MiddlewareMixin



class UrlRecordMiddleware(MiddlewareMixin):

    def process_view(self,request,func,*args,**kwargs):
        if request.path.endswith('.html') and request.path not in exclude_path:
            request.session['pre_path'] = request.get_full_path()