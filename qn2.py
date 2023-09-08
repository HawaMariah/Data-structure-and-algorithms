def remove_duplicates(sequence):
    unique_set = set()
    result = []
    
    for item in sequence:
        if item not in unique_set:
            result.append(item)
            unique_set.add(item)
    
    return result

#test
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
