# Cython-and-Modularity

The purpose of the code is to demonstrate modularization and optimization using Cython.

The code is modularized into two main files: main.py and utils.py.

main.py serves as the entry point of the program. It imports functions from utils.py to perform calculations and prints the results.
utils.py contains two functions: add_numbers and multiply_numbers, which respectively add and multiply two numbers.
The code is optimized using Cython by creating a separate file cython_code.pyx where the functions add_numbers and multiply_numbers are defined with Cython syntax. The setup.py file is used to build the Cython code into a module.

Overall, the code demonstrates good programming practices by modularizing the code into reusable components and optimizing performance using Cython.

**Runtime Comparison**
The runtime comparison was performed using the time command in the terminal. The screenshot below shows the comparison of the runtimes.
