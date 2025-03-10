import numpy as np

def hill_climbing(func, start, step_size=0.01, max_iterations=1000):
    current_position = start
    current_value = func(current_position)
    
    for i in range(max_iterations):
        next_position_positive = current_position + step_size
        next_value_positive = func(next_position_positive)
        
        next_position_negative = current_position - step_size
        next_value_negative = func(next_position_negative)
        
        if next_value_positive > current_value and next_value_positive >= next_value_negative:
            current_position = next_position_positive
            current_value = next_value_positive
        elif next_value_negative > current_value and next_value_negative > next_value_positive:
            current_position = next_position_negative
            current_value = next_value_negative
        else:
            break
    
    return current_position, current_value

func_str = input("\nEnter a function of x: ")
x = 0
eval(func_str)

func = lambda x: eval(func_str)



start_str = input("\nEnter the starting value to begin the search: ")
    
start = float(start_str)
        

maxima, max_value = hill_climbing(func, start)
print(f"The maxima is at x = {maxima}")
print(f"The maximum value obtained is {max_value}")