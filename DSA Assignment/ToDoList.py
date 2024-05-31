class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def is_completed(self):
        return self.completed

    def mark_completed(self):
        self.completed = True


class Node:
    def __init__(self, task):
        self.task = task
        self.next = None


class ToDoList:
    def __init__(self):
        self.head = None

    def add_todo(self, task):
        new_node = Node(task)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def mark_todo_as_completed(self, title):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current:
            if current.task.get_title() == title:
                current.task.mark_completed()
                print("Task '" + title + "' marked as completed.")
                return
            current = current.next
        print("Task '" + title + "' not found.")

    def view_todo_list(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        print("To-Do List:")
        while current:
            completion_status = "Completed" if current.task.is_completed() else "Pending"
            print("- " + completion_status + " : " + current.task.get_title())
            current = current.next
todo_list = ToDoList()
todo_list.add_todo(Task("Buy groceries", "Milk, bread, eggs"))
todo_list.add_todo(Task("Finish report", "Due tomorrow"))

todo_list.view_todo_list()  

todo_list.mark_todo_as_completed("Buy groceries")
todo_list.view_todo_list()  