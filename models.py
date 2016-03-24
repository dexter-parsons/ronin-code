from django.db import models

# Create your models here.
#from django.db import models

# Create your models here.

class Goals(models.Model):
	goal_text = models.CharField(max_length=255) # now i can submit my goal_text in lower case here
	hash = models.CharField(max_length=100, default="")

	def __unicode__(self):
		return self.goal_text	

class Goals_log(models.Model):
	goals_id = models.ForeignKey(Goals)
	user = models.CharField(max_length=32) #need to put placeholder in the form field
	time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.user

class Goalsco(models.Model):
	goals_id_a = models.ForeignKey(Goals, related_name="goal_a")
	goals_id_b = models.ForeignKey(Goals, related_name="goal_b") #this should have the many to many relationship with the user
	count = models.IntegerField(default=0) #could also use AutoField for automatic increments.

	#class Meta:
		#unique_together = ('goals_id_a', 'goals_id_b') #this for enforce the code to check for goal_a != goal_b
 # we need code to set the goals_id_a and _b to "goals" model, and then to count the id the number of times each user has visited.

