"""
Factorial Digit Sum Calculator - SOLID Principles Implementation

This application calculates the factorial of 100 and then computes the sum of
all digits in the resulting factorial number. Demonstrates SOLID principles
including Single Responsibility, Open/Closed, Liskov Substitution, Interface
Segregation, and Dependency Inversion.

SOLID PRINCIPLES DEMONSTRATED:
- Single Responsibility: Each class has one reason to change
- Open/Closed: Classes are open for extension, closed for modification
- Liskov Substitution: Subclasses can replace base classes seamlessly
- Interface Segregation: Clients depend only on interfaces they use
- Dependency Inversion: High-level modules depend on abstractions, not concretions
"""

import math
from abc import ABC, abstractmethod


# SOLID: INTERFACE SEGREGATION PRINCIPLE
# Creating focused interfaces that clients actually need
class CalculatorInterface(ABC):
    """Interface for mathematical calculations."""

    @abstractmethod
    def calculate(self, number: int) -> int:
        """Calculate a mathematical operation on a number."""
        pass


# SOLID: INTERFACE SEGREGATION PRINCIPLE
# Separate interface for cacheable operations
class CacheableInterface(ABC):
    """Interface for operations that can be cached."""

    @abstractmethod
    def get_cached_result(self) -> tuple:
        """Get the last cached calculation result."""
        pass


# SOLID: INTERFACE SEGREGATION PRINCIPLE
# Dedicated interface for display operations
class DisplayInterface(ABC):
    """Interface for display operations."""

    @abstractmethod
    def display(self, content: str) -> None:
        """Display content to the user."""
        pass


# SOLID: INTERFACE SEGREGATION PRINCIPLE
# Specific interface for formatting operations
class FormatterInterface(ABC):
    """Interface for formatting operations."""

    @abstractmethod
    def format_header(self) -> str:
        """Format application header."""
        pass

    @abstractmethod
    def format_calculation_start(self, number: int) -> str:
        """Format calculation start message."""
        pass

    @abstractmethod
    def format_result(self, number: int, result: int) -> str:
        """Format calculation result."""
        pass


# SOLID: SINGLE RESPONSIBILITY PRINCIPLE
# This class has one responsibility: calculating factorials
class FactorialCalculator(CalculatorInterface, CacheableInterface):
    """
    Calculates factorial values with caching capability.

    SOLID: SINGLE RESPONSIBILITY - Only responsible for factorial calculations
    SOLID: INTERFACE SEGREGATION - Implements only needed interfaces
    """

    def __init__(self):
        self._cached_number = None
        self._cached_result = None

    # SOLID: LISKOV SUBSTITUTION PRINCIPLE
    # This implementation can substitute any CalculatorInterface
    def calculate(self, number: int) -> int:
        """
        Calculate factorial with validation and caching.

        SOLID: SINGLE RESPONSIBILITY - One method, one purpose
        """
        self._validate_input(number)

        if self._is_result_cached(number):
            return self._cached_result

        result = self._compute_factorial(number)
        self._cache_result(number, result)
        return result

    # SOLID: LISKOV SUBSTITUTION PRINCIPLE
    # This implementation can substitute any CacheableInterface
    def get_cached_result(self) -> tuple:
        """Return cached calculation data."""
        return self._cached_number, self._cached_result

    # SOLID: SINGLE RESPONSIBILITY PRINCIPLE
    # Each private method has one specific responsibility
    def _validate_input(self, number: int) -> None:
        """Validate input for factorial calculation."""
        if number < 0:
            raise ValueError("Factorial undefined for negative numbers")

    def _is_result_cached(self, number: int) -> bool:
        """Check if result is cached for given number."""
        return self._cached_number == number and self._cached_result is not None

    def _compute_factorial(self, number: int) -> int:
        """Compute factorial using standard library."""
        return math.factorial(number)

    def _cache_result(self, number: int, result: int) -> None:
        """Cache the calculation result."""
        self._cached_number = number
        self._cached_result = result


