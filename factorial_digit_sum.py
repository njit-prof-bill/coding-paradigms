"""
Factorial Digit Sum Calculator - Functional Programming Implementation

This application calculates the factorial of 100 and then computes the sum of
all digits in the resulting factorial number. Demonstrates functional programming
principles including pure functions, immutability, function composition, and
higher-order functions.

FUNCTIONAL PROGRAMMING CONCEPTS DEMONSTRATED:
- Pure Functions: Functions with no side effects, same input = same output
- Immutability: Data structures that don't change after creation
- Function Composition: Building complex operations from simple functions
- Higher-Order Functions: Functions that take or return other functions
- Currying: Transforming functions to take one argument at a time
- Closures: Functions that capture variables from their outer scope
- Separation of Concerns: Pure logic separated from side effects
"""

import math
from functools import reduce
from typing import Callable, Tuple, Dict, Any


# FUNCTIONAL CONCEPT: PURE FUNCTIONS
# These functions have no side effects and always return the same output for the same input
def calculate_factorial(number: int) -> int:
    """
    Pure function to calculate factorial of a number.

    FUNCTIONAL CONCEPT: PURE FUNCTION - No side effects, deterministic output

    Args:
        number: The number to calculate factorial for

    Returns:
        The factorial result as an integer

    Raises:
        ValueError: If number is negative
    """
    # FUNCTIONAL CONCEPT: IMMUTABLE INPUT VALIDATION
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    # FUNCTIONAL CONCEPT: USING BUILT-IN PURE FUNCTIONS
    return math.factorial(number)


def calculate_digit_sum(number: int) -> int:
    """
    Pure function to calculate sum of digits in a number.

    FUNCTIONAL CONCEPT: PURE FUNCTION - No state mutation, no side effects

    Args:
        number: The number to calculate digit sum for

    Returns:
        The sum of all digits in the number
    """
    # FUNCTIONAL CONCEPT: IMMUTABLE DATA TRANSFORMATION
    # Create new value instead of mutating original
    abs_number = abs(number)

    # FUNCTIONAL CONCEPT: FUNCTION COMPOSITION AND LIST COMPREHENSION
    # Transform: number -> string -> sequence of digits -> sum
    return sum(int(digit) for digit in str(abs_number))


# FUNCTIONAL CONCEPT: HIGHER-ORDER FUNCTIONS
# Functions that take other functions as parameters or return functions
def create_formatter(title: str) -> Callable[[str], str]:
    """
    Higher-order function that creates a formatter function.

    FUNCTIONAL CONCEPT: HIGHER-ORDER FUNCTION - Returns a function
    FUNCTIONAL CONCEPT: CLOSURE - Inner function captures outer scope variable

    Args:
        title: The title for the formatter

    Returns:
        A function that formats messages with the given title
    """
    # FUNCTIONAL CONCEPT: IMMUTABLE LOCAL COMPUTATION
    separator = "=" * len(title)

    # FUNCTIONAL CONCEPT: CLOSURE - Function that captures variables from enclosing scope
    def format_with_header(message: str = "") -> str:
        """Inner function that uses closure variables."""
        if message:
            return f"{title}\n{separator}\n\n{message}"
        else:
            return f"{title}\n{separator}\n"

    return format_with_header


# FUNCTIONAL CONCEPT: FACTORY FUNCTION - Returns data structure of functions
def create_message_formatters() -> Dict[str, Callable]:
    """
    Factory function that returns a dictionary of formatting functions.

    FUNCTIONAL CONCEPT: FACTORY FUNCTION - Creates and returns related functions
    FUNCTIONAL CONCEPT: IMMUTABLE DATA STRUCTURE - Returns dictionary of functions

    Returns:
        Dictionary containing various message formatting functions
    """
    # FUNCTIONAL CONCEPT: FUNCTION COMPOSITION
    header_formatter = create_formatter("Factorial Digit Sum Calculator")

    # FUNCTIONAL CONCEPT: IMMUTABLE DATA STRUCTURE OF FUNCTIONS
    return {
        "header": lambda: header_formatter(),
        "calculation_start": lambda n: f"Calculating {n}!...",
        "factorial_result": lambda n, f: f"{n}! = {f}\n",
        "final_result": lambda n, s: f"Sum of digits in {n}!: {s}",
    }


# FUNCTIONAL CONCEPT: PURE FUNCTION FOR SIDE EFFECTS
# Isolating side effects (I/O) into pure functions
def display_message(message: str) -> None:
    """
    Pure function for displaying messages (isolated side effect).

    FUNCTIONAL CONCEPT: SIDE EFFECT ISOLATION - I/O operations isolated

    Args:
        message: The message to display
    """
    print(message)


# FUNCTIONAL CONCEPT: FUNCTION COMPOSITION
def compose_functions(*functions: Callable) -> Callable:
    """
    Compose multiple functions into a single function pipeline.

    FUNCTIONAL CONCEPT: FUNCTION COMPOSITION - Combining functions
    FUNCTIONAL CONCEPT: HIGHER-ORDER FUNCTION - Takes functions as arguments

    Args:
        *functions: Variable number of functions to compose

    Returns:
        A composed function that applies all functions in sequence
    """
    # FUNCTIONAL CONCEPT: REDUCE - Functional approach to iteration
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


