from django.conf import settings


"""
Define remitente de los e-mails
"""
SENDER_EMAIL = getattr(settings, 'SENDER_EMAIL', 'admin@localhost')