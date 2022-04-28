def linear_search(list, target):
  """
  Returns the index position of the target if found, else returns none
  """

  for i in range(0, len(list)):
    if list[i] == target:
      return i
  return None



numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20]

print(linear_search(numbers, 8))