import math

from typing import Collection


def distance_on_circumference(a: float, b: float, circumference: float = 1.) -> float:
    distance = abs(a - b)
    if distance >= circumference / 2.:
      return circumference - distance
    return distance


def uniform_distribution_on_circumference(values: Collection[float]) -> float:
  l = len(values)
  assert 0 < l
  if l == 1:
    return 0.
    
  s = 0.
  for i, each_value in enumerate(values):
    for j in range(i+1, len(values)):
      other_value = values[j]
      s += math.sqrt(distance_on_circumference(each_value, other_value))
  
  return s / (l * (l - 1) / 2.)


def concentration(values: Collection[float]) -> float:
  '''
  Given a collection of values, return the concentration of the values. 
  
  The concentration of a collection of values is the proportion of the values that are the maximum
  value of the collection.
  
  :param values: Collection[float]
  :type values: Collection[float]
  :return: The concentration of the values.
  '''
  assert all(x >= 0. for x in values)
  no_values = len(values)
  if 0 >= no_values:
      return 0.
  if 1 >= no_values:
    return 1.

  value_sum = sum(values)
  if 1 >= no_values:
      return float(0. < value_sum)

  value_average = value_sum / no_values
  normalize_quotient = value_sum - value_average
  if 0. >= normalize_quotient:
    return 0.

  return (max(values) - value_average) / normalize_quotient


def linear_to_circular(x: float, y: float, value: float, radius: float=1.) -> tuple[float, float]:
  '''
  Given a value between 0 and 1, return the corresponding point on a circle of radius 1
  
  :param x: The x coordinate of the center of the circle
  :type x: float
  :param y: The y-coordinate of the center of the circle
  :type y: float
  :param value: the value of the parameter, between 0 and 1
  :type value: float
  :param radius: The radius of the circle
  :type radius: float
  :return: The coordinates of the point on the circle.
  '''
  assert 1. >= value >= 0.
  assert 0. < radius
  theta = 2. * math.pi * value
  return x + radius * math.cos(theta), y + radius * math.sin(theta)

def segment_length(a_radian: float, b_radian: float) -> float:
  '''
  Given two angles in radians, return the length of the segment between them.
  
  :param a_radian: The first angle in radians
  :type a_radian: float
  :param b_radian: The second angle in radians
  :type b_radian: float
  :return: The length of the segment
  '''
  return math.sqrt(math.pow(math.cos(b_radian) - math.cos(a_radian), 2) + math.pow(math.sin(b_radian) - math.sin(a_radian), 2))