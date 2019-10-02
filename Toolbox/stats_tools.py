# This isn't correct, but at least it will give me a benchmark of where I am.
# Link to code challenge instructions

import statistics
import numpy as np

class Stats():
    # creating an empty list

    our_list = []   # setting our list as the attribute?

    def __init__(self, mean, median, mode, variance, std_dev, coeff):

      self.mean = sum(list) / len(list)
      self.median = sum(list) / 2
      self.mode = statistics.mode(list)
      self.variance = np.var(list)
      self.std_dev = stdev(list)
      self.coeff = self.std_dev / self.mean

    def mean(self):   # okay, this is where I'm confused.  I define it above. and again below?
      return sum(list) / len(list)

    def median(self):
      return sum(list) / 2

    def mode(self):
      return statistics.mode(list)

    def variance(self):
      return np.var(list)

    def std_dev(self):
      return stdev(list)

    def coeff(self):
      return self.std_dev / self.mean


##### DIRECTIONS #####
"""
Create a ToolBox dir
Inside the ToolBox dir, make a stats_tools.py file
Inside stats_tools.py make a Stats class
Your Stats class should take in a list
Stats class methods include the mean, median (for odd and even N), mode, variance, standard deviation, and coefficient of variation
You may use NumPy but not for its math methods
Git status, add, status, commit, push
Make a pull request when you are done
"""
