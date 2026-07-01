"""
### PROBLEM 5: Data Processor
Create a function `process_data()` that:

* Takes required `operation` (string)
* Takes any number of `*numbers`
* Takes optional `round_to` defaulting to 2
* Returns processed data (sum, average, max, min based on operation)
"""

def process_data(operation,*numbers,round_to=2):

    if operation == '+':
      return sum(numbers)
    elif operation == 'avg':
      avg = sum(numbers) / len(numbers)
      return round(avg,round_to)
    elif operation == 'max':
      return max(numbers)
    elif operation == 'min':
      return min(numbers)
    else:
      return "Invalid operation"


print(process_data('avg',12,34,33,2,11.6757979,round_to=3))
