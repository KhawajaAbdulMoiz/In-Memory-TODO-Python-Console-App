# Research: Todo In-Memory Python Console App

## Decision: Data Structure for Task Storage
- **Rationale**: Using Python dataclass for Task model provides clean, readable code with automatic generation of special methods like __init__ and __repr__. For in-memory storage, a dictionary with task IDs as keys provides O(1) lookup time.
- **Alternatives considered**: 
  - NamedTuple: Immutable, but tasks need to be updated
  - Regular class: More verbose than necessary
  - List of tasks: O(n) lookup time for operations by ID

## Decision: Table Rendering Approach
- **Rationale**: Using string formatting with Unicode box-drawing characters provides a clean, professional look across different terminals that support Unicode. This approach is implementable with Python's built-in string methods.
- **Alternatives considered**:
  - External libraries (e.g., tabulate): Would violate zero-dependency constraint
  - ASCII-only borders: Less visually appealing
  - Dynamic column sizing: More complex implementation

## Decision: Command Parsing Strategy
- **Rationale**: Simple string splitting with validation provides a good balance between functionality and simplicity. It handles the required command syntax without complex parsing libraries.
- **Alternatives considered**:
  - Regular expressions: More complex than needed
  - argparse module: Designed for CLI arguments, not interactive commands
  - Third-party parsing libraries: Would violate zero-dependency constraint

## Decision: ANSI Color Support
- **Rationale**: Implementing optional ANSI color support with fallback to plain text provides enhanced UX where supported while maintaining compatibility with all terminals.
- **Alternatives considered**:
  - Always use colors: Could appear as gibberish on terminals without ANSI support
  - Never use colors: Misses opportunity to enhance UX
  - External color libraries: Would violate zero-dependency constraint

## Decision: Input Validation Approach
- **Rationale**: Comprehensive validation at the command level prevents invalid data from entering the system and provides clear feedback to users.
- **Alternatives considered**:
  - Minimal validation: Could lead to inconsistent data
  - Validation only at storage level: Less clear feedback to users