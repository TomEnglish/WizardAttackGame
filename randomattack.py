import random
import math

def random_attack(attack, percent_range=25):
     multiplier_range = percent_range / 100.0

     random_multiplier = random.uniform(1 - multiplier_range, 1 + multiplier_range)

     return attack * random_multiplier