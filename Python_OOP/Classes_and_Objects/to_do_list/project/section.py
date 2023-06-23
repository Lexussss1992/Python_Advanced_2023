from project import task
from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section{self.name}"

        else:
            self.tasks.append(new_task)

            return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in self.completed_tasks:
            return f"Could not find task with the name {task_name}"
        else:
            task.completed = True
            self.completed_tasks.append(task_name)
            return f"Completed task {task_name}"

    def clean_section(self):
        amount_of_removed_tasks = len(self.completed_tasks)
        self.completed_tasks.clear()

        return f"Cleared {amount_of_removed_tasks} tasks."

    def view_section(self):

        result = [f"Section {self.name}:"]
        [result.append(f"{s.details()}") for s in self.tasks]

        return "\n".join(result)