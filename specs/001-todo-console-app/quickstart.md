# Quickstart Guide: Todo In-Memory Python Console App

## Getting Started

1. Ensure you have Python 3.13+ installed on your system
2. Navigate to the project directory
3. Run the application with: `python -m src.main`

## Available Commands

### Add a Task
```
add "Task Title" "Task Description"
```
Example:
```
add "Buy groceries" "Milk, eggs, bread, vegetables"
```

### List All Tasks
```
list
```
Displays all tasks in a formatted table with ID, Status, Title, and Description.

### Update a Task
```
update <id> "New Title" "New Description"
```
Example:
```
update 1 "Buy weekly groceries" "Milk, eggs, bread, vegetables, fruits"
```

### Delete a Task
```
delete <id>
```
Example:
```
delete 1
```

### Toggle Task Status
```
toggle <id>
```
Toggles the completion status of a task between complete (✓) and incomplete (○).
Example:
```
toggle 1
```

### Get Help
```
help
```
Displays all available commands.

### Exit the Application
```
exit
```
or
```
quit
```

## Example Workflow

1. Add a task:
   ```
   add "Complete project" "Finish the todo console app implementation"
   ✓ Task added successfully with ID 1
   ```

2. List tasks:
   ```
   list
   ┌────┬────────┬──────────────────────┬─────────────────────────────────┐
   │ ID │ Status │ Title                │ Description                     │
   ├────┼────────┼──────────────────────┼─────────────────────────────────┤
   │ 1  │ ○      │ Complete project     │ Finish the todo console app    │
   └────┴────────┴──────────────────────┴─────────────────────────────────┘
   ```

3. Toggle task status:
   ```
   toggle 1
   ✓ Task status updated successfully
   ```

4. List tasks again to see the updated status:
   ```
   list
   ┌────┬────────┬──────────────────────┬─────────────────────────────────┐
   │ ID │ Status │ Title                │ Description                     │
   ├────┼────────┼──────────────────────┼─────────────────────────────────┤
   │ 1  │ ✓      │ Complete project     │ Finish the todo console app    │
   └────┴────────┴──────────────────────┴─────────────────────────────────┘
   ```

## Error Handling

The application provides clear error messages with ✗ indicators when something goes wrong:

- Invalid command: ✗ Unknown command. Type 'help' for available commands.
- Non-existent task ID: ✗ Task with ID 999 does not exist.
- Empty title: ✗ Task title cannot be empty.