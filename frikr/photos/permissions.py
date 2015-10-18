# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission



class UserPermision(BasePermission):

    def has_permission(self, request, view):
        """
        Queremos que:
            - Solo los administradores puedan ver el listado o detalle de cualquier usuario (GET)
            - Cualquiera pueda crear un usuario (para que se registren) (POST)
            - Sólo pueden ver el detalle de los usuarios si accedes a tu mismo usuario (ver mi perfil)
            - Si eres un administrador, puedes ver el detalle de cualquier usuario
        Define si tiene permiso para ejecutar esta acción
        :param request: petición recibida
        :param view: vista que se está ejecutando
        :return: boolean
        """

        if request.method == "POST":
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False

    # def has_object_permission(self, request, view, obj):
    #     """
    #     Esto sólo se ejecuta cuando es una petición PUT o DELETE (operación de escritura)
    #     Si es superuser va a poder actualizar o borrar cualquier usuario.
    #     Si no es superuser, sólo va a poder actualizar o borrar su usuario.
    #     :param request: petición
    #     :param view: vista
    #     :param obj: objeto usuario sobre el que se quiere actuar
    #     :return:
    #     """
    #     return request.user == obj or request.user.is_superuser