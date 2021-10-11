import pytest
from pmgr.project import TaskException, Project
@pytest.fixture(scope="function")

def proj():
    item1 = Project("Do the dishes")
    yield item1
    item1.delete()

def test_get_tasks_none(proj):
    assert [] == proj.get_tasks()

def test_get_tasks_one(proj):
    proj.add_task("clean the spoon")
    assert "clean the spoon" in proj.get_tasks()

def test_get_tasks_many(proj):
    proj.add_task("clean the spoon")
    proj.add_task("clean the knife")
    assert "clean the spoon" in proj.get_tasks()
    assert "clean the knife" in proj.get_tasks()

def test_add_task_new(proj):
    proj.add_task("clean the spoon")
    assert "clean the spoon" in proj.get_tasks()

def test_add_multiple_tasks(proj):
    proj.add_task("clean the spoon")
    proj.add_task("clean the knife")
    assert "clean the spoon" in proj.get_tasks()
    assert "clean the knife" in proj.get_tasks()

def test_add_prexisting(proj):
    proj.add_task("clean the spoon")
    with pytest.raises(TaskException):
        proj.add_task("clean the spoon")

def test_remove_prexisting(proj): 
    proj.add_task("clean the spoon")
    proj.remove_task("clean the spoon")
    assert "clean the spoon" not in proj.get_tasks()

def test_remove_nonexisting(proj):
    proj.add_task("clean the spoon")
    with pytest.raises(TaskException):
        proj.remove_task("clean the knife")

def test_remove_multiple_tasks(proj): 
    proj.add_task("clean the spoon")
    proj.add_task("clean the knife")
    proj.remove_task("clean the spoon")
    proj.remove_task("clean the knife")
    assert "clean the spoon" not in proj.get_tasks()
    assert "clean the knife" not in proj.get_tasks()
