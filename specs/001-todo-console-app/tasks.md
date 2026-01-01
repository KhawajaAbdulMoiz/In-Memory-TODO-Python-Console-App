---

description: "Task list for Todo In-Memory Python Console App implementation"
---

# Todo In-Memory Python Console App – Phase I
## Task Breakdown v1.0

**Input**: Design documents from `/specs/001-todo-console-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan with src/ directory
- [ ] T002 [P] Initialize Python package with __init__.py files in src/
- [ ] T003 [P] Set up basic configuration and constants in src/config.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Create Task dataclass in src/models.py with id, title, description, completed fields
- [ ] T005 [P] Implement TodoManager class in src/todo_manager.py with in-memory storage
- [ ] T006 [P] Create utility functions for string truncation with ellipsis in src/utils.py
- [ ] T007 Create basic UI rendering functions in src/ui.py for welcome header and messages

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks with a title and description

**Independent Test**: Can add a task with title and description, see success message, and verify it has an auto-incrementing ID

### Implementation for User Story 1

- [ ] T008 [US1] Implement add_task method in src/todo_manager.py with validation
- [ ] T009 [US1] Create add command handler in src/commands.py
- [ ] T010 [US1] Add success/error message formatting in src/ui.py
- [ ] T011 [US1] Integrate add command with main loop in src/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - List/View Tasks (Priority: P2)

**Goal**: Display all tasks in a formatted table with ID, Status, Title, Description

**Independent Test**: Can list all tasks in a properly formatted table with appropriate column widths and truncation

### Implementation for User Story 2

- [ ] T012 [US2] Implement list_tasks method in src/todo_manager.py
- [ ] T013 [US2] Create table rendering function in src/ui.py with Unicode box characters
- [ ] T014 [US2] Add "no tasks" message handling in src/ui.py
- [ ] T015 [US2] Create list command handler in src/commands.py
- [ ] T016 [US2] Integrate list command with main loop in src/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Toggle Task Status (Priority: P3)

**Goal**: Allow users to toggle a task's status between complete/incomplete by ID

**Independent Test**: Can toggle a task's status by ID and see the change reflected in the list

### Implementation for User Story 3

- [ ] T017 [US3] Implement toggle_task_status method in src/todo_manager.py
- [ ] T018 [US3] Create toggle command handler in src/commands.py
- [ ] T019 [US3] Integrate toggle command with main loop in src/main.py

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task (Priority: P4)

**Goal**: Allow users to update the title and/or description of a task by its ID

**Independent Test**: Can update a task's title and/or description by ID and see the change reflected in the list

### Implementation for User Story 4

- [ ] T020 [US4] Implement update_task method in src/todo_manager.py
- [ ] T021 [US4] Create update command handler in src/commands.py
- [ ] T022 [US4] Integrate update command with main loop in src/main.py

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Task (Priority: P5)

**Goal**: Allow users to delete a task by its ID

**Independent Test**: Can delete a task by ID and verify it no longer appears in the list

### Implementation for User Story 5

- [ ] T023 [US5] Implement delete_task method in src/todo_manager.py
- [ ] T024 [US5] Create delete command handler in src/commands.py
- [ ] T025 [US5] Integrate delete command with main loop in src/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T026 [P] Implement command parsing and dispatching in src/commands.py
- [ ] T027 [P] Add help command functionality in src/commands.py and main loop
- [ ] T028 [P] Add quit/exit command functionality in src/commands.py and main loop
- [ ] T029 [P] Add comprehensive error handling and validation across all commands
- [ ] T030 [P] Implement proper application startup with welcome message in src/main.py
- [ ] T031 [P] Add ANSI color support (with fallback) for success/error messages in src/ui.py
- [ ] T032 [P] Code cleanup and refactoring
- [ ] T033 [P] Add docstrings and comments for all functions and classes
- [ ] T034 [P] Run quickstart.md validation to ensure all commands work as documented

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4 → P5)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints/commands
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement add_task method in src/todo_manager.py"
Task: "Create add command handler in src/commands.py"
Task: "Add success/error message formatting in src/ui.py"
Task: "Integrate add command with main loop in src/main.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Task)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence