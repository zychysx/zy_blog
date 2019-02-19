from django.db import models


# Create your models here.


class BlogUser(models.Model):
    user_uuid = models.CharField(max_length=100)
    user_name = models.CharField(max_length=66,unique=True)
    n_name = models.CharField(max_length=20)
    password = models.CharField(max_length=88)
    email = models.CharField(max_length=66)
    super_key = models.BooleanField(default=False)
    private_key = models.BooleanField(default=False) #私人
    write_key = models.BooleanField(default=False)
    comment_key = models.BooleanField(default=True)
    cerate_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'user_table'