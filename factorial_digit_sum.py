"""
Factorial Digit Sum Calculator - Clean Code Implementation

This application calculates the factorial of 100 and then computes the sum of
all digits in the resulting factorial number. Demonstrates Clean Code principles
including meaningful names, single responsibility, DRY, and self-documentation.

CLEAN CODE PRINCIPLES DEMONSTRATED:
- Meaningful Names: Variables and functions have descriptive, intention-revealing names
- Single Responsibility: Each function and class has one clear purpose
- DRY (Don't Repeat Yourself): Code duplication is minimized
- Self-Documentation: Code explains itself without excessive comments
- Simplicity: Functions are small and focused
- Consistency: Uniform naming conventions and formatting
- Modularity: Code is broken into small, reusable components
"""

import math


# CLEAN CODE: MEANINGFUL NAMES - Class name clearly indicates its purpose
class FactorialCalculator:
    """Calculates factorial values with caching for efficiency."""

    def __init__(self):
        # CLEAN CODE: MEANINGFUL NAMES - Variables clearly indicate their purpose
        self.cached_number = None
        self.cached_result = None

    # CLEAN CODE: SINGLE RESPONSIBILITY - Method does one thing: calculate factorial
    # CLEAN CODE: MEANINGFUL NAMES - Method name is descriptive and intention-revealing
    def calculate(self, number):
        """Calculate factorial of a number with input validation."""
        # CLEAN CODE: SELF-DOCUMENTATION - Code explains intent without comments
        self._validate_input(number)

        if self._is_cached(number):
            return self.cached_result

        result = self._compute_factorial(number)
        self._cache_result(number, result)
        return result

    # CLEAN CODE: MODULARITY - Private methods break down complex operations
    # CLEAN CODE: MEANINGFUL NAMES - Method name clearly states what it validates
    def _validate_input(self, number):
        """Validate that input is suitable for factorial calculation."""
        if number < 0:
            raise ValueError("Factorial undefined for negative numbers")

    # CLEAN CODE: SINGLE RESPONSIBILITY - Method has one job: check cache
    def _is_cached(self, number):
        """Check if result is already cached for this number."""
        return self.cached_number == number and self.cached_result is not None

    # CLEAN CODE: SIMPLICITY - Simple, focused method
    def _compute_factorial(self, number):
        """Compute factorial using built-in function."""
        return math.factorial(number)

    # CLEAN CODE: MODULARITY - Separate caching logic
    def _cache_result(self, number, result):
        """Cache the calculated result for future use."""
        self.cached_number = number
        self.cached_result = result

    # CLEAN CODE: MEANINGFUL NAMES - Method name clearly indicates return value
    def get_last_calculation(self):
        """Return the last calculated number and its factorial."""
        return self.cached_number, self.cached_result


# CLEAN CODE: SINGLE RESPONSIBILITY - Class has one clear purpose
class DigitSumCalculator:
    """Calculates the sum of digits in a number."""

    # CLEAN CODE: MEANINGFUL NAMES - Method name is descriptive and clear
    def calculate(self, number):
        """Calculate sum of all digits in a number."""
        # CLEAN CODE: SELF-DOCUMENTATION - Variable name explains the transformation
        absolute_number = abs(number)

        # CLEAN CODE: SIMPLICITY - One-line solution using built-in functions
        return sum(int(digit) for digit in str(absolute_number))


