def normalize(values):
  max = None
  min = None
  for value in values:
    if max == None and min == None:
      min = value
      max = value
    else:
      if max < value:
        max = value
      if min > value:
        min = value
        
  value_range = max - min
  result = []
  for i in range(len(values)):
    result.append((values[i] - min)/value_range)
  return result