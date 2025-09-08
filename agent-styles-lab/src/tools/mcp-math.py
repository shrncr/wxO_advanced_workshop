# basic import 
from fastmcp import FastMCP
import math

# instantiate an MCP server client
mcp = FastMCP("Math Tools")

# DEFINE TOOLS - INTEGER VERSIONS

#addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return int(a + b)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return int(a * b)

#  division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    return float(a / b)

# power tool
@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    return int(a ** b)

# square root tool
@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    return float(a ** 0.5)

# cube root tool
@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    return float(a ** (1/3))

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """factorial of a number"""
    return int(math.factorial(a))

# log tool
@mcp.tool()
def log(a: int) -> float:
    """log of a number"""
    return float(math.log(a))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """remainder of two numbers divison"""
    return int(a % b)

# sin tool
@mcp.tool()
def sin(a: int) -> float:
    """sin of a number"""
    return float(math.sin(a))

# cos tool
@mcp.tool()
def cos(a: int) -> float:
    """cos of a number"""
    return float(math.cos(a))

# tan tool
@mcp.tool()
def tan(a: int) -> float:
    """tan of a number"""
    return float(math.tan(a))

# DEFINE TOOLS - DECIMAL/FLOAT VERSIONS

# addition tool for decimals
@mcp.tool()
def add_decimal(a: float, b: float) -> float:
    """Add two decimal numbers"""
    return float(a + b)

# subtraction tool for decimals
@mcp.tool()
def subtract_decimal(a: float, b: float) -> float:
    """Subtract two decimal numbers"""
    return float(a - b)

# multiplication tool for decimals
@mcp.tool()
def multiply_decimal(a: float, b: float) -> float:
    """Multiply two decimal numbers"""
    return float(a * b)

# division tool for decimals
@mcp.tool() 
def divide_decimal(a: float, b: float) -> float:
    """Divide two decimal numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return float(a / b)

# power tool for decimals
@mcp.tool()
def power_decimal(a: float, b: float) -> float:
    """Power of two decimal numbers"""
    return float(a ** b)

# square root tool for decimals
@mcp.tool()
def sqrt_decimal(a: float) -> float:
    """Square root of a decimal number"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return float(math.sqrt(a))

# cube root tool for decimals
@mcp.tool()
def cbrt_decimal(a: float) -> float:
    """Cube root of a decimal number"""
    return float(a ** (1/3))

# nth root tool for decimals
@mcp.tool()
def nth_root_decimal(a: float, n: float) -> float:
    """Calculate the nth root of a decimal number"""
    if n == 0:
        raise ValueError("Root cannot be zero")
    return float(a ** (1/n))

# logarithm tool for decimals (natural log)
@mcp.tool()
def log_decimal(a: float) -> float:
    """Natural logarithm of a decimal number"""
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    return float(math.log(a))

# logarithm base 10 for decimals
@mcp.tool()
def log10_decimal(a: float) -> float:
    """Base-10 logarithm of a decimal number"""
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    return float(math.log10(a))

# logarithm with custom base for decimals
@mcp.tool()
def log_base_decimal(a: float, base: float) -> float:
    """Logarithm of a decimal number with custom base"""
    if a <= 0 or base <= 0 or base == 1:
        raise ValueError("Invalid input for logarithm")
    return float(math.log(a) / math.log(base))

# modulo/remainder tool for decimals
@mcp.tool()
def remainder_decimal(a: float, b: float) -> float:
    """Remainder of two decimal numbers division (modulo)"""
    if b == 0:
        raise ValueError("Cannot calculate remainder with zero divisor")
    return float(a % b)

# sin tool for decimals
@mcp.tool()
def sin_decimal(a: float) -> float:
    """Sine of a decimal number (in radians)"""
    return float(math.sin(a))

# cos tool for decimals
@mcp.tool()
def cos_decimal(a: float) -> float:
    """Cosine of a decimal number (in radians)"""
    return float(math.cos(a))

# tan tool for decimals
@mcp.tool()
def tan_decimal(a: float) -> float:
    """Tangent of a decimal number (in radians)"""
    return float(math.tan(a))

# sin tool for decimals in degrees
@mcp.tool()
def sin_degrees(a: float) -> float:
    """Sine of a decimal number (in degrees)"""
    return float(math.sin(math.radians(a)))

# cos tool for decimals in degrees
@mcp.tool()
def cos_degrees(a: float) -> float:
    """Cosine of a decimal number (in degrees)"""
    return float(math.cos(math.radians(a)))

# tan tool for decimals in degrees
@mcp.tool()
def tan_degrees(a: float) -> float:
    """Tangent of a decimal number (in degrees)"""
    return float(math.tan(math.radians(a)))

# inverse trigonometric functions for decimals
@mcp.tool()
def asin_decimal(a: float) -> float:
    """Arcsine of a decimal number (returns radians)"""
    if not -1 <= a <= 1:
        raise ValueError("Arcsine domain is [-1, 1]")
    return float(math.asin(a))

@mcp.tool()
def acos_decimal(a: float) -> float:
    """Arccosine of a decimal number (returns radians)"""
    if not -1 <= a <= 1:
        raise ValueError("Arccosine domain is [-1, 1]")
    return float(math.acos(a))

@mcp.tool()
def atan_decimal(a: float) -> float:
    """Arctangent of a decimal number (returns radians)"""
    return float(math.atan(a))

# hyperbolic functions for decimals
@mcp.tool()
def sinh_decimal(a: float) -> float:
    """Hyperbolic sine of a decimal number"""
    return float(math.sinh(a))

@mcp.tool()
def cosh_decimal(a: float) -> float:
    """Hyperbolic cosine of a decimal number"""
    return float(math.cosh(a))

@mcp.tool()
def tanh_decimal(a: float) -> float:
    """Hyperbolic tangent of a decimal number"""
    return float(math.tanh(a))

# absolute value for decimals
@mcp.tool()
def abs_decimal(a: float) -> float:
    """Absolute value of a decimal number"""
    return float(abs(a))

# rounding functions for decimals
@mcp.tool()
def round_decimal(a: float, decimals: int = 0) -> float:
    """Round a decimal number to specified decimal places"""
    return float(round(a, decimals))

@mcp.tool()
def floor_decimal(a: float) -> float:
    """Floor of a decimal number"""
    return float(math.floor(a))

@mcp.tool()
def ceil_decimal(a: float) -> float:
    """Ceiling of a decimal number"""
    return float(math.ceil(a))

# exponential function for decimals
@mcp.tool()
def exp_decimal(a: float) -> float:
    """Exponential function (e^x) of a decimal number"""
    return float(math.exp(a))

# DEFINE RESOURCES

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
    
 
 # execute and return the stdio output
if __name__ == "__main__":
   mcp.run()
   #mcp.run(transport="stdio")
   #mcp.run(transport="https", host="0.0.0.0", port=4050)