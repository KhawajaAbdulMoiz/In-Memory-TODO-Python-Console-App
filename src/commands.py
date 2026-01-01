"""
Command parsing and handling for the Todo In-Memory Python Console App.
"""
import re
from typing import Tuple, Optional
from .todo_manager import TodoManager


class CommandHandler:
    """
    Handles parsing and execution of user commands.
    """
    
    def __init__(self, todo_manager: TodoManager):
        """
        Initialize the command handler with a TodoManager instance.
        
        Args:
            todo_manager: The TodoManager instance to use for operations
        """
        self.todo_manager = todo_manager
    
    def parse_command(self, user_input: str) -> Tuple[str, list]:
        """
        Parse the user input into a command and its arguments.
        
        Args:
            user_input: The raw user input string
            
        Returns:
            A tuple containing the command name and a list of arguments
        """
        # Remove leading/trailing whitespace
        user_input = user_input.strip()
        
        # Handle commands with quoted arguments
        # This regex finds quoted strings or individual words
        pattern = r'"([^"]*)"|\'([^\']*)\'|(\S+)'
        matches = re.findall(pattern, user_input)
        
        # Each match is a tuple of (double_quoted, single_quoted, unquoted)
        # We extract the non-empty part from each tuple
        parts = [match[0] or match[1] or match[2] for match in matches]
        
        if not parts:
            return "help", []
        
        command = parts[0].lower()
        args = parts[1:]
        
        return command, args
    
    def execute_command(self, command: str, args: list) -> bool:
        """
        Execute a command with the given arguments.
        
        Args:
            command: The command to execute
            args: The arguments for the command
            
        Returns:
            True if the command should continue the app, False to exit
        """
        if command == "add":
            return self._handle_add(args)
        elif command == "list":
            return self._handle_list(args)
        elif command == "update":
            return self._handle_update(args)
        elif command == "delete":
            return self._handle_delete(args)
        elif command == "toggle":
            return self._handle_toggle(args)
        elif command == "help":
            return self._handle_help(args)
        elif command in ["quit", "exit"]:
            return self._handle_exit(args)
        else:
            print(f"✗ Unknown command: {command}. Type 'help' for available commands.")
            return True  # Continue running
    
    def _handle_add(self, args: list) -> bool:
        """
        Handle the 'add' command.
        
        Args:
            args: Arguments for the add command [title, description]
        """
        if len(args) < 1:
            print("✗ Usage: add \"title\" \"description\" (description is optional)")
            return True
        
        title = args[0]
        description = args[1] if len(args) > 1 else ""
        
        try:
            task = self.todo_manager.add_task(title, description)
            print(f"✓ Task added successfully with ID {task.id}")
        except ValueError as e:
            print(f"✗ Error adding task: {e}")
        
        return True  # Continue running
    
    def _handle_list(self, args: list) -> bool:
        """
        Handle the 'list' command.
        
        Args:
            args: Arguments for the list command (none expected)
        """
        if args:
            print("✗ Usage: list (no arguments required)")
            return True
        
        tasks = self.todo_manager.get_all_tasks()
        from .ui import print_task_table
        print_task_table(tasks)
        
        return True  # Continue running
    
    def _handle_update(self, args: list) -> bool:
        """
        Handle the 'update' command.
        
        Args:
            args: Arguments for the update command [id, title, description]
        """
        if len(args) < 2:
            print("✗ Usage: update <id> \"title\" \"description\" (title and/or description required)")
            return True
        
        try:
            task_id = int(args[0])
        except ValueError:
            print("✗ Task ID must be a number")
            return True
        
        title = args[1] if len(args) > 1 else None
        description = args[2] if len(args) > 2 else None
        
        # If both title and description are None or empty, use current values
        if title is None or title == "":
            title = None
        if description is None or description == "":
            description = None
        
        success = self.todo_manager.update_task(task_id, title, description)
        if success:
            print(f"✓ Task {task_id} updated successfully")
        else:
            print(f"✗ Task with ID {task_id} does not exist")
        
        return True  # Continue running
    
    def _handle_delete(self, args: list) -> bool:
        """
        Handle the 'delete' command.
        
        Args:
            args: Arguments for the delete command [id]
        """
        if len(args) != 1:
            print("✗ Usage: delete <id>")
            return True
        
        try:
            task_id = int(args[0])
        except ValueError:
            print("✗ Task ID must be a number")
            return True
        
        success = self.todo_manager.delete_task(task_id)
        if success:
            print(f"✓ Task {task_id} deleted successfully")
        else:
            print(f"✗ Task with ID {task_id} does not exist")
        
        return True  # Continue running
    
    def _handle_toggle(self, args: list) -> bool:
        """
        Handle the 'toggle' command.
        
        Args:
            args: Arguments for the toggle command [id]
        """
        if len(args) != 1:
            print("✗ Usage: toggle <id>")
            return True
        
        try:
            task_id = int(args[0])
        except ValueError:
            print("✗ Task ID must be a number")
            return True
        
        success = self.todo_manager.toggle_task_status(task_id)
        if success:
            print(f"✓ Task {task_id} status toggled successfully")
        else:
            print(f"✗ Task with ID {task_id} does not exist")
        
        return True  # Continue running
    
    def _handle_help(self, args: list) -> bool:
        """
        Handle the 'help' command.
        
        Args:
            args: Arguments for the help command (none expected)
        """
        if args:
            print("✗ Usage: help (no arguments required)")
            return True
        
        from .ui import print_welcome_header
        print_welcome_header()
        return True  # Continue running
    
    def _handle_exit(self, args: list) -> bool:
        """
        Handle the 'exit' or 'quit' command.
        
        Args:
            args: Arguments for the exit command (none expected)
        """
        if args:
            print("✗ Usage: exit or quit (no arguments required)")
            return True
        
        print("Goodbye!")
        return False  # Stop running