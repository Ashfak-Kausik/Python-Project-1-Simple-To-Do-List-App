import tkinter as tk

# Function to add task
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

# Function to delete selected task
def delete_task():
    listbox.delete(tk.ANCHOR)

# GUI setup
root = tk.Tk()
root.title("To-Do List App")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()
