"""
Core business logic for the Todo In-Memory Python Console App.
"""
from typing import Dict, List, Optional
from .models import Task


class TodoManager:
    """
    Manages the in-memory storage and operations for tasks.
    
    This class handles all CRUD operations for tasks, maintaining them in memory
    with auto-incrementing IDs starting from 1.
    """
    
    def __init__(self):
        """
        Initialize the TodoManager with an empty task storage and ID counter.
        """
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1
    
    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task with the given title and description.
        
        Args:
            title: The title of the task
            description: The description of the task (optional)
            
        Returns:
            The newly created Task object
            
        Raises:
            ValueError: If the title is empty or exceeds length limits
        """
        # Create a new task with the next available ID
        task = Task(id=self._next_id, title=title, description=description, completed=False)
        
        # Add the task to storage
        self._tasks[self._next_id] = task
        
        # Increment the ID counter for the next task
        self._next_id += 1
        
        return task
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The Task object if found, None otherwise
        """
        return self._tasks.get(task_id)
    
    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks.
        
        Returns:
            A list of all Task objects, sorted by ID
        """
        return sorted(self._tasks.values(), key=lambda task: task.id)
    
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update the title and/or description of a task by its ID.
        
        Args:
            task_id: The ID of the task to update
            title: The new title (optional)
            description: The new description (optional)
            
        Returns:
            True if the task was updated, False if the task ID doesn't exist
        """
        if task_id not in self._tasks:
            return False
        
        task = self._tasks[task_id]
        
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
            
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            True if the task was deleted, False if the task ID doesn't exist
        """
        if task_id not in self._tasks:
            return False
        
        del self._tasks[task_id]
        return True
    
    def toggle_task_status(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task by its ID.
        
        Args:
            task_id: The ID of the task to toggle
            
        Returns:
            True if the task status was toggled, False if the task ID doesn't exist
        """
        if task_id not in self._tasks:
            return False
        
        task = self._tasks[task_id]
        task.completed = not task.completed
        return True