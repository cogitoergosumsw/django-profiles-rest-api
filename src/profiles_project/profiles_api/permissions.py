from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    Allow users to edit their own profile
    """

    def has_object_permission(self, request, view, obj):
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

class PostOwnStatus(permissions.BasePermission):
    """
    Allow users to update their own status
    """

    def has_object_permission(self, request, view, obj):
        """
        check if user is trying to update their own status
        :param request:
        :param view:
        :param obj:
        :return:
        """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id