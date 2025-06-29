# class_static_methods_demo.py

class Calculator:
    """
    A simple Calculator class demonstrating static methods and class methods.
    """
    # Class attribute referenced by the class method
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: Returns the sum of two numbers.
        It does not require access to the class or instance.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: Returns the product of two numbers.
        It takes 'cls' as the first argument, allowing it to access
        class-level attributes like 'calculation_type'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

