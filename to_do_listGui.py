import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("مدیریت وظایف")
        self.tasks = []

        self.label = tk.Label(root, text="برنامه مدیریت وظایف پایتون", font=("Arial", 14))
        self.label.pack(pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        self.add_button = tk.Button(root, text="➕ اضافه کردن وظیفه", command=self.add_task)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="❌ حذف وظیفه", command=self.remove_task)
        self.remove_button.pack()

        self.complete_button = tk.Button(root, text="✅ علامت‌گذاری کامل‌شده", command=self.mark_completed)
        self.complete_button.pack()

    def add_task(self):
        task_name = self.entry.get().strip()
        if task_name:
            self.tasks.append({"name": task_name, "completed": False})
            self.update_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("هشدار", "نام وظیفه نمی‌تواند خالی باشد.")

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.tasks.pop(selected[0])
            self.update_task_list()
        else:
            messagebox.showwarning("هشدار", "لطفاً یک وظیفه را انتخاب کنید.")

    def mark_completed(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.tasks[selected[0]]["completed"] = True
            self.update_task_list()
        else:
            messagebox.showwarning("هشدار", "لطفاً یک وظیفه را انتخاب کنید.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✅" if task["completed"] else "⏳"
            self.task_listbox.insert(tk.END, f"{task['name']} - {status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerGUI(root)
    root.mainloop()
