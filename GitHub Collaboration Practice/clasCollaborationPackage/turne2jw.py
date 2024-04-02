# Name: Jared Turner
# email: turne2jw@mail.uc.edu
# Assignment Number: InClass github collabotion
# Due Date:
# Course/Section: IS4010-001
# Semester/Year: spring 2024
# Brief Description of the assignment:This is a collaborative class assignment
# Brief Description of what this module does. This module counts the number of bits 
#191. number of bits 
def hamming_weight(n: int) -> int:
    """
    Calculates the Hamming weight (number of set bits) for a positive integer.
    
    Args:
        n (int): The positive integer in binary representation.
    
    Returns:
        int: Number of set bits (Hamming weight).
    """
    count = 0
    while n > 0:
        # Check if the rightmost bit is set (i.e., equal to 1)
        if n & 1:
            count += 1
        # Right shift n to consider the next bit
        n >>= 1
    return count

def bit():
    # Taking user input for the integer n
    n = int(7)
    # Calculating the Hamming weight and displaying the result
    print(f"The Hamming weight of {n} is: {hamming_weight(n)}")

if __name__ == "__main__":
    bit()