"""
Utility functions for the Todo In-Memory Python Console App.
"""


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum length, adding a suffix if truncated.
    
    Args:
        text: The string to truncate
        max_length: The maximum length of the string
        suffix: The suffix to add if the string is truncated (default: "...")
        
    Returns:
        The truncated string with suffix if it was too long
    """
    if len(text) <= max_length:
        return text
    
    # Make sure the suffix fits within the max length
    if len(suffix) >= max_length:
        return suffix[:max_length]
    
    return text[:max_length - len(suffix)] + suffix


def safe_string(text: str) -> str:
    """
    Ensure a string is safe for display by handling None and empty values.
    
    Args:
        text: The string to make safe
        
    Returns:
        A safe string representation
    """
    if text is None:
        return ""
    return str(text)