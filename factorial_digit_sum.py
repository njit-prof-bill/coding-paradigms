"""
Factorial Digit Sum Calculator - Object-Oriented Implementation

This application calculates the factorial of 100 and then computes the sum of
all digits in the resulting factorial number. Demonstrates OOP principles
including encapsulation, single responsibility, and composition.

OOP CONCEPTS DEMONSTRATED:
- Encapsulation: Private attributes and methods, data hiding
- Single Responsibility Principle: Each class has one clear purpose
- Composition: Classes working together to achieve functionality
- Abstraction: Complex operations hidden behind simple interfaces
- Modularity: Code organized into logical, reusable units
"""

import math


# OOP CONCEPT: CLASS DEFINITION - Blueprints for creating objects
class FactorialCalculator:
    """
    Handles factorial computation with encapsulation of calculation logic.

    OOP CONCEPT: SINGLE RESPONSIBILITY PRINCIPLE
    This class has one clear responsibility: calculating factorials
    """

    def __init__(self):
        """
        Initialize the factorial calculator.

        OOP CONCEPT: CONSTRUCTOR - Special method to initialize object state
        """
        # OOP CONCEPT: ENCAPSULATION - Private attributes (name mangling with _)
        # These attributes are hidden from direct external access
        self._last_calculated_value = None
        self._last_calculated_factorial = None

    def calculate_factorial(self, number: int) -> int:
        """
        Calculate the factorial of a given number.

        OOP CONCEPT: METHOD - Function that operates on object data
        OOP CONCEPT: ABSTRACTION - Complex calculation hidden behind simple interface

        Args:
            number: The number to calculate factorial for

        Returns:
            The factorial result as an integer
        """
        # OOP CONCEPT: DATA VALIDATION - Protecting object state
        if number < 0:
            raise ValueError("Factorial is not defined for negative numbers")

        if number == 0 or number == 1:
            return 1

        # Use Python's built-in math.factorial for efficiency and accuracy
        result = math.factorial(number)

        # OOP CONCEPT: STATE MANAGEMENT - Updating internal object state
        # Cache the result for potential future use
        self._last_calculated_value = number
        self._last_calculated_factorial = result

        return result

    def get_last_calculation(self) -> tuple:
        """
        Get the last calculated factorial value and its input.

        OOP CONCEPT: ACCESSOR METHOD - Controlled access to private data
        OOP CONCEPT: ENCAPSULATION - Providing controlled access to internal state

        Returns:
            Tuple of (input_value, factorial_result) or (None, None) if no calculation done
        """
        return self._last_calculated_value, self._last_calculated_factorial


# OOP CONCEPT: SEPARATE CLASS FOR DIFFERENT RESPONSIBILITY
class DigitSumCalculator:
    """
    Handles digit sum computation for large numbers.

    OOP CONCEPT: SINGLE RESPONSIBILITY PRINCIPLE
    This class has one clear responsibility: calculating digit sums
    """

    def calculate_digit_sum(self, number: int) -> int:
        """
        Calculate the sum of all digits in a number.

        OOP CONCEPT: METHOD - Behavior associated with the class
        OOP CONCEPT: ABSTRACTION - Complex string manipulation hidden behind simple interface

        Args:
            number: The number to calculate digit sum for

        Returns:
            The sum of all digits in the number
        """
        # OOP CONCEPT: DATA VALIDATION AND TRANSFORMATION
        if number < 0:
            number = abs(number)  # Handle negative numbers by taking absolute value

        # Convert to string and sum each digit
        digit_sum = sum(int(digit) for digit in str(number))

        return digit_sum


