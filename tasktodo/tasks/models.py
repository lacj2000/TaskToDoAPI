from django.db import models

from django.contrib.auth.models import User
class Task(models.Model):
    name = models.CharField(max_length= 128)
    description = models.CharField(max_length= 2048)
    create = models.DateTimeField(auto_now_add= True, blank= True)
    check = models.BooleanField(default= False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.name

    def get_check(self):
        if(self.check==False):
            self.check = True
            self.save()
        return self

    def get_uncheck(self):
        if(self.check==True):
            self.check = False
            self.save()
        return self
         
    def check_user(self, user):
        return (self.user == user)


class Sublist(models.Model):
    title = models.CharField(max_length= 128)
    task = models.ForeignKey(Task, related_name='sublists', on_delete= models.CASCADE)

    def __str__(self):
        return self.title+"("+self.task.name+")"

    def check_user(self, user):
        return (self.task.user == user)
    
 
class Item(models.Model):    
    text = models.CharField(max_length= 128)
    check = models.BooleanField(default= False)
    sublist = models.ForeignKey(Sublist, related_name='items', on_delete= models.CASCADE)

    def __str__(self):
        return self.text+"("+self.sublist.title+")"

    def check_user(self, user):
        return (self.sublist.task.user == user)
    
    def get_check(self):
        if(self.check==False):
            self.check = True
            self.save()
        return self

    def get_uncheck(self):
        if(self.check==True):
            self.check = False
            self.save()
        return self
