import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("500x560")
        self.root.resizable(False, False)

        self.tasks = []
        self.editing_index = None

        self.header_label = tk.Label(root, text="My Tasks", font=("Arial", 18, "bold"))
        self.header_label.pack(pady=(16, 8))

        entry_frame = tk.Frame(root)
        entry_frame.pack(fill=tk.X, padx=12)

        self.task_entry = tk.Entry(entry_frame, font=("Arial", 14), width=30)
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.priority_var = tk.StringVar(value="Medium")
        self.priority_menu = tk.OptionMenu(entry_frame, self.priority_var, "Low", "Medium", "High")
        self.priority_menu.pack(side=tk.RIGHT, padx=(8, 0))

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.add_button = tk.Button(button_frame, text="Add Task", command=self.add_task, width=12)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.edit_button = tk.Button(button_frame, text="Edit Task", command=self.edit_task, width=12)
        self.edit_button.grid(row=0, column=1, padx=5, pady=5)

        self.toggle_button = tk.Button(button_frame, text="Toggle Done", command=self.toggle_task_done, width=12)
        self.toggle_button.grid(row=1, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, width=12)
        self.delete_button.grid(row=1, column=1, padx=5, pady=5)

        self.clear_done_button = tk.Button(root, text="Clear Completed", command=self.clear_completed, width=18)
        self.clear_done_button.pack(pady=(0, 10))

        self.task_listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE, height=15, activestyle="none")
        self.task_listbox.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 10))
        self.task_listbox.bind("<<ListboxSelect>>", self.on_select)
        self.task_listbox.bind("<Double-Button-1>", self.toggle_task_done)

        self.status_var = tk.StringVar(value="Ready")
        self.status_label = tk.Label(root, textvariable=self.status_var, font=("Arial", 10), fg="gray")
        self.status_label.pack(pady=(0, 12))

        self.refresh_listbox()
        self.task_entry.focus_set()

    def _task_text(self, task):
        icon = "✅" if task["done"] else "☐"
        priority = task.get("priority", "Medium")
        return f"{icon} [{priority}] {task['title']}"

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, self._task_text(task))
        self.status_var.set(f"{len(self.tasks)} task(s) total")

    def _get_selected_index(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task first.")
            return None
        return selected[0]

    def add_task(self):
        task_title = self.task_entry.get().strip()
        task_priority = self.priority_var.get()

        if self.editing_index is not None:
            if task_title == "":
                messagebox.showwarning("Warning", "Task cannot be empty.")
                return
            if len(task_title) >= 50:
                messagebox.showwarning("Warning", "Task must be less than 50 characters.")
                return

            self.tasks[self.editing_index]["title"] = task_title
            self.tasks[self.editing_index]["priority"] = task_priority
            self.editing_index = None
            self.add_button.config(text="Add Task")
            self.status_var.set("Task updated")
        else:
            if task_title == "":
                messagebox.showwarning("Warning", "You must enter a task.")
                return
            if len(task_title) >= 50:
                messagebox.showwarning("Warning", "Task must be less than 50 characters.")
                return

            self.tasks.append({"title": task_title, "done": False, "priority": task_priority})
            self.status_var.set("Task added")

        self.task_entry.delete(0, tk.END)
        self.priority_var.set("Medium")
        self.refresh_listbox()
        self.task_entry.focus_set()

    def edit_task(self):
        index = self._get_selected_index()
        if index is None:
            return

        task = self.tasks[index]
        self.editing_index = index
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(0, task["title"])
        self.priority_var.set(task.get("priority", "Medium"))
        self.add_button.config(text="Save Changes")
        self.status_var.set("Editing selected task")
        self.task_entry.focus_set()

    def toggle_task_done(self, event=None):
        index = self._get_selected_index()
        if index is None:
            return

        self.tasks[index]["done"] = not self.tasks[index]["done"]
        self.refresh_listbox()
        self.task_listbox.selection_set(index)
        self.status_var.set("Task marked as done" if self.tasks[index]["done"] else "Task reopened")

    def delete_task(self):
        index = self._get_selected_index()
        if index is None:
            return

        del self.tasks[index]
        self.refresh_listbox()
        self.status_var.set("Task deleted")

    def clear_completed(self):
        self.tasks = [task for task in self.tasks if not task["done"]]
        self.refresh_listbox()
        self.status_var.set("Completed tasks removed")

    def on_select(self, event=None):
        if not self.task_listbox.curselection():
            return
        self.status_var.set(f"Selected item {self.task_listbox.curselection()[0] + 1}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()