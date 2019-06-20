from django.core.exceptions import PermissionDenied


def check_is_admin(user):
    if not user.is_anonymous and user.is_admin:
        return True
    else:
        raise PermissionDenied
