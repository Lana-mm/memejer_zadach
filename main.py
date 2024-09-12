class TaskManager:
    def __init__(self):
        self.tasks = []
        print("Менеджер задач инициализирован.")

    class Task:
        def __init__(self, description, due_date):
            self.description = description
            self.due_date = due_date
            self.completed = False

        def mark_completed(self):
            self.completed = True
            print(f"Задача '{self.description}' отмечена как выполненная.")

        def __str__(self):
            status = "Выполнено" if self.completed else "Не выполнено"
            return f"{self.description} (Срок: {self.due_date}) - {status}"

    def add_task(self, description, due_date):
        new_task = self.Task(description, due_date)
        self.tasks.append(new_task)
        print(f"Добавлена новая задача: '{description}' с сроком: {due_date}.")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
        else:
            print("Задача с таким индексом не найдена.")

    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if current_tasks:
            print("Текущие задачи:")
            for index, task in enumerate(current_tasks):
                print(f"{index}. {task}")
        else:
            print("Нет текущих задач.")

