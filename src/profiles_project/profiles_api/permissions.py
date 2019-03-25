from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    Allow users to edit their own profile
    """

    def has_object_permission(self, request: Request, view: View, obj: Any):
        """
        Check user is trying to edit their own profile
        :param request:
        :param view:
        :param obj:
        :return:
        """

        if request.method in permissions.SAFE_METHODS:
            return True

        # check if the user is trying to change its own profile
        return obj.id == request.user.id
