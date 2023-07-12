from django.contrib.auth.decorators import login_required
from app.models import Hocsinh

def get_User_name(request):
    name = None
    if request.user.is_authenticated:
        try:
            user = Hocsinh.objects.get(mahs=request.user)
            name = user.tengv.strip()
        except Hocsinh.DoesNotExist:
            pass

    return {'User_name': name}
