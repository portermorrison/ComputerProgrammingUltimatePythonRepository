# 03ConditionalsAndFunctions

1. `rpn_calculator.py`
   Prompt the user three times: first for a mathematical operation from choices `+`, `-`, `*` or `/`. Then for a first number, then for a second number. Print the result of applying the mathematical operator on the two numbers.

    | operator | first number | second number | result |
    | -------- | ------------ | ------------- | ------ |
    | `+`      | 2            | 7             | 9      |
    | `-`      | 2            | 3             | -1     |
    | `*`      | 3            | 8             | 24     |
    | `/`      | 7            | 4             | 1.75   |

1. `grade_utilities.py` - `is_valid_act_score`
   Write a function called `is_valid_act_score` which takes an integer as input and returns `True` or `False`, depending on whether the input represents a valid ACT score. Valid ACT scores are integers between 1 and 36 inclusive.

    | input | output  |
    | ----- | ------- |
    | 23    | `True`  |
    | 0     | `False` |
    | 36    | `True`  |
    | 37    | `False` |

    In the file, demonstrate a few uses of the function in a human readable way.

1. `grade_utilities.py` - `percent_to_letter_grade`
   Write a function called `percent_to_letter_grade` that takes one input: a number representing a percent grade. It should return (output) a single letter: either "A", "B", "C", "D", or "F" according to the following grading scale:

    | input percent | output letter |
    | ------------- | ------------- |
    | 90-100        | "A"           |
    | 80-89.9       | "B"           |
    | 70 - 79.9     | "C"           |
    | 60-69.9       | "D"           |
    | 0 - 59.9      | "F"           |

    In the file, demonstrate a few uses of the function in a human readable way.

1. `grade_utilities.py` - `same_letter_grade`
   Write a function called `same_letter_grade` that takes two inputs: a number that is a percent grade for student 1, and a number that is a percent grade for student 2. It should output (return) `True` if the two students have the same grade letter (e.g. 79.2 and 73.8 both have "C" grades), and `False` if they have different letter grades (e.g. 68.2 and 71.1 have different grades - a "D" and a "C").

    In the file, demonstrate a few uses of the function in a human readable way.

1. `stats_utilities.py` - `range`
   Write a function called `range` that takes three numbers as inputs. It should return the range of the set of numbers (the highest number minus the lowest number). For example,

    | input1 | input2 | input3 | output |
    | ------ | ------ | ------ | ------ |
    | 3      | 1      | 5      | 4      |
    | 7      | 7      | 7      | 0      |
    | -1     | 0      | -1     | 1      |

    In the file, demonstrate a few uses of the function in a human readable way.

1. `stats_utilities.py` - `median`
   Write a function called `median` that takes three numbers as inputs. It should return the median of the set of numbers (not the largest, not the smallest, but the middle). For example,

    | input 1 | input 2 | input3 | output |
    | ------- | ------- | ------ | ------ |
    | -6      | -2      | -4     | -4     |
    | 1       | 3       | 1      | 1      |
    | 0       | -2      | 1      | 0      |

    In the file, demonstrate a few uses of the function in a human readable way.