# SOLID: SINGLE RESPONSIBILITY PRINCIPLE
# This class has one responsibility: calculating digit sums
class DigitSumCalculator(CalculatorInterface):
    """
    Calculates sum of digits in a number.

    SOLID: SINGLE RESPONSIBILITY - Only responsible for digit sum calculations
    SOLID: LISKOV SUBSTITUTION - Can substitute any CalculatorInterface
    """

    def calculate(self, number: int) -> int:
        """
        Calculate sum of digits in a number.

        SOLID: SINGLE RESPONSIBILITY - One clear purpose
        """
        absolute_number = abs(number)
        return sum(int(digit) for digit in str(absolute_number))


# SOLID: SINGLE RESPONSIBILITY PRINCIPLE
# This class has one responsibility: console output
class ConsoleDisplay(DisplayInterface):
    """
    Handles console output operations.

    SOLID: SINGLE RESPONSIBILITY - Only responsible for console display
    SOLID: LISKOV SUBSTITUTION - Can substitute any DisplayInterface
    """

    def display(self, content: str) -> None:
        """Display content to console."""
        print(content)


# SOLID: SINGLE RESPONSIBILITY PRINCIPLE
# This class has one responsibility: formatting messages
class MessageFormatter(FormatterInterface):
    """
    Formats messages for display.

    SOLID: SINGLE RESPONSIBILITY - Only responsible for message formatting
    SOLID: OPEN/CLOSED PRINCIPLE - Can be extended without modification
    """

    def __init__(self, title: str):
        self._title = title
        self._separator = "=" * len(title)

    def format_header(self) -> str:
        """Format application header."""
        return f"{self._title}\n{self._separator}\n"

    def format_calculation_start(self, number: int) -> str:
        """Format calculation start message."""
        return f"Calculating {number}!..."

    def format_result(self, number: int, result: int) -> str:
        """Format calculation result."""
        return f"{number}! = {result}\n"


# SOLID: OPEN/CLOSED PRINCIPLE
# Extended formatter without modifying the base class
class ExtendedMessageFormatter(MessageFormatter):
    """
    Extended message formatter with additional formatting capabilities.

    SOLID: OPEN/CLOSED PRINCIPLE - Extends functionality without modifying parent
    SOLID: LISKOV SUBSTITUTION - Can substitute MessageFormatter
    """

    def format_digit_sum_result(self, number: int, digit_sum: int) -> str:
        """Format digit sum result message."""
        return f"Sum of digits in {number}!: {digit_sum}"


