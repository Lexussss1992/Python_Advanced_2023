from task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.completed_task = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.tasks}'
        else:
            self.tasks.append(new_task)

            return f'Task {new_task} is added to the section'

    def complete_task(self, task_name):
        if task_name not in self.tasks:
            return f'Could not find task with the name {task_name}'
        else:
            task.completed = True

            self.completed_task.append(task_name)

            return f'Completed task {task_name}'

    def clean_section(self):

        removed_tasks = len(self.completed_task)
        self.completed_task.clear()

        return f'Cleared {removed_tasks} tasks.'

    def view_section(self):
        print(self.tasks)
        return f'{self.name}'


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())