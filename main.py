class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False  # По умолчанию задача не выполнена

    def mark_as_done(self):
        self.status = True  # Отметить задачу как выполненную

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        self.tasks.append(Task(description, deadline))

    def mark_task_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_done()

    def current_tasks(self):
        return [task.description for task in self.tasks if not task.status]

# Пример использования
manager = TaskManager()
manager.add_task("Позвонить клиенту", "2023-04-15")
manager.add_task("Отправить отчет", "2023-04-20")
print(manager.current_tasks())  # Выведет список текущих задач
manager.mark_task_done("Позвонить клиенту")
print(manager.current_tasks())  # Выведет обновленный список задач

