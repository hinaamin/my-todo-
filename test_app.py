"""
Simple test script to verify the todo application components work correctly
"""

import sys
import os
# Add the src directory to the path so we can import modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from models.task import Task
from managers.task_manager import TaskManager

def test_task_creation():
    """Test that we can create a task correctly"""
    print("Testing Task creation...")
    try:
        task = Task(1, "Test Task", "Test Description", False)
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed == False
        print("[PASS] Task creation works correctly")
    except Exception as e:
        print(f"[FAIL] Task creation failed: {e}")
        return False
    return True

def test_task_manager():
    """Test that the TaskManager works correctly"""
    print("\nTesting TaskManager...")
    try:
        tm = TaskManager()

        # Test adding a task
        task = tm.add_task("Test Task", "Test Description")
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed == False
        print("[PASS] TaskManager.add_task works correctly")

        # Test getting all tasks
        tasks = tm.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].id == 1
        print("[PASS] TaskManager.get_all_tasks works correctly")

        # Test getting task by ID
        retrieved_task = tm.get_task_by_id(1)
        assert retrieved_task is not None
        assert retrieved_task.id == 1
        print("[PASS] TaskManager.get_task_by_id works correctly")

        # Test updating task
        updated_task = tm.update_task(1, "Updated Task", "Updated Description")
        assert updated_task is not None
        assert updated_task.title == "Updated Task"
        assert updated_task.description == "Updated Description"
        print("[PASS] TaskManager.update_task works correctly")

        # Test toggling completion
        toggled_task = tm.toggle_task_completion(1)
        assert toggled_task is not None
        assert toggled_task.completed == True
        print("[PASS] TaskManager.toggle_task_completion works correctly")

        # Test deleting task
        success = tm.delete_task(1)
        assert success == True
        tasks_after_delete = tm.get_all_tasks()
        assert len(tasks_after_delete) == 0
        print("[PASS] TaskManager.delete_task works correctly")

        print("[PASS] All TaskManager operations work correctly")
    except Exception as e:
        print(f"[FAIL] TaskManager test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    return True

def main():
    """Run all tests"""
    print("Running tests for Todo Console Application...")

    success = True
    success &= test_task_creation()
    success &= test_task_manager()

    if success:
        print("\n[SUCCESS] All tests passed! The application components are working correctly.")
    else:
        print("\n[FAILURE] Some tests failed.")

    return success

if __name__ == "__main__":
    main()