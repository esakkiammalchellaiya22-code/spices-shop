from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    address = models.TextField()

    total_price = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    order_id = models.CharField(
    max_length=20,
    default='ORD001'
)
    status = models.CharField(
    max_length=20,
    default='Pending'
)


    def __str__(self):
        return self.user.username
