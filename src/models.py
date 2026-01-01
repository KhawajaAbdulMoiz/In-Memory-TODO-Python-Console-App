"""
Data models for the Todo In-Memory Python Console App.
"""
from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents a single task in the todo list.
    
    Attributes:
        id: Unique identifier for the task (auto-incrementing)
        title: Title of the task (required)
        description: Detailed description of the task (optional)
        completed: Status of the task (True for complete, False for incomplete)
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False

    def __post_init__(self):
        """
        Validate the task after initialization.
        """
        if not self.title.strip():
            raise ValueError("Task title cannot be empty")
        if len(self.title) > 200:
            raise ValueError("Task title cannot exceed 200 characters")
        if len(self.description) > 500:
            raise ValueError("Task description cannot exceed 500 characters")