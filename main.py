
import tkinter as tk
import threading
import time
from win11toast import toast

INTERVAL = 60  # 1 minute

class WaterReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💧 Water Reminder")
        self.root.geometry("300x120")
        self.root.resizable(False, False)

        self.running = False

        self.label = tk.Label(root, text="Water Reminder App", font=("Arial", 14))
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Reminder", width=20, command=self.start_reminder)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Reminder", width=20, command=self.stop_reminder, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

    def start_reminder(self):
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        threading.Thread(target=self.reminder_loop, daemon=True).start()

    def stop_reminder(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def reminder_loop(self):
        while self.running:
            toast(
                title="💧 Drink Water Reminder",
                body="Time to drink water! Stay hydrated 😊",
                duration="short"
            )

            for _ in range(INTERVAL):
                if not self.running:
                    return
                time.sleep(1)


if __name__ == "__main__":
    root = tk.Tk()
    app = WaterReminderApp(root)
    root.mainloop()
