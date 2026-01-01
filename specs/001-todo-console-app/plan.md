# Todo In-Memory Python Console App – Phase I
## Implementation Plan v1.0

### 1. Overall Architecture & Module Breakdown

The application will follow a clean, layered architecture with clear separation of concerns:

- **main.py**: Entry point and main application loop
- **models.py**: Data models (Task class/dataclass)
- **todo_manager.py**: Core business logic (CRUD operations, state management)
- **ui.py**: Console presentation layer (table rendering, messages, formatting)
- **commands.py**: Command parsing and dispatching logic
- **utils.py**: Helper functions (input validation, string formatting)

### 2. Main Data Structures

**Task Data Model**:
- Use a Python dataclass for clean, readable code:
  - id: int (auto-incrementing)
  - title: str
  - description: str
  - completed: bool (default: False)

**In-Memory Storage**:
- Use a dictionary with task IDs as keys for O(1) lookups
- Maintain a separate counter for the next available ID

### 3. Key Components / Layers

- **Data management**: Task dataclass and in-memory storage (todo_manager.py)
- **Command parsing & dispatching**: Parse user input and route to appropriate handlers (commands.py)
- **Business logic (CRUD + toggle)**: Add, list, update, delete, and toggle task status (todo_manager.py)
- **Console presentation / rendering**: Table formatting, messages, and UI elements (ui.py)
- **Main application loop**: Input handling, command execution, and application flow (main.py)

### 4. File Structure Proposal

```
src/
├── __init__.py
├── main.py               # entry point + main loop
├── models.py             # Task dataclass
├── todo_manager.py       # core data & business logic
├── ui.py                 # console rendering (tables, messages, header)
├── commands.py           # command parsing & handlers
└── utils.py              # utility functions
```

### 5. Detailed Feature Implementation Outline

**Add Task**:
- Function: `add_task(title: str, description: str) -> bool`
- Input validation: Ensure title is not empty
- Edge cases: Handle empty strings, very long inputs
- Side effects: Increment ID counter, add to storage, print success message

**List Tasks**:
- Function: `list_tasks() -> None`
- Input validation: None needed
- Edge cases: Handle empty task list
- Side effects: Print formatted table to console

**Update Task**:
- Function: `update_task(task_id: int, title: str = None, description: str = None) -> bool`
- Input validation: Ensure task exists, validate ID
- Edge cases: Invalid ID, empty title
- Side effects: Update task in storage, print success/error message

**Delete Task**:
- Function: `delete_task(task_id: int) -> bool`
- Input validation: Ensure task exists, validate ID
- Edge cases: Invalid ID
- Side effects: Remove from storage, print success/error message

**Toggle Task**:
- Function: `toggle_task_status(task_id: int) -> bool`
- Input validation: Ensure task exists, validate ID
- Edge cases: Invalid ID
- Side effects: Update task status, print success/error message

### 6. Console UX & Formatting Strategy

**Table Rendering**:
- Use string formatting with calculated column widths
- Implement a helper function to draw Unicode box-drawing characters
- Columns: ID (3 chars), Status (6 chars), Title (20 chars), Description (25 chars)
- Truncate long text with ellipsis (...) using string slicing

**Message Style**:
- Success: ✓ [message] (green if ANSI supported)
- Error: ✗ [message] (red if ANSI supported)
- Welcome: Display app name and command hints on startup

**Input Prompt**:
- Use a simple `> ` prompt for commands
- Parse commands using string splitting and validation

### 7. Error Handling & User Feedback Strategy

- Implement comprehensive input validation
- Provide clear error messages for invalid commands or IDs
- Handle edge cases gracefully (empty lists, invalid inputs)
- Use try-catch blocks where appropriate
- Implement command validation to handle typos

### 8. Development Sequence Recommendation

1. **Core data structure + basic manager class** (models.py, todo_manager.py basics)
2. **Console rendering utilities** (ui.py - table drawing, messages)
3. **Command parser / dispatcher** (commands.py - basic parsing)
4. **Individual command implementations** (add → list → toggle → update → delete)
5. **Main loop + startup/shutdown** (main.py - complete loop)
6. **Polish** (help command, better messages, edge cases)

### 9. Technical Decisions & Trade-offs

- **Data structure**: Use dataclass for Task model (clean, readable, Pythonic)
- **Table drawing**: Unicode box-drawing characters for better appearance
- **ANSI support**: Optional (implement with fallback to plain text)
- **Text truncation**: Implement helper function to truncate with ellipsis
- **Command syntax**: Simple string parsing with validation

### 10. Risks & Watch-outs

- **String parsing**: Be careful with parsing commands that contain quotes
- **ID management**: Ensure ID counter is properly maintained
- **Memory management**: Since everything is in-memory, ensure efficient storage
- **Input validation**: Handle all edge cases to prevent crashes
- **Unicode rendering**: Test table rendering on different terminals