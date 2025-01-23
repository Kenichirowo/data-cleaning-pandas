import re
import pandas as pd
import numpy as np


def clean_sex(value):
    if pd.isna(value): # making sure that function is not crashing when facing NaN
        return value
    elif str(value).strip() in ["M", "F"]:  # Keep valid entries
        return str(value).strip()
    else:
        return "Unknown"  # Replace others with 'Unknown'


def replace_with_average(age_str):
    """
    Replaces a range of numbers (e.g., "x and y", "x to y", "x & y", etc.)
    in a given string with their average. If no match is found, the input string is returned unchanged.

    Args:
        age_str (str): The input string containing the age range.

    Returns:
        float or str: The average of the two numbers if a range is detected,
                      otherwise the original input string.
    """
    age_str = str(age_str)
    match = re.match(r'(\d+)\s*(?:and|or|to|&|/)\s*(\d+)', age_str)

    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        average = (num1 + num2) / 2
        return average
    return age_str


def clean_age(age_str):
    """
    Cleans and processes an age string by extracting numeric values, including handling fractions like "½".
    Returns the average of all extracted numbers.

    Args:
        age_str (str): The input string containing age information.

    Returns:
        float or None: The average of all numeric values extracted from the string,
                       or None if no valid numbers are found.
    """
    age_str = str(age_str).strip()
    match = re.findall(r'\d+\.?\d*|\d+½', age_str)

    if match:
        processed_numbers = []
        for num in match:
            if '½' in num:
                num = num.replace('½', '.5')  # Converts "6½" to "6.5"
            processed_numbers.append(float(num))
        if processed_numbers:
            return sum(processed_numbers) / len(processed_numbers)


def extract_numbers(value):
    """
    Extracts the first numeric value from a string, rounds it to the nearest integer,
    and returns it. If no numbers are found, it returns NaN.

    Args:
        value (str): The input string containing numeric information.

    Returns:
        int or float: The first number in the string rounded to the nearest integer,
                      or NaN if no valid number is found.
    """
    value = str(value).strip()
    numbers = re.findall(r'\d+(?:\.\d+)?', value)

    if numbers:
        return int(round(float(numbers[0])))
    return np.nan
    