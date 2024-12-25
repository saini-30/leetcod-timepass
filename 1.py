from collections import Counter

def min_operations_to_make_good(s):
    # Step 1: Count the frequency of each character
    freq = Counter(s)
    freq_values = list(freq.values())
    
    # Step 2: Determine unique frequency targets
    max_frequency = max(freq_values)  # The highest frequency in the current string
    operations = float('inf')  # To store the minimum number of operations

    # Step 3: Try to make all characters occur `t` times for each t from 1 to max_frequency
    for target in range(1, max_frequency + 1):
        current_operations = 0
        for f in freq_values:
            if f > target:
                # Delete extra characters
                current_operations += (f - target)
            elif f < target:
                # Insert or modify to increase frequency
                current_operations += (target - f)
        
        # Update the minimum operations needed
        operations = min(operations, current_operations)
    
    return operations
