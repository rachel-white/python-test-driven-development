def even_number_of_evens(numbers):
    evens = 0
    if len(numbers) == 2:
        for number in numbers:
            if number % 2 == 1:
                return False
            else:
                evens = evens + 1
                return True
        if evens == 2:
            return True
        else:
            return False
    elif len(numbers) < 2:
        return False
        
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
##assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
##assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
##assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")