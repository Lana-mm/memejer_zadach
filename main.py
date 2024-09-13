class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "Не выполнено"

    def mark_completed(self):
        self.status = "Выполнено"

    def __str__(self):
        return f"{self.description} (Срок: {self.deadline}) - {self.status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        self.tasks.append(Task(description, deadline))

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
        else:
            print("Задача с таким индексом не найдена.")

    def show_current_tasks(self):
        if not self.tasks:
            print("Нет текущих задач.")
            return

        print("Текущие задачи:")
        for index, task in enumerate(self.tasks):
            print(f"{index}. {task}")


if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\nМеню:\n1. Добавить задачу\n2. Показать текущие задачи\n3. Отметить задачу как выполненную\n4. Выйти")
        choice = input("Выберите действие (1-4): ")

        if choice == "1":
            description = input("Введите описание задачи: ")
            deadline = input("Введите срок выполнения задачи: ")
            manager.add_task(description, deadline)
        elif choice == "2":
            manager.show_current_tasks()
        elif choice == "3":
            task_index = int(input("Введите индекс задачи для отметки как выполненной: "))
            manager.mark_task_completed(task_index)
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")
