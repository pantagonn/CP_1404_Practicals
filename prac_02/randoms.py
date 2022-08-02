"""
Import random
"""

import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Q: What did you see on line 1?
# A: Number 11

# Q: What was the smallest number you could have seen, what was the largest?
# A: The smallest number i could have seen is 5 , while largest number i could have seen is 20.

# Q: What did you see on line 2?
# A: Number 5

# Q: What was the smallest number you could have seen, what was the largest?
# A: The smallest number i could have seen is 3 , while largest number i could have seen is 9.

# Q: Could line 2 have produced a 4?
# A: Not possible because of the 2 step incrementation which will result in an odd number.

# Q: What did you see on line 3?
# A: Number 4.481070144344898

# Q: What was the smallest number you could have seen, what was the largest?
# A: The smallest number i could have seen is 2.5 , while largest number i could have seen is 5.5.

# Q: Write code, not a comment, to produce a random number between 1 and 100 inclusive.
# A:

print(random.randint(1, 100))
