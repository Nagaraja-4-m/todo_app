from django.db import models
from authapp.models import Users

# Create your models here.
class Tasks(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(Users,on_delete=models.DO_NOTHING,related_name='users_task')
    title=models.CharField(max_length=512)
    # description=models.TextField()
    date_updated=models.DateTimeField(auto_now=True)
    date_created=models.DateTimeField(auto_now_add=True)
    status=models.SmallIntegerField(default=0)

    '''
        ========= status codes ===========
        status:0 --> Task added / new task / pending task
        status:1 --> completed task
        status:2 --> deleted task 
    '''