# Data Analyzer and Transformer Program

**Author:** Jaineel Shingala\
**Language:** Python 3\
**Project:** Data Analyzer and Transformer Program

## Project Description

This is a menu-driven Python program for entering and analyzing a
one-dimensional array of integer values. It demonstrates Python built-in
functions, recursion, lambda functions, sorting, and returning multiple
values from a function.

## Program Menu

1.  Input Data
2.  Display Data Summary (Built-in Functions)
3.  Calculate Factorial (Recursion)
4.  Filter Data by Threshold (Lambda Function)
5.  Sort Data
6.  Display Dataset Statistics (Return Multiple Values)
7.  Exit Program

## Features

-   **Input Data:** Accepts integer values separated by spaces.
-   **Data Summary:** Displays total elements, minimum value, maximum
    value, sum, and average.
-   **Factorial:** Calculates a number's factorial using recursion.
-   **Filter Data:** Uses a lambda function with `filter()` to display
    values greater than or equal to a threshold.
-   **Sort Data:** Sorts the entered data in ascending or descending
    order.
-   **Dataset Statistics:** Returns minimum, maximum, sum, and average
    as multiple values.
-   **Exit:** Closes the program.

## Requirements

-   Python 3.x
-   No external libraries are required.

## How to Run

1.  Download `project4.py`.

2.  Open Command Prompt or a terminal in the folder containing the file.

3.  Run:

    ``` bash
    python project4.py
    ```

4.  Enter a menu option from `1` to `7` when prompted.

## Example Run Shown in the Screenshots

The supplied screenshots show the following inputs:

  Operation                                 Input
  ---------------------------- ------------------
  Input data                                 `12`
  Display data summary            Menu choice `2`
  Calculate factorial                         `8`
  Filter threshold                          `123`
  Sort order                     Descending (`2`)
  Display dataset statistics      Menu choice `6`
  Exit program                    Menu choice `7`

### Results in the Screenshots

For the entered dataset containing the single value `12`:

-   Total elements: `1`
-   Minimum value: `12`
-   Maximum value: `12`
-   Sum of all values: `12`
-   Average value: `12.00`
-   Factorial of `8`: `40320`
-   Filtering with threshold `123`: no values are displayed because `12`
    is below the threshold.
-   Descending sort: `12`

## Python Concepts Used

-   Functions
-   Lists and user input
-   `while` loop and `if-elif-else` conditions
-   Built-in functions: `len()`, `min()`, `max()`, and `sum()`
-   Recursion
-   Lambda function
-   `filter()`
-   `sorted()`
-   Returning multiple values
-   Exception handling with `try` and `except`

## Output Screenshots

The screenshots below are included in this project folder. They are
displayed directly in this README when viewed on GitHub or in a Markdown
viewer that supports relative image paths.

### Screenshot 1 -- Input Data and Data Summary

`<img src="output_1.png" alt="Screenshot 1: Input data and data summary" width="700">`{=html}

### Screenshot 2 -- Factorial and Threshold Filtering

`<img src="output_2.png" alt="Screenshot 2: Factorial and threshold filtering" width="700">`{=html}

### Screenshot 3 -- Sorting and Dataset Statistics

`<img src="output_3.png" alt="Screenshot 3: Sorting and dataset statistics" width="700">`{=html}

### Screenshot 4 -- Exit Program

`<img src="output_4.png" alt="Screenshot 4: Exit program" width="700">`{=html}

## Project Structure

``` text
data_analyzer_readme/
├── project4.py
├── README.md
├── output_1.png
├── output_2.png
├── output_3.png
└── output_4.png
```

------------------------------------------------------------------------

**Author: Jaineel Shingala**
