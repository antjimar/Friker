# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Photo(models.Model):
    COPYRIGHT = 'RIG'
    COPYLEFT = 'LEF'
    CREATIVE_COMMONS = 'CC'

    LICENSES = (
        (COPYRIGHT, 'Copyright'),
        (COPYLEFT, 'Copyleft'),
        (CREATIVE_COMMONS, 'Creative Commons')
    )

    VISIBILITY_PUBLIC = 'PUB'
    VISIBILITY_PRIVATE = 'PRI'

    VISIBILITY = (
        (VISIBILITY_PUBLIC, 'Pública'),
        (VISIBILITY_PRIVATE, 'Privada')
    )

    owner = models.ForeignKey(User)  # relacionamos la foto con un usuario (el que da Django)
    name = models.CharField(max_length=150)
    #url = models.URLField()
    url = models.FileField(upload_to="uploads")
    description = models.TextField(blank=True) # permitir estar vacío
    created_at = models.DateTimeField(auto_now_add=True) # cuando se crea se pone a NOW()
    modified_at = models.DateTimeField(auto_now_add=True, auto_now=True) # cuando se crea o modifica, se pone a NOW()
    license = models.CharField(max_length=3, choices=LICENSES)
    visibility = models.CharField(max_length=3, choices=VISIBILITY)

    def __unicode__(self): # es como el toString. Es para mostrar el nombre en la tabla del administrador
        return self.name


    # from http://goo.gl/G2nCu7
    BADWORDS = (u'diseñata', u'limpiatubos', u'abollao', u'abrazafarolas')

    def clean(self):
        """
        Valida que la descripción no contiene tacos (esta validación está a nivel de modelo
        :return:
        """
        for badword in self.BADWORDS:
            if badword in self.description:
                raise ValidationError(badword + u" es una palabra no permitida")


class PhotoFile(models.Model):

    url = models.FileField(upload_to='uploads')
    created_at = models.DateTimeField(auto_now_add=True)