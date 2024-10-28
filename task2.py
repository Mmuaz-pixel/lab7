def generate_permutations(s, exclude_duplicates=True):
    """
    Generates all permutations of a given string using recursion.
    
    Parameters:
    - s (str): The input string.
    - exclude_duplicates (bool): If True, excludes duplicate permutations.
    
    Returns:
    - List of all unique permutations of the string.
    
    Raises:
    - TypeError: If input is not a string.
    - ValueError: If the input string is empty.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    if len(s) == 0:
        raise ValueError("Input string cannot be empty.")
    
    permutations = []
    _permute_recursive(list(s), 0, len(s) - 1, permutations, exclude_duplicates)
    return permutations

def _permute_recursive(chars, left, right, permutations, exclude_duplicates):
    """
    Helper recursive function to generate permutations.
    
    Parameters:
    - chars (list): List of characters in the string.
    - left (int): Starting index for permutation.
    - right (int): Ending index for permutation.
    - permutations (list): List to store all permutations.
    - exclude_duplicates (bool): If True, excludes duplicate permutations.
    """
    if left == right:
        perm = ''.join(chars)
        if not exclude_duplicates or perm not in permutations:
            permutations.append(perm)
    else:
        seen = set()
        for i in range(left, right + 1):
            if exclude_duplicates and chars[i] in seen:
                continue
            seen.add(chars[i])
            chars[left], chars[i] = chars[i], chars[left]  # Swap
            _permute_recursive(chars, left + 1, right, permutations, exclude_duplicates)
            chars[left], chars[i] = chars[i], chars[left]  # Backtrack
            
def generate_permutations_iterative(s):
    """
    Generates all permutations of a given string using an iterative approach (Heap's Algorithm).
    
    Parameters:
    - s (str): The input string.
    
    Returns:
    - List of all permutations of the string.
    
    Raises:
    - TypeError: If input is not a string.
    - ValueError: If the input string is empty.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    if len(s) == 0:
        raise ValueError("Input string cannot be empty.")
    
    chars = list(s)
    n = len(chars)
    permutations = []
    c = [0] * n  # Initialize counter array
    permutations.append(''.join(chars))
    
    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                chars[0], chars[i] = chars[i], chars[0]
            else:
                chars[c[i]], chars[i] = chars[i], chars[c[i]]
            permutations.append(''.join(chars))
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    
    return permutations

# Example usage
try:
    input_string = "1x3e"
    print("Permutations (recursive, excluding duplicates):")
    print(generate_permutations(input_string, exclude_duplicates=True))
    
    print("\nPermutations (iterative):")
    print(generate_permutations_iterative(input_string))
except TypeError as e:
    print(f"TypeError: {e}")
except ValueError as e:
    print(f"ValueError: {e}")
