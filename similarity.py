# this code can only run on python2.7
from __future__ import print_function
from scipy import spatial
from collections import Counter
import csv
import codecs
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

filename = codecs.open('pokemon.csv', 'r')

data = csv.DictReader(filename)
mapping = {}

# Create mapping table
for line in data:
  #mapping[(line['height'], line['weight'])]= line['ndex']
  height = line['height'].split("'")
  hundred = float(height[0]) * 12 * 2.54
  number = float(height[1].split('"')[0]) * 2.54
  total_height = hundred + number
  
  weight = line['weight'].split()[0]
  total_weight = float(weight) * 0.454

  mapping[(total_height, total_weight)] = str(line['ndex'])

#print(w_max, w_min, h_max, h_min)

def read_string():
  x = raw_input(">>> Please enter your height(in cm): ")
  y = raw_input(">>> Please enter your weight(in kg): ")
  
  return x, y

# Return pokemon index
def calculate_similarity(height, weight):
  try:
    height = float(height)
    weight = float(weight)
  except ValueError:
    print("Please enter integer or float! ")
    return 1000
  input_1 = [float(height), float(weight)]
  best_score = -1.0
  best_tuple = (None, None)
  for key_1, key_2 in mapping:
    input_2 = [key_1, key_2]
    score = 1 - spatial.distance.cosine(input_1, input_2)
    if score > best_score:
      best_tuple = (key_1, key_2)
      best_score = score

  print("Best Score: ", best_score)
  return mapping[best_tuple]

def main(height, weight):

  try:
    height = float(height)
    weight = float(weight)
  except ValueError:
    print("Please enter integer or float! ")
    return 1000
  index = calculate_similarity(height, weight, mapping)
  return index

'''
if "__name__" == "__main__":
    
  while True:
    height, weight = read_string()
    try:
      height = float(height)
      weight = float(weight)
    except ValueError:
      print("Please enter integer or float! ")
      continue
    index = calculate_similarity(height, weight, mapping)
    print("Your pokemon index: ", index)
'''
