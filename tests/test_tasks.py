import sys
import os

from app.tasks import add_task, get_tasks

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")))

def test_add_task():
    add_task("learn Docker")
    assert "learn Docker" in get_tasks()
def test_multiple_tasks():
    add_task("learn CI")
    add_task("learn Devops")
    
    tasks=get_tasks()
    assert "learn CI" in tasks
    assert "learn Devops" in tasks