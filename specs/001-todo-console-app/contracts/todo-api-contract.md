# Todo Console App API Contract

## Command Interface

### Add Task
- **Command**: `add "title" "description"`
- **Input**: Title (string), Description (string)
- **Output**: Success message with task ID or error message
- **Error Cases**: 
  - Empty title
  - System error

### List Tasks
- **Command**: `list`
- **Input**: None
- **Output**: Table of all tasks or "no tasks" message
- **Error Cases**: None

### Update Task
- **Command**: `update <id> "title" "description"`
- **Input**: Task ID (integer), new title (string), new description (string)
- **Output**: Success message or error message
- **Error Cases**:
  - Invalid ID
  - Non-existent task
  - Empty title

### Delete Task
- **Command**: `delete <id>`
- **Input**: Task ID (integer)
- **Output**: Success message or error message
- **Error Cases**:
  - Invalid ID
  - Non-existent task

### Toggle Task Status
- **Command**: `toggle <id>`
- **Input**: Task ID (integer)
- **Output**: Success message or error message
- **Error Cases**:
  - Invalid ID
  - Non-existent task

### Help
- **Command**: `help`
- **Input**: None
- **Output**: List of available commands
- **Error Cases**: None

### Exit
- **Command**: `exit` or `quit`
- **Input**: None
- **Output**: Exit message
- **Error Cases**: None