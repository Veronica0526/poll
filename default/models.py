from django.db import models

# Create your models here.
class Poll(models.Model):
    title = models.Charfield("投票主題"), max_length=250)
    date_created = models.Datefield("建立日期"), auto_now=False, auto_now_add=True)

    def __str__(self)
       return self.subject
class Option(models):
    title = models.Charfield("選項標題"), max_length=50)
    count = models.Integerfield("票數")
    poll_id = models.Integerfield("投票主題")

    def __str__(self):
        return str(self.poll.id) + ": " + self.title