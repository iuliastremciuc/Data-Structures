"""
Constant time: The efficiency doesn't depend on the size of the input. O(1)
Linear time: The efficiency does depend on the size of the input. O(n)

"""

# Runtime Complexity

commands = ['n', 's', 'w', 'e']

# Constant time. Constant runtime doesn't grow as the size of the input incrases
commands[3]

# Constant < Linear

# Linear time. Linear runtime grows 1 to 1 as the size of the input incrases
for command in commands:    # O(n)
    print(command) # O(1)

    for _ in commands: # O(n) 
    # O(n) * O(1) * O(n) == O(n^2)


