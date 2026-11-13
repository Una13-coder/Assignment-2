import sys
import math

def load_data(filepath:str, column:int)-> tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column

    # Step 1: Make an empty list to store numbers
    numbers = []
    # Step 2: Create a variable called count_lines, starting at 0, to count the lines
    count_lines = 0
    # Step 3: Open the file and read it one line at a time
    with open(filepath, 'r') as infile:
        for line in infile:
            # Step 4: Every time the loop runs, count_lines goes up by 1
            count_lines += 1
            # Step 5: Split the line into a list of columns at every tab
            columns = line.split("\t")
            # Step 6: Look up the chosen column, and if it is out of range, print an error and exit
            try:
                value = columns[column]
            except IndexError:
                print("Exiting: There is no valid 'list index' in column " + str(column) + " in line " + str(count_lines) + " in file: " + filepath.split("/")[-1])
                sys.exit()
            # Step 7: Turn the value into a number, and if it is text (ValueError), skip this line
            try:
                number = float(value)
            except ValueError:
                continue
            # Step 8: Skip NaN values, and add the valid numbers to the list
            if number != number:
                continue
            numbers.append(number)
    # Step 9: If no valid numbers were found, show an error and stop the program
    if len(numbers) == 0:
        print("Error: There were no valid number(s) in column " + str(column) + " in file: " + filepath.split("/")[-1])
        sys.exit()
    # Step 10: Return the list of numbers and the total number of lines read
    return numbers, count_lines

def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers

    # Step 1: Create a variable called total and set it to 0 before adding anything
    total = 0
    # Step 2: For every number in the list, add it to total
    for number in numbers:
        total += number
    # Step 3: Divide the total by how many numbers there are
    average = total / len(numbers)
    # Step 4: Return the average
    return average

def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    
    # Step 1: Set both maximum and minimum to the first number, then check the rest of the list against them
    maximum_value = numbers[0]
    minimum_value = numbers[0]
    # Step 2: Loop over the list, and if a number beats the current maximum or minimum, save it as the new one
    for number in numbers:
        if number > maximum_value:
            maximum_value = number
        if number < minimum_value:
            minimum_value = number
    # Step 3: Return the maximum first, then the minimum
    return maximum_value, minimum_value
    

def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list

    # Step 1: With one number there is nothing to compare, so return 0.0
    if len(numbers) == 1:
        return 0.0
    # Step 2: Find the average by passing the list to calculate_average
    mean = calculate_average(numbers)
    # Step 3: Create a variable called squared_sum, set to 0, to add up the squared distances
    squared_sum = 0
    # Step 4: For each number, subtract the average, multiply the result by itself, and add that to squared_sum
    for number in numbers:
        squared_sum += (number - mean) * (number - mean)
    # Step 5: Divide by (n - 1) and return the result
    return squared_sum / (len(numbers) - 1)

def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list

    # Step 1:  Use calculate_variance (the function above) to work out the variance, and store it in variance
    variance = calculate_variance(numbers)
    # Step 2: The standard deviation is the square root of the variance
    return math.sqrt(variance)

def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
  
    # Step 1: Put the numbers in order, from the smallest to the biggest
    ordered_list = sorted(number)
    # Step 2: Use len() to count the numbers, then use // 2 to find the index of the middle
    n = len(ordered_list)
    middle_position = n // 2
    # Step 3: If the count is odd, return the middle number
    if n % 2 == 1:
        return float(ordered_list[middle_position])
    # Step 4: If there is an even number of values, add the two middle ones and divide by 2
    return (ordered_list[middle_position - 1] + ordered_list[middle_position]) / 2