# CLEAN CODE: MEANINGFUL NAMES - Class name clearly indicates its responsibility
class OutputFormatter:
    """Formats and displays application output."""

    def __init__(self):
        # CLEAN CODE: MEANINGFUL NAMES - Constants have descriptive names
        self.application_title = "Factorial Digit Sum Calculator"
        self.title_separator = "=" * len(self.application_title)

    # CLEAN CODE: SINGLE RESPONSIBILITY - Each method handles one type of output
    def show_header(self):
        """Display application header with title and separator."""
        print(self.application_title)
        print(self.title_separator)
        print()

    # CLEAN CODE: MEANINGFUL NAMES - Method name clearly indicates its purpose
    def show_calculation_start(self, number):
        """Display message indicating calculation is beginning."""
        print(f"Calculating {number}!...")

    # CLEAN CODE: CONSISTENCY - All display methods follow same naming pattern
    def show_factorial_result(self, number, factorial):
        """Display the calculated factorial result."""
        print(f"{number}! = {factorial}")
        print()

    # CLEAN CODE: MEANINGFUL NAMES - Method name clearly indicates final result
    def show_final_result(self, number, digit_sum):
        """Display the final digit sum result."""
        print(f"Sum of digits in {number}!: {digit_sum}")


# CLEAN CODE: MEANINGFUL NAMES - Class name clearly indicates its role
class FactorialDigitSumApplication:
    """Main application that coordinates factorial and digit sum calculations."""

    def __init__(self):
        # CLEAN CODE: MEANINGFUL NAMES - Instance variables have descriptive names
        self.factorial_calculator = FactorialCalculator()
        self.digit_sum_calculator = DigitSumCalculator()
        self.output_formatter = OutputFormatter()
        self.target_number = 100

    # CLEAN CODE: SINGLE RESPONSIBILITY - Method orchestrates the entire workflow
    def run(self):
        """Execute the complete calculation and display workflow."""
        try:
            self._display_application_header()
            factorial_result = self._calculate_factorial()
            self._display_factorial_result(factorial_result)
            digit_sum = self._calculate_digit_sum(factorial_result)
            self._display_final_result(digit_sum)
            return True
        except Exception as error:
            self._handle_error(error)
            return False

    # CLEAN CODE: MODULARITY - Workflow broken into small, focused methods
    # CLEAN CODE: MEANINGFUL NAMES - Method names clearly indicate their actions
    def _display_application_header(self):
        """Display the application header and start message."""
        self.output_formatter.show_header()
        self.output_formatter.show_calculation_start(self.target_number)

    # CLEAN CODE: SINGLE RESPONSIBILITY - Method has one job: calculate factorial
    def _calculate_factorial(self):
        """Calculate factorial for the target number."""
        return self.factorial_calculator.calculate(self.target_number)

    # CLEAN CODE: SELF-DOCUMENTATION - Method name explains what it displays
    def _display_factorial_result(self, factorial_result):
        """Display the calculated factorial result."""
        self.output_formatter.show_factorial_result(
            self.target_number, factorial_result
        )

    # CLEAN CODE: SINGLE RESPONSIBILITY - Method focuses on digit sum calculation
    def _calculate_digit_sum(self, factorial_result):
        """Calculate the sum of digits in the factorial result."""
        return self.digit_sum_calculator.calculate(factorial_result)

    # CLEAN CODE: MEANINGFUL NAMES - Method name clearly indicates final display
    def _display_final_result(self, digit_sum):
        """Display the final digit sum result."""
        self.output_formatter.show_final_result(self.target_number, digit_sum)

    # CLEAN CODE: MODULARITY - Error handling separated into its own method
    def _handle_error(self, error):
        """Handle and display application errors."""
        print(f"Error: {error}")


# CLEAN CODE: SIMPLICITY - Simple, focused function
# CLEAN CODE: MEANINGFUL NAMES - Function name clearly indicates its purpose
def run_factorial_digit_sum_calculator():
    """Create and run the factorial digit sum calculator application."""
    # CLEAN CODE: MEANINGFUL NAMES - Variable name indicates its purpose
    application = FactorialDigitSumApplication()
    application.run()


# CLEAN CODE: CONSISTENCY - Main function follows standard Python convention
def main():
    """Application entry point."""
    run_factorial_digit_sum_calculator()


# CLEAN CODE: STANDARD PATTERN - Common Python idiom for script execution
if __name__ == "__main__":
    main()
