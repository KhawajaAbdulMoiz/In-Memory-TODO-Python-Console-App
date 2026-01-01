"""
Configuration and constants for the Todo In-Memory Python Console App.
"""

# Application constants
APP_NAME = "Todo In-Memory Python Console App"
APP_VERSION = "1.0.0"

# Table formatting constants
TABLE_MIN_WIDTHS = {
    'id': 3,
    'status': 6,
    'title': 20,
    'description': 25
}

# Maximum lengths for truncation
MAX_TITLE_LENGTH = 200
MAX_DESCRIPTION_LENGTH = 500

# Unicode box-drawing characters for table borders
BOX_CHARS = {
    'horizontal': '─',
    'vertical': '│',
    'top_left': '┌',
    'top_right': '┐',
    'bottom_left': '└',
    'bottom_right': '┘',
    'cross': '┼',
    'top_cross': '┬',
    'bottom_cross': '┴',
    'left_cross': '├',
    'right_cross': '┤'
}

# ANSI color codes (optional, with fallback to plain text)
COLORS = {
    'success': '\033[92m',  # Green
    'error': '\033[91m',    # Red
    'reset': '\033[0m'      # Reset
}

# Status symbols
STATUS_SYMBOLS = {
    'complete': '✓',
    'incomplete': '○'
}