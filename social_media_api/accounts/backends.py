from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()
class EmailBackend(BaseBackend):
    

    def authenticate(self, request, username = None, password = None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            
            else:
                return None
        except User.DoesNotExist as e:
            return f"Error: {e}"
        
    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return user
        except Exception as e:
            return e 
        