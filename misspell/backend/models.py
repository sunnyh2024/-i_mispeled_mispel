from django.db import models
import random

def generate_code():
  allowed = '1234567890'
  while True:
    code = ''.join([random.choice(allowed) for _ in range(6)])
    if Room.objects.filter(code=code).count() == 0:
      break
  return code    

class Player(models.Model):
  name = models.CharField(max_length=11, default="", unique=True)
  score = models.IntegerField(default = 0)

class Room(models.Model):
  code = models.CharField(max_length=6, default="", unique=True)
  full = models.BooleanField(default=False)


  #TODO: Add players

  # players = 

  # num of players
  # players

  # current_word
  # 30 seconds



