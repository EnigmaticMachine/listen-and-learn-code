# Importing specific tools from the more_itertools library
# --------------------------------------------------------
# The more_itertools library extends Python's built-in iteration tools,
# providing additional ways to process and manage data efficiently.

from more_itertools import chunked, distinct_permutations, ilen

# Example 1: Using `chunked` to break data into smaller pieces
# ------------------------------------------------------------
# Imagine you have a long list of numbers, and you want to break it down into smaller parts,
# like slicing a loaf of bread into pieces. The `chunked` function from more_itertools helps you do this.
# It creates an iterator that yields chunks (sub-lists) of a specified size from the original list.

# Here, we create an iterator that yields chunks of 3 elements each from a range of numbers from 0 to 9.
chunks = chunked(range(10), 3)

# We can now iterate over these chunks using a `for` loop.
# The loop will print each chunk (sub-list) one by one.
for chunk in chunks:
    print(chunk)

# Output Explanation:
# The output will be:
# [0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]
# [9]
# Each line represents a chunk of 3 elements from the original range. The last chunk may have fewer elements if the total count is not a multiple of 3.


# Example 2: Using `distinct_permutations` to find unique arrangements
# --------------------------------------------------------------------
# Now, let’s explore another example from the more_itertools library: `distinct_permutations`.
# This function helps find all unique permutations of a list of items, meaning it gives you every possible arrangement
# of the items but without repeating any identical arrangements.

# Imagine you have three cards in your hand: two with the number 1 and one with the number 2.
# You want to see all the different ways you can arrange these cards. The `distinct_permutations` function is like
# a helper that shuffles the cards and shows you each unique arrangement.

# We create an iterator for the distinct permutations of the list [1, 2, 1].
perms = distinct_permutations([1, 2, 1])

# We then iterate over these permutations and print each one.
for perm in perms:
    print(perm)

# Output Explanation:
# The output will include all unique permutations of the list [1, 2, 1]:
# (1, 2, 1)
# (1, 1, 2)
# (2, 1, 1)
# Each permutation is printed as a tuple. Note that even though the list [1, 2, 1] has repeated elements,
# `distinct_permutations` ensures that only unique arrangements are shown, avoiding duplicates.


# Example 3: Using `ilen` to efficiently count filtered items
# -----------------------------------------------------------
# Finally, let’s consider a situation where you need to count specific items within a large dataset.
# For instance, imagine you want to count how many numbers between 1 and 1,000,000 are divisible by 3.

# We create a generator expression that yields numbers divisible by 3.
gen = (x for x in range(1000000) if x % 3 == 0)

# To count how many such numbers there are, we use the `ilen` function from more_itertools.
# `ilen` efficiently counts the number of items produced by the generator.
count = ilen(gen)

# Print the count of numbers divisible by 3.
print(f"gen count ilen: {count}")

# Output Explanation:
# The output will be:
# gen count ilen: 333333
# This tells us that there are 333,333 numbers between 1 and 1,000,000 that are divisible by 3.
# The generator expression generates these numbers on-the-fly, and `ilen` efficiently counts them
# without needing to store all the numbers in memory at once.


# Summary of Concrete Implementations of the Iterator Pattern:
# ------------------------------------------------------------
# In these examples, we’ve seen how the more_itertools library provides concrete implementations of the Iterator pattern
# that help us handle and process data smoothly and efficiently.
# - The `chunked` function breaks down large data sets into smaller, manageable chunks.
# - The `distinct_permutations` function generates unique arrangements of items, avoiding duplicates.
# - The `ilen` function efficiently counts items produced by a generator or iterator.

# These tools make big tasks more manageable by processing data one piece at a time,
# allowing you to work with large datasets in an efficient and organized way. The Iterator pattern is a powerful concept
# in Python, and more_itertools offers practical and concrete ways to apply it in real-world programming scenarios.
