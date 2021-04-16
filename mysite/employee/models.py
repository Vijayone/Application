from django.db import models
from users.models import User
# Create your models here.
class  Emloyee(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	full_name = models.CharField(max_length= 255,null= False)
	department = models.CharField(max_length= 255,null= False)
	salary = models.IntegerField(null= False)
	is_employee = models.BooleanField(default=False)
	join_of_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return "%s and %s " %(self.user.username, self.full_name)

	class Meta:
		app_label = 'employee'
		ordering = ['full_name']
	



