# Project : Vector addition in n-dimensional space

## ENG

### 🎯 Objective
Development of a console program in the Python language for finding the length and coordinates of a vector, which is the result of the addition of two vectors in N-dimensional space, specified by the user, with the possible input and output of data through a file and through the console.

### 📋 Project Description
The program is intended for the addition of two vectors specified by the user, and the calculation of the parameters of the resulting vector.
The project includes:
• Interactive input of vector coordinates through the console.
• The possibility of reading initial data from a file (JSON) and writing the result to a file.
• Calculation of the coordinates of the sum of two vectors.
• Calculation of the length (modulus) of the resulting vector.
• Data validation (checking that vectors have the same dimension).
• A module for backing up spatial geometry data. 

### ⚙️ Installation and Launch
**1.Requirements**
To run the program, Python version 3.8 or higher is required. Third-party libraries are not required (the standard library math and json is used).

**2.Requirements**
 Launch in console mode
Run the main script from the terminal:
python vector_math.py
 
The program will step-by-step ask to enter the dimension of space (N) and coordinates for each vector.
 
3. Launch in file mode
To input data from a file and save the result, execute:
python vector_math.py input.json output.json
 
Example of an input file input.json:
{
    "v1": [1, 2, 3],
    "v2": [4, 5, 6]
}
