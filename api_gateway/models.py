from django.db import models
from django.db.models import CharField
from cryptography.fernet import Fernet
from django.conf import settings

class EncryptedCharField(CharField):
    def __init__(self, max_length=255, *args, **kwargs):
        super(EncryptedCharField, self).__init__(max_length=max_length, *args, **kwargs)

    def to_python(self, value):
        if isinstance(value, str):
            return value
        if value is None:
            return value
        fernet = Fernet(settings.ENCRYPTION_KEY.encode())
        return fernet.decrypt(value.encode()).decode()

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        if value is not None and not isinstance(value, str):
            fernet = Fernet(settings.ENCRYPTION_KEY.encode())
            value = fernet.encrypt(value.encode()).decode()
        return value

    def db_type(self, connection):
        return 'char'

class PaymentOrder(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    payment_type = models.CharField(max_length=15)
    card_number = EncryptedCharField(max_length=20, blank=True, null=True)
    expiration_month = models.PositiveSmallIntegerField()
    expiration_year = models.PositiveSmallIntegerField()
    cvv = models.CharField(max_length=4)
    timestamp = models.DateTimeField(auto_now_add=True)

class PaymentLog(models.Model):
    order = models.ForeignKey(PaymentOrder, on_delete=models.CASCADE)
    status = models.CharField(max_length=15)
    authorization_code = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
