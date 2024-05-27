import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        self.root.configure(bg='green')


        self.tasks = []


        self.task_label = tk.Label(root, fg='black', text="Enter a task:")
        self.task_label.pack(pady=5)


        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=5)


        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)


        self.update_task_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_task_button.pack(pady=5)


        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)


        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)


        self.populate_tasks()


    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.populate_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")


    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.populate_tasks()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")


    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.populate_tasks()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")


    def populate_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()