# SOLID: SINGLE RESPONSIBILITY PRINCIPLE
# This class has one responsibility: managing application workflow
class ApplicationOrchestrator:
    """
    Orchestrates the application workflow.

    SOLID: SINGLE RESPONSIBILITY - Only responsible for workflow coordination
    SOLID: DEPENDENCY INVERSION - Depends on abstractions, not concretions
    """

    def __init__(
        self,
        factorial_calculator: CalculatorInterface,
        digit_sum_calculator: CalculatorInterface,
        display: DisplayInterface,
        formatter: ExtendedMessageFormatter,
    ):
        """
        Initialize with dependencies.

        SOLID: DEPENDENCY INVERSION - Depends on abstractions (interfaces)
        SOLID: INTERFACE SEGREGATION - Only depends on needed interfaces
        """
        self._factorial_calculator = factorial_calculator
        self._digit_sum_calculator = digit_sum_calculator
        self._display = display
        self._formatter = formatter
        self._target_number = 100

    def run(self) -> bool:
        """
        Execute the application workflow.

        SOLID: SINGLE RESPONSIBILITY - One method, one workflow
        """
        try:
            self._display_header()
            self._display_calculation_start()
            factorial_result = self._calculate_factorial()
            self._display_factorial_result(factorial_result)
            digit_sum = self._calculate_digit_sum(factorial_result)
            self._display_digit_sum_result(digit_sum)
            return True
        except Exception as error:
            self._handle_error(error)
            return False

    # SOLID: SINGLE RESPONSIBILITY PRINCIPLE
    # Each method has one specific responsibility
    def _display_header(self) -> None:
        """Display application header."""
        header = self._formatter.format_header()
        self._display.display(header)

    def _display_calculation_start(self) -> None:
        """Display calculation start message."""
        start_message = self._formatter.format_calculation_start(self._target_number)
        self._display.display(start_message)

    def _calculate_factorial(self) -> int:
        """Calculate factorial using injected calculator."""
        return self._factorial_calculator.calculate(self._target_number)

    def _display_factorial_result(self, factorial_result: int) -> None:
        """Display factorial calculation result."""
        result_message = self._formatter.format_result(
            self._target_number, factorial_result
        )
        self._display.display(result_message)

    def _calculate_digit_sum(self, factorial_result: int) -> int:
        """Calculate digit sum using injected calculator."""
        return self._digit_sum_calculator.calculate(factorial_result)

    def _display_digit_sum_result(self, digit_sum: int) -> None:
        """Display digit sum calculation result."""
        digit_sum_message = self._formatter.format_digit_sum_result(
            self._target_number, digit_sum
        )
        self._display.display(digit_sum_message)

    def _handle_error(self, error: Exception) -> None:
        """Handle application errors."""
        error_message = f"Error: {error}"
        self._display.display(error_message)


# SOLID: DEPENDENCY INVERSION PRINCIPLE
# Factory creates concrete implementations but returns abstractions
class CalculatorFactory:
    """
    Factory for creating calculator instances.

    SOLID: SINGLE RESPONSIBILITY - Only responsible for creating calculators
    SOLID: DEPENDENCY INVERSION - Returns abstractions, not concretions
    """

    @staticmethod
    def create_factorial_calculator() -> CalculatorInterface:
        """Create factorial calculator instance."""
        return FactorialCalculator()

    @staticmethod
    def create_digit_sum_calculator() -> CalculatorInterface:
        """Create digit sum calculator instance."""
        return DigitSumCalculator()


# SOLID: DEPENDENCY INVERSION PRINCIPLE
# Factory for display-related components
class DisplayFactory:
    """
    Factory for creating display-related instances.

    SOLID: SINGLE RESPONSIBILITY - Only responsible for creating display components
    SOLID: DEPENDENCY INVERSION - Returns abstractions, not concretions
    """

    @staticmethod
    def create_console_display() -> DisplayInterface:
        """Create console display instance."""
        return ConsoleDisplay()

    @staticmethod
    def create_message_formatter() -> ExtendedMessageFormatter:
        """Create message formatter instance."""
        return ExtendedMessageFormatter("Factorial Digit Sum Calculator")


# SOLID: DEPENDENCY INVERSION PRINCIPLE
# High-level function depends on abstractions through dependency injection
def create_application() -> ApplicationOrchestrator:
    """
    Create application with all dependencies.

    SOLID: DEPENDENCY INVERSION - Assembles dependencies using abstractions
    SOLID: SINGLE RESPONSIBILITY - Only responsible for application assembly
    """
    # Create dependencies using factories
    factorial_calculator = CalculatorFactory.create_factorial_calculator()
    digit_sum_calculator = CalculatorFactory.create_digit_sum_calculator()
    display = DisplayFactory.create_console_display()
    formatter = DisplayFactory.create_message_formatter()

    # SOLID: DEPENDENCY INVERSION - Inject dependencies as abstractions
    return ApplicationOrchestrator(
        factorial_calculator=factorial_calculator,
        digit_sum_calculator=digit_sum_calculator,
        display=display,
        formatter=formatter,
    )


def main() -> None:
    """
    Application entry point.

    SOLID: DEPENDENCY INVERSION - Uses factory to create dependencies
    """
    application = create_application()
    application.run()


if __name__ == "__main__":
    main()
