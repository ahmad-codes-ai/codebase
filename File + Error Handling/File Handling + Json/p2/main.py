'''
Problem 2: Number Processor 🔢
You have a file called numbers.txt with this content:

text
12,45,78,34,90,11,56
Your task:

Read the file, split the numbers by commas, and convert them to integers.

Calculate the sum, average (as a float), minimum, and maximum.

Write the results to results.txt in this format:

text
Sum: 326
Average: 46.57
Minimum: 11
Maximum: 90

'''


with open('numbers.txt','r') as f:
    data = f.read()
    raw_numbers = data.split(',')
    final_numbers = []
    for num in raw_numbers:
        final_numbers.append(int(num))
    s = sum(final_numbers)
    avg = sum(final_numbers) / len(final_numbers)
    minimum = min(final_numbers)
    maximum = max(final_numbers)

with open('results.txt','w') as f:
    f.write(f"Sum: {s}\nAverage: {avg}\nMinimum: {minimum}\nMaximum: {maximum}")

