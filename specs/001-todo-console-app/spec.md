# Todo In-Memory Python Console App – Phase I
## Specification v1.0

### 1. Project Overview

The Todo In-Memory Python Console App is a command-line application that allows users to manage their tasks in a simple, efficient manner. The application stores all data in memory with no persistence to files or databases, focusing on core functionality and user experience. The app provides a clean, intuitive command-line interface with table-formatted output for easy task management.

### 2. Functional Requirements

#### 2.1 Core Features

**FR-001: Add Task**
- System MUST allow users to add a new task with a title and description
- System MUST assign an auto-incrementing integer ID starting from 1 to each new task
- System MUST set the initial status of the task to "incomplete"
- System MUST display a success message with emoji indicator (✓) when task is added successfully
- System MUST display an error message with emoji indicator (✗) if task addition fails

**FR-002: List/View All Tasks**
- System MUST display all tasks in a table format with columns: ID | Status | Title | Description
- System MUST use Unicode box characters or clean ASCII for table formatting
- System MUST truncate long titles and descriptions with ellipsis (...) to maintain readability
- System MUST display a friendly "no tasks" message when the list is empty
- System MUST show the status as either "✓" for complete or "○" for incomplete

**FR-003: Update Task**
- System MUST allow users to update the title and/or description of a task by its ID
- System MUST validate that the provided ID exists before attempting update
- System MUST display a success message with emoji indicator (✓) when task is updated successfully
- System MUST display an error message with emoji indicator (✗) if the task ID doesn't exist or update fails

**FR-004: Delete Task**
- System MUST allow users to delete a task by its ID
- System MUST validate that the provided ID exists before attempting deletion
- System MUST display a success message with emoji indicator (✓) when task is deleted successfully
- System MUST display an error message with emoji indicator (✗) if the task ID doesn't exist or deletion fails

**FR-005: Toggle Task Status**
- System MUST allow users to toggle a task's status between complete/incomplete by its ID
- System MUST validate that the provided ID exists before attempting status change
- System MUST display a success message with emoji indicator (✓) when status is toggled successfully
- System MUST display an error message with emoji indicator (✗) if the task ID doesn't exist or status change fails

#### 2.2 Command Interface & Syntax

**Command Syntax:**
- `add "task title" "task description"` - Add a new task
- `list` - Display all tasks in table format
- `update <id> "new title" "new description"` - Update task details (title and/or description)
- `delete <id>` - Delete task by ID
- `toggle <id>` - Toggle task status between complete/incomplete
- `help` - Show available commands
- `quit` or `exit` - Exit the application

#### 2.3 Expected Output Formats

**Table Format:**
```
┌────┬────────┬──────────────────────┬─────────────────────────────────┐
│ ID │ Status │ Title                │ Description                     │
├────┼────────┼──────────────────────┼─────────────────────────────────┤
│ 1  │ ○      │ Buy groceries        │ Milk, eggs, bread, vegetables  │
│ 2  │ ✓      │ Complete project     │ Finish the todo console app    │
└────┴────────┴──────────────────────┴─────────────────────────────────┘
```

**Column Specifications:**
- ID: Right-aligned, minimum 3 characters width
- Status: Centered, 6 characters width, showing "○" for incomplete and "✓" for complete
- Title: Left-aligned, maximum 20 characters with ellipsis (...) for truncation
- Description: Left-aligned, maximum 25 characters with ellipsis (...) for truncation

**Success/Error Messages:**
- Success: ✓ [Action completed successfully] (e.g., ✓ Task added successfully)
- Error: ✗ [Error description] (e.g., ✗ Task with ID 5 does not exist)

### 3. Data Model & Storage

- All data MUST be stored in-memory only (no files, no database, no persistence)
- Tasks MUST be stored as objects with the following properties:
  - id: integer (auto-incrementing starting from 1)
  - title: string
  - description: string
  - completed: boolean (default: false)
- The application MUST maintain an in-memory collection of tasks that persists for the duration of the session

### 4. Non-Functional Requirements

#### 4.1 Technical Stack & Constraints
- Application MUST be written in Python 3.13+
- Application MUST use only Python standard library modules (zero external dependencies)
- Application MUST run in a console/terminal environment
- Application MUST be compatible with Windows, macOS, and Linux operating systems

#### 4.2 Code Quality & Style Guidelines
- Code MUST adhere to PEP 8 style guidelines
- Functions and classes MUST include appropriate docstrings
- Variable and function names MUST be descriptive and follow Python naming conventions
- Code MUST be organized into logical modules (e.g., models, services, cli)

#### 4.3 Error Handling & User Experience
- Application MUST provide clear, user-friendly error messages
- Application MUST handle invalid user inputs gracefully
- Application MUST validate task IDs before performing operations
- Application MUST provide helpful feedback for all user actions
- Application MUST include a welcome header and command hint on startup

### 5. User Stories

- As a user, I want to add tasks with a title and description so that I can keep track of what I need to do
- As a user, I want to view all my tasks in a clear table format so that I can easily see what needs to be done
- As a user, I want to update task details by ID so that I can modify my tasks as needed
- As a user, I want to delete tasks by ID so that I can remove completed or unnecessary tasks
- As a user, I want to mark tasks as complete/incomplete so that I can track my progress

### 6. Acceptance Criteria

**For Add Task:**
- Given I am on the main screen, when I enter "add 'Buy groceries' 'Milk, eggs, bread'", then the task should be added with ID 1 and status incomplete, and a success message should be displayed

**For List Tasks:**
- Given I have added tasks, when I enter "list", then all tasks should be displayed in the specified table format
- Given I have no tasks, when I enter "list", then a friendly "no tasks" message should be displayed

**For Update Task:**
- Given I have a task with ID 1, when I enter "update 1 'Buy weekly groceries' 'Milk, eggs, bread, vegetables'", then the task should be updated and a success message should be displayed
- Given I enter an invalid ID, when I enter "update 999 'title' 'description'", then an error message should be displayed

**For Delete Task:**
- Given I have a task with ID 1, when I enter "delete 1", then the task should be removed and a success message should be displayed
- Given I enter an invalid ID, when I enter "delete 999", then an error message should be displayed

**For Toggle Task:**
- Given I have an incomplete task with ID 1, when I enter "toggle 1", then the task status should change to complete and a success message should be displayed
- Given I enter an invalid ID, when I enter "toggle 999", then an error message should be displayed

### 7. Explicitly Out of Scope for Phase I

- Data persistence (saving to files, databases, or cloud storage)
- User authentication or multiple user accounts
- Task categories, tags, or filtering
- Task due dates or reminders
- Import/export functionality
- Web interface or GUI
- Mobile application
- Network synchronization
- Advanced search capabilities

### 8. Recommended In-Memory Data Structure

- Use a Python list to store task objects
- Each task object should be a dictionary or class instance with id, title, description, and completed properties
- Maintain a counter for the next available ID that increments with each new task
- Use the ID as the primary identifier for all operations (update, delete, toggle)

### 9. Notes for Next Steps (plan generation)

- The implementation should follow a layered architecture (models, services, CLI interface)
- Consider using Python's built-in `dataclasses` for task representation
- For table formatting, consider using string formatting with calculated column widths
- The CLI loop should handle user input, command parsing, and result display
- Error handling should be consistent across all operations
- Consider creating a TaskManager class to encapsulate all task operations