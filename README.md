# Todo Console Application

A simple command-line todo application built with Python as part of Hackathon II: Spec-Driven Development.

## Overview

This application allows users to manage their tasks through a console interface. All tasks are stored in memory and will be lost when the application exits.

## Features

- Add new tasks with titles and optional descriptions
- View all tasks with their completion status
- Update existing tasks
- Delete tasks
- Mark tasks as complete or incomplete

## Requirements

- Python 3.13+ 
- No external dependencies (uses only Python standard library)

## Setup

1. Clone or download this repository
2. Navigate to the project directory
3. Run the application using Python:

```bash
cd src
python main.py
```

## Usage

The application provides a menu-driven interface:

1. **Add Task**: Create a new task with a title and optional description
2. **View All Tasks**: Display all tasks with their ID, status, title, and description
3. **Update Task**: Modify the title or description of an existing task
4. **Delete Task**: Remove a task from the list
5. **Mark Task as Complete/Incomplete**: Toggle the completion status of a task
6. **Exit**: Close the application

## Project Structure

```
src/
├── main.py              # Entry point and main application loop
├── models/
│   └── task.py          # Task model definition
├── managers/
│   └── task_manager.py  # Task management logic
└── ui/
    └── cli.py           # Command-line interface
```

## Architecture

This application follows a simple layered architecture:
- **User Interface Layer**: Command-line interface for user interaction
- **Business Logic Layer**: Task management operations
- **Data Management Layer**: In-memory storage for tasks

## Development

This project was developed using Spec-Driven Development methodology with the following artifacts:
- `speckit.constitution` - Project principles
- `speckit.specify` - Requirements specification
- `speckit.plan` - Technical architecture
- `speckit.tasks` - Implementation tasks