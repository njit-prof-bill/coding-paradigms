"""
Factorial Digit Sum Calculator - Functional Programming Implementation

This application calculates the factorial of 100 and then computes the sum of
all digits in the resulting factorial number. Demonstrates functional programming
principles including pure functions, immutability, function composition, and
higher-order functions.
"""

import math
from functools import reduce
from typing import Callable


# FUNCTIONAL PRINCIPLE: Pure Functions
# These functions have no side effects and always return the same output for the same input
def calculate_factorial(number: int) -> int:
    """
    Pure function to calculate factorial of a number.

    Args:
        number: The number to calculate factorial for

    Returns:
        The factorial result as an integer

    Raises:
        ValueError: If number is negative
    """
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    # FUNCTIONAL PRINCIPLE: Using built-in pure function
    return math.factorial(number)


def calculate_digit_sum(number: int) -> int:
    """
    Pure function to calculate sum of digits in a number.

    Args:
        number: The number to calculate digit sum for

    Returns:
        The sum of all digits in the number
    """
    # FUNCTIONAL PRINCIPLE: Immutable data transformation
    # Convert negative to positive without mutating original
    abs_number = abs(number)

    # FUNCTIONAL PRINCIPLE: Function composition and list comprehension
    # Transform number -> string -> list of digits -> sum
    return sum(int(digit) for digit in str(abs_number))


# FUNCTIONAL PRINCIPLE: Higher-Order Functions
# Functions that take other functions as parameters
def create_formatter(title: str) -> Callable[[str], str]:
    """
    Higher-order function that creates a formatter function.

    Args:
        title: The title for the formatter

    Returns:
        A function that formats messages with the given title
    """
    separator = "=" * len(title)

    def format_with_header(message: str = "") -> str:
        """Inner function that uses the closure variable."""
        if message:
            return f"{title}\n{separator}\n\n{message}"
        else:
            return f"{title}\n{separator}\n"

    return format_with_header


def create_message_formatter() -> dict:
    """
    Factory function that returns a dictionary of formatting functions.

    Returns:
        Dictionary containing various message formatting functions
    """
    # FUNCTIONAL PRINCIPLE: Function composition
    header_formatter = create_formatter("Factorial Digit Sum Calculator")

    return {
        "header": lambda: header_formatter(),
        "calculation_start": lambda n: f"Calculating {n}!...",
        "factorial_result": lambda n, f: f"{n}! = {f}\n",
        "final_result": lambda n, s: f"Sum of digits in {n}!: {s}",
    }


# FUNCTIONAL PRINCIPLE: Pure function for side effects (I/O)
def display_message(message: str) -> None:
    """
    Pure function for displaying messages (isolated side effect).

    Args:
        message: The message to display
    """
    print(message)


# FUNCTIONAL PRINCIPLE: Function composition and pipeline
def compose_functions(*functions) -> Callable:
    """
    Compose multiple functions into a single function pipeline.

    Args:
        *functions: Variable number of functions to compose

    Returns:
        A composed function that applies all functions in sequence
    """
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


# FUNCTIONAL PRINCIPLE: Currying - partial application of functions
def create_calculator_pipeline(target_number: int) -> Callable:
    """
    Create a curried calculation pipeline for a specific number.

    Args:
        target_number: The number to calculate factorial and digit sum for

    Returns:
        A function that performs the complete calculation pipeline
    """

    def calculation_pipeline() -> tuple:
        """Execute the calculation pipeline and return results."""
        # FUNCTIONAL PRINCIPLE: Function composition
        factorial_result = calculate_factorial(target_number)
        digit_sum = calculate_digit_sum(factorial_result)

        return target_number, factorial_result, digit_sum

    return calculation_pipeline


# FUNCTIONAL PRINCIPLE: Immutable data structures and pure transformations
def create_result_data(number: int, factorial: int, digit_sum: int) -> dict:
    """
    Create an immutable result data structure.

    Args:
        number: The input number
        factorial: The calculated factorial
        digit_sum: The calculated digit sum

    Returns:
        Immutable dictionary containing all results
    """
    return {
        "number": number,
        "factorial": factorial,
        "digit_sum": digit_sum,
        "factorial_length": len(str(factorial)),
    }


# FUNCTIONAL PRINCIPLE: Pure function for application orchestration
def run_application(target_number: int = 100) -> bool:
    """
    Main application function using functional composition.

    Args:
        target_number: The number to calculate (default: 100)

    Returns:
        True if successful, False otherwise
    """
    try:
        # FUNCTIONAL PRINCIPLE: Create immutable formatters
        formatters = create_message_formatter()

        # FUNCTIONAL PRINCIPLE: Create calculation pipeline
        calculator = create_calculator_pipeline(target_number)

        # FUNCTIONAL PRINCIPLE: Execute pure calculations
        number, factorial, digit_sum = calculator()

        # FUNCTIONAL PRINCIPLE: Create immutable result data
        result_data = create_result_data(number, factorial, digit_sum)

        # FUNCTIONAL PRINCIPLE: Functional pipeline for output
        # Each step is a pure transformation followed by controlled side effect
        messages = [
            formatters["header"](),
            formatters["calculation_start"](result_data["number"]),
            formatters["factorial_result"](
                result_data["number"], result_data["factorial"]
            ),
            formatters["final_result"](result_data["number"], result_data["digit_sum"]),
        ]

        # FUNCTIONAL PRINCIPLE: Map side effects over data
        # Separate calculation from side effects
        for message in messages:
            display_message(message)

        return True

    except Exception as e:
        display_message(f"Error: {e}")
        return False


# FUNCTIONAL PRINCIPLE: Pure main function
def main() -> None:
    """Main entry point using functional approach."""
    # FUNCTIONAL PRINCIPLE: Application as a function call with no side effects in main logic
    run_application()


if __name__ == "__main__":
    main()