# FUNCTIONAL CONCEPT: CURRYING - Partial application of functions
def create_calculator_pipeline(
    target_number: int,
) -> Callable[[], Tuple[int, int, int]]:
    """
    Create a curried calculation pipeline for a specific number.

    FUNCTIONAL CONCEPT: CURRYING - Partial application of functions
    FUNCTIONAL CONCEPT: CLOSURE - Captures target_number in closure

    Args:
        target_number: The number to calculate factorial and digit sum for

    Returns:
        A function that performs the complete calculation pipeline
    """

    # FUNCTIONAL CONCEPT: CLOSURE - Function captures outer scope variable
    def calculation_pipeline() -> Tuple[int, int, int]:
        """
        Execute the calculation pipeline and return results.

        FUNCTIONAL CONCEPT: PURE FUNCTION - No side effects, deterministic
        """
        # FUNCTIONAL CONCEPT: FUNCTION COMPOSITION - Chaining pure functions
        factorial_result = calculate_factorial(target_number)
        digit_sum = calculate_digit_sum(factorial_result)

        # FUNCTIONAL CONCEPT: IMMUTABLE RETURN VALUE
        return target_number, factorial_result, digit_sum

    return calculation_pipeline


# FUNCTIONAL CONCEPT: IMMUTABLE DATA STRUCTURES
def create_result_data(number: int, factorial: int, digit_sum: int) -> Dict[str, Any]:
    """
    Create an immutable result data structure.

    FUNCTIONAL CONCEPT: IMMUTABLE DATA STRUCTURE - Dictionary that won't be modified
    FUNCTIONAL CONCEPT: PURE FUNCTION - No side effects

    Args:
        number: The input number
        factorial: The calculated factorial
        digit_sum: The calculated digit sum

    Returns:
        Immutable dictionary containing all results
    """
    # FUNCTIONAL CONCEPT: IMMUTABLE DATA CREATION
    return {
        "number": number,
        "factorial": factorial,
        "digit_sum": digit_sum,
        "factorial_length": len(str(factorial)),
    }


# FUNCTIONAL CONCEPT: PARTIAL APPLICATION
def create_partial_formatters(formatters: Dict[str, Callable]) -> Dict[str, Callable]:
    """
    Create partially applied formatter functions.

    FUNCTIONAL CONCEPT: PARTIAL APPLICATION - Pre-filling function arguments
    FUNCTIONAL CONCEPT: HIGHER-ORDER FUNCTION - Works with functions as data

    Args:
        formatters: Dictionary of formatter functions

    Returns:
        Dictionary of partially applied functions
    """
    return {
        "header": formatters["header"],
        "calculation_start": formatters["calculation_start"],
        "factorial_result": formatters["factorial_result"],
        "final_result": formatters["final_result"],
    }


# FUNCTIONAL CONCEPT: PURE FUNCTION FOR APPLICATION ORCHESTRATION
def run_application(target_number: int = 100) -> bool:
    """
    Main application function using functional composition.

    FUNCTIONAL CONCEPT: PURE FUNCTION - Main logic without side effects
    FUNCTIONAL CONCEPT: FUNCTION COMPOSITION - Orchestrating pure functions

    Args:
        target_number: The number to calculate (default: 100)

    Returns:
        True if successful, False otherwise
    """
    try:
        # FUNCTIONAL CONCEPT: IMMUTABLE DATA CREATION
        formatters = create_message_formatters()

        # FUNCTIONAL CONCEPT: CURRYING - Create specialized function
        calculator = create_calculator_pipeline(target_number)

        # FUNCTIONAL CONCEPT: PURE FUNCTION EXECUTION
        number, factorial, digit_sum = calculator()

        # FUNCTIONAL CONCEPT: IMMUTABLE DATA STRUCTURE CREATION
        result_data = create_result_data(number, factorial, digit_sum)

        # FUNCTIONAL CONCEPT: FUNCTIONAL PIPELINE FOR DATA TRANSFORMATION
        # Transform data through series of pure functions
        messages = [
            formatters["header"](),
            formatters["calculation_start"](result_data["number"]),
            formatters["factorial_result"](
                result_data["number"], result_data["factorial"]
            ),
            formatters["final_result"](result_data["number"], result_data["digit_sum"]),
        ]

        # FUNCTIONAL CONCEPT: MAP OPERATION - Apply function to each element
        # Separate pure computation from side effects
        for message in messages:
            display_message(message)

        return True

    except Exception as e:
        # FUNCTIONAL CONCEPT: ERROR HANDLING WITH SIDE EFFECT ISOLATION
        display_message(f"Error: {e}")
        return False


# FUNCTIONAL CONCEPT: PURE MAIN FUNCTION
def main() -> None:
    """
    Main entry point using functional approach.

    FUNCTIONAL CONCEPT: PURE FUNCTION - No side effects in main logic
    """
    # FUNCTIONAL CONCEPT: APPLICATION AS FUNCTION CALL
    run_application()


# FUNCTIONAL CONCEPT: ENTRY POINT
if __name__ == "__main__":
    main()
