"""
Factorial Digit Sum Calculator - Object-Oriented Implementation

This application calculates the factorial of 100 and then computes the sum of
all digits in the resulting factorial number. Demonstrates OOP principles
including encapsulation, single responsibility, and composition.
"""

import math


class FactorialCalculator:
    """Handles factorial computation with encapsulation of calculation logic."""

    def __init__(self):
        """Initialize the factorial calculator."""
        self._last_calculated_value = None
        self._last_calculated_factorial = None

    def calculate_factorial(self, number: int) -> int:
        """
        Calculate the factorial of a given number.

        Args:
            number: The number to calculate factorial for

        Returns:
            The factorial result as an integer
        """
        if number < 0:
            raise ValueError("Factorial is not defined for negative numbers")

        if number == 0 or number == 1:
            return 1

        # Use Python's built-in math.factorial for efficiency and accuracy
        result = math.factorial(number)

        # Cache the result for potential future use
        self._last_calculated_value = number
        self._last_calculated_factorial = result

        return result

    def get_last_calculation(self) -> tuple:
        """
        Get the last calculated factorial value and its input.

        Returns:
            Tuple of (input_value, factorial_result) or (None, None) if no calculation done
        """
        return self._last_calculated_value, self._last_calculated_factorial


class DigitSumCalculator:
    """Handles digit sum computation for large numbers."""

    def calculate_digit_sum(self, number: int) -> int:
        """
        Calculate the sum of all digits in a number.

        Args:
            number: The number to calculate digit sum for

        Returns:
            The sum of all digits in the number
        """
        if number < 0:
            number = abs(number)  # Handle negative numbers by taking absolute value

        # Convert to string and sum each digit
        digit_sum = sum(int(digit) for digit in str(number))

        return digit_sum


class ResultDisplay:
    """Handles output formatting and display of results."""

    def __init__(self):
        """Initialize the result display handler."""
        self._title = "Factorial Digit Sum Calculator"
        self._separator = "=" * len(self._title)

    def display_header(self):
        """Display the application header."""
        print(self._title)
        print(self._separator)
        print()

    def display_calculation_start(self, number: int):
        """
        Display message indicating calculation is starting.

        Args:
            number: The number being calculated
        """
        print(f"Calculating {number}!...")

    def display_factorial_result(self, number: int, factorial: int):
        """
        Display the factorial result.

        Args:
            number: The input number
            factorial: The calculated factorial
        """
        print(f"{number}! = {factorial}")
        print()

    def display_final_result(self, number: int, digit_sum: int):
        """
        Display the final digit sum result.

        Args:
            number: The input number
            digit_sum: The calculated digit sum
        """
        print(f"Sum of digits in {number}!: {digit_sum}")


class Application:
    """Main application orchestrator that coordinates all components."""

    def __init__(self):
        """Initialize the application with its components."""
        self._factorial_calculator = FactorialCalculator()
        self._digit_sum_calculator = DigitSumCalculator()
        self._result_display = ResultDisplay()
        self._target_number = 100  # Hardcoded as per requirements

    def run(self):
        """
        Execute the main application logic.

        This method orchestrates the entire calculation process:
        1. Display header
        2. Calculate factorial
        3. Calculate digit sum
        4. Display results
        """
        try:
            # Display application header
            self._result_display.display_header()

            # Indicate calculation is starting
            self._result_display.display_calculation_start(self._target_number)

            # Calculate factorial
            factorial_result = self._factorial_calculator.calculate_factorial(
                self._target_number
            )

            # Display factorial result
            self._result_display.display_factorial_result(
                self._target_number, factorial_result
            )

            # Calculate digit sum
            digit_sum = self._digit_sum_calculator.calculate_digit_sum(factorial_result)

            # Display final result
            self._result_display.display_final_result(self._target_number, digit_sum)

        except Exception as e:
            print(f"Error: {e}")
            return False

        return True


def main():
    """Main entry point for the application."""
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
