# Data Model: Todo In-Memory Python Console App

## Task Entity

### Properties
- **id**: integer
  - Auto-incrementing identifier starting from 1
  - Primary key for the task
  - Required field
- **title**: string
  - Title of the task
  - Required field
  - Maximum length: 200 characters
- **description**: string
  - Detailed description of the task
  - Optional field (can be empty)
  - Maximum length: 500 characters
- **completed**: boolean
  - Status of the task
  - Default value: False
  - Required field

### Validation Rules
- **id**: Must be a positive integer
- **title**: Must not be empty or contain only whitespace
- **description**: Optional, but if provided must not exceed 500 characters
- **completed**: Must be a boolean value

### State Transitions
- **Incomplete to Complete**: When toggle command is executed on an incomplete task
- **Complete to Incomplete**: When toggle command is executed on a complete task

## In-Memory Storage Structure

### Task Storage
- **Type**: Dictionary (dict)
- **Key**: Task ID (integer)
- **Value**: Task object (dataclass instance)
- **Purpose**: Provide O(1) lookup time for task operations by ID

### ID Counter
- **Type**: Integer
- **Initial Value**: 1
- **Purpose**: Track the next available ID for new tasks
- **Behavior**: Incremented each time a new task is added