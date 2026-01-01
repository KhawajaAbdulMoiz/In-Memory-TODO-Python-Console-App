"""
Main entry point for the Todo In-Memory Python Console App.
"""
from .todo_manager import TodoManager
from .commands import CommandHandler
from .ui import print_welcome_header


def main():
    """
    Main application loop for the Todo In-Memory Python Console App.
    """
    print_welcome_header()
    
    # Initialize the application components
    todo_manager = TodoManager()
    command_handler = CommandHandler(todo_manager)
    
    # Main application loop
    running = True
    while running:
        try:
            # Get user input
            user_input = input("> ").strip()
            
            # If input is empty, continue the loop
            if not user_input:
                continue
            
            # Parse and execute the command
            command, args = command_handler.parse_command(user_input)
            running = command_handler.execute_command(command, args)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except EOFError:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()