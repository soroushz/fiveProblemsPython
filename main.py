# Number 1: FizzBuzz
def fizz_buzz(number):
    for i in range(1, number):
        if i % 3 == 0 and i % 5 == 0: # The order is important
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

#fizz_buzz(101)

# Number 2: Palindrome
def palindrome(original_str):
    normalized_str = ''.join(e for e in original_str if e.isalnum()).lower()
    reversed_str = normalized_str[::-1]
    if reversed_str == normalized_str:
        print("It's Palindrome ")

#palindrome('BOb')

# Number 3: Two numbers Sum
def two_sum(nums, target):
    # Initialize a dictionary to store numbers and their indices
    num_map = {}

    # Iterate over the list with indices
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num

        # Check if the complement is in the dictionary
        if complement in num_map:
            # Return the indices of the complement and the current number
            return [num_map[complement], i]

        # Add the current number and its index to the dictionary
        num_map[num] = i


# Example usage
#print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
#print(two_sum([3, 2, 4], 6))  # Output: [1, 2]
#print(two_sum([3, 3], 6))  # Output: [0, 1]

# Number 4: Longest Substring Without Repeating Characters,
def length_of_longest_substring(s):
    characters = set()
    start = 0
    max_length = 0

    for end in range(len(s)):
        while s[end] in characters:
            characters.remove(s[start])
            start += 1
        characters.add(s[end])
        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage
st = "ABCCJKKK".lower()
#print(length_of_longest_substring(st))  # Output: 3



# Number 5: Product of Array Except Self
def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Step 1: Calculate left products and store in result array
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Step 2: Calculate right products and update result array
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result

# Example usage
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]