# OOP CONCEPT: SEPARATION OF CONCERNS - Display logic in separate class
class ResultDisplay:
    """
    Handles output formatting and display of results.

    OOP CONCEPT: SINGLE RESPONSIBILITY PRINCIPLE
    This class has one clear responsibility: displaying results
    """

    def __init__(self):
        """
        Initialize the result display handler.

        OOP CONCEPT: CONSTRUCTOR - Initialize object with default state
        """
        # OOP CONCEPT: ENCAPSULATION - Private attributes for internal configuration
        self._title = "Factorial Digit Sum Calculator"
        self._separator = "=" * len(self._title)

    def display_header(self):
        """
        Display the application header.

        OOP CONCEPT: METHOD - Behavior encapsulated within the class
        """
        print(self._title)
        print(self._separator)
        print()

    def display_calculation_start(self, number: int):
        """
        Display message indicating calculation is starting.

        OOP CONCEPT: METHOD WITH PARAMETERS - Flexible behavior based on input

        Args:
            number: The number being calculated
        """
        print(f"Calculating {number}!...")

    def display_factorial_result(self, number: int, factorial: int):
        """
        Display the factorial result.

        OOP CONCEPT: METHOD - Encapsulated behavior for specific display task

        Args:
            number: The input number
            factorial: The calculated factorial
        """
        print(f"{number}! = {factorial}")
        print()

    def display_final_result(self, number: int, digit_sum: int):
        """
        Display the final digit sum result.

        OOP CONCEPT: METHOD - Specific behavior for final result display

        Args:
            number: The input number
            digit_sum: The calculated digit sum
        """
        print(f"Sum of digits in {number}!: {digit_sum}")


# OOP CONCEPT: MAIN ORCHESTRATOR CLASS - Coordinates other classes
class Application:
    """
    Main application orchestrator that coordinates all components.

    OOP CONCEPT: COMPOSITION - This class is composed of other classes
    OOP CONCEPT: SINGLE RESPONSIBILITY - Orchestrates the application flow
    """

    def __init__(self):
        """
        Initialize the application with its components.

        OOP CONCEPT: CONSTRUCTOR - Setting up object dependencies
        """
        # OOP CONCEPT: COMPOSITION - Creating instances of other classes
        # This class "has-a" relationship with other classes
        self._factorial_calculator = FactorialCalculator()
        self._digit_sum_calculator = DigitSumCalculator()
        self._result_display = ResultDisplay()

        # OOP CONCEPT: ENCAPSULATION - Private configuration data
        self._target_number = 100  # Hardcoded as per requirements

    def run(self):
        """
        Execute the main application logic.

        OOP CONCEPT: METHOD - Main behavior of the Application class
        OOP CONCEPT: ABSTRACTION - Complex workflow hidden behind simple interface
        OOP CONCEPT: COMPOSITION - Using other objects to accomplish tasks

        This method orchestrates the entire calculation process:
        1. Display header
        2. Calculate factorial
        3. Calculate digit sum
        4. Display results
        """
        try:
            # OOP CONCEPT: METHOD DELEGATION - Delegating tasks to appropriate objects
            # Display application header
            self._result_display.display_header()

            # Indicate calculation is starting
            self._result_display.display_calculation_start(self._target_number)

            # OOP CONCEPT: OBJECT COLLABORATION - Objects working together
            # Calculate factorial using the factorial calculator
            factorial_result = self._factorial_calculator.calculate_factorial(
                self._target_number
            )

            # Display factorial result
            self._result_display.display_factorial_result(
                self._target_number, factorial_result
            )

            # Calculate digit sum using the digit sum calculator
            digit_sum = self._digit_sum_calculator.calculate_digit_sum(factorial_result)

            # Display final result
            self._result_display.display_final_result(self._target_number, digit_sum)

        except Exception as e:
            # OOP CONCEPT: ERROR HANDLING - Protecting object state and providing feedback
            print(f"Error: {e}")
            return False

        return True


# OOP CONCEPT: PROCEDURAL INTERFACE - Simple function interface for object-oriented code
def main():
    """
    Main entry point for the application.

    OOP CONCEPT: OBJECT INSTANTIATION - Creating an instance of the Application class
    """
    # OOP CONCEPT: OBJECT CREATION AND METHOD INVOCATION
    app = Application()  # Create instance
    app.run()  # Call method on instance


if __name__ == "__main__":
    main()
