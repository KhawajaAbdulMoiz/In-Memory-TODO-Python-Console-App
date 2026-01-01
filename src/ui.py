"""
Console presentation layer for the Todo In-Memory Python Console App.
"""
from typing import List
from .models import Task
from .config import BOX_CHARS, COLORS, STATUS_SYMBOLS, TABLE_MIN_WIDTHS
from .utils import truncate_string


def print_welcome_header():
    """
    Print the welcome header and command hints on startup.
    """
    print(f"\n{BOX_CHARS['top_left']}{BOX_CHARS['horizontal'] * 50}{BOX_CHARS['top_right']}")
    print(f"{BOX_CHARS['vertical']} {COLORS['success']}Todo In-Memory Python Console App{COLORS['reset']} {' ' * 14}{BOX_CHARS['vertical']}")
    print(f"{BOX_CHARS['vertical']} Version 1.0.0 - Manage your tasks in memory      {BOX_CHARS['vertical']}")
    print(f"{BOX_CHARS['bottom_left']}{BOX_CHARS['horizontal'] * 50}{BOX_CHARS['bottom_right']}")
    print("\nAvailable commands:")
    print("  add \"title\" \"description\"    - Add a new task")
    print("  list                        - List all tasks")
    print("  update <id> \"title\" \"desc\"  - Update a task")
    print("  delete <id>                 - Delete a task")
    print("  toggle <id>                 - Toggle task status")
    print("  help                        - Show this help")
    print("  quit/exit                   - Exit the app")
    print()


def print_success_message(message: str):
    """
    Print a success message with emoji indicator.
    
    Args:
        message: The success message to print
    """
    print(f"✓ {message}")


def print_error_message(message: str):
    """
    Print an error message with emoji indicator.
    
    Args:
        message: The error message to print
    """
    print(f"✗ {message}")


def print_task_table(tasks: List[Task]):
    """
    Print all tasks in a formatted table with Unicode box characters.
    
    Args:
        tasks: List of Task objects to display
    """
    if not tasks:
        print("\nNo tasks found. Add some tasks to get started!")
        return

    # Define column widths based on minimums and content
    id_width = max(TABLE_MIN_WIDTHS['id'], len('ID'))
    status_width = max(TABLE_MIN_WIDTHS['status'], len('Status'))
    title_width = max(TABLE_MIN_WIDTHS['title'], len('Title'))
    desc_width = max(TABLE_MIN_WIDTHS['description'], len('Description'))
    
    # Calculate actual widths based on content if needed
    for task in tasks:
        id_width = max(id_width, len(str(task.id)))
        title_width = max(title_width, len(truncate_string(task.title, title_width)))
        desc_width = max(desc_width, len(truncate_string(task.description, desc_width)))
    
    # Ensure minimum widths
    id_width = max(id_width, TABLE_MIN_WIDTHS['id'])
    status_width = max(status_width, TABLE_MIN_WIDTHS['status'])
    title_width = max(title_width, TABLE_MIN_WIDTHS['title'])
    desc_width = max(desc_width, TABLE_MIN_WIDTHS['description'])
    
    # Calculate total width
    total_width = id_width + status_width + title_width + desc_width + 9  # 9 for separators and padding
    
    # Print table header
    print(f"\n{BOX_CHARS['top_left']}{BOX_CHARS['horizontal'] * (id_width + 2)}{BOX_CHARS['top_cross']}"
          f"{BOX_CHARS['horizontal'] * (status_width + 2)}{BOX_CHARS['top_cross']}"
          f"{BOX_CHARS['horizontal'] * (title_width + 2)}{BOX_CHARS['top_cross']}"
          f"{BOX_CHARS['horizontal'] * (desc_width + 2)}{BOX_CHARS['top_right']}")
    
    print(f"{BOX_CHARS['vertical']} {'ID':>{id_width}} {BOX_CHARS['vertical']} {'Status':^{status_width}} "
          f"{BOX_CHARS['vertical']} {'Title':<{title_width}} {BOX_CHARS['vertical']} {'Description':<{desc_width}} "
          f"{BOX_CHARS['vertical']}")
    
    print(f"{BOX_CHARS['left_cross']}{BOX_CHARS['horizontal'] * (id_width + 2)}{BOX_CHARS['cross']}"
          f"{BOX_CHARS['horizontal'] * (status_width + 2)}{BOX_CHARS['cross']}"
          f"{BOX_CHARS['horizontal'] * (title_width + 2)}{BOX_CHARS['cross']}"
          f"{BOX_CHARS['horizontal'] * (desc_width + 2)}{BOX_CHARS['right_cross']}")
    
    # Print task rows
    for task in tasks:
        status = STATUS_SYMBOLS['complete'] if task.completed else STATUS_SYMBOLS['incomplete']
        title = truncate_string(task.title, title_width)
        description = truncate_string(task.description, desc_width)
        
        print(f"{BOX_CHARS['vertical']} {task.id:>{id_width}} {BOX_CHARS['vertical']} {status:^{status_width}} "
              f"{BOX_CHARS['vertical']} {title:<{title_width}} {BOX_CHARS['vertical']} {description:<{desc_width}} "
              f"{BOX_CHARS['vertical']}")
    
    # Print table footer
    print(f"{BOX_CHARS['bottom_left']}{BOX_CHARS['horizontal'] * (id_width + 2)}{BOX_CHARS['bottom_cross']}"
          f"{BOX_CHARS['horizontal'] * (status_width + 2)}{BOX_CHARS['bottom_cross']}"
          f"{BOX_CHARS['horizontal'] * (title_width + 2)}{BOX_CHARS['bottom_cross']}"
          f"{BOX_CHARS['horizontal'] * (desc_width + 2)}{BOX_CHARS['bottom_right']}")