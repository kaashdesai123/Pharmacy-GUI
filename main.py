import tkinter as tk
from tkinter import ttk, messagebox


class PharmacyApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Pharmacy Tracker")
        self.geometry("600x500")

        # Labels
        ttk.Label(self, text="Medication Name:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        ttk.Label(self, text="Type of Pill:").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        ttk.Label(self, text="Symptoms:").grid(row=2, column=0, pady=10, padx=10, sticky="w")

        # Entries
        self.med_name = tk.StringVar()
        ttk.Entry(self, textvariable=self.med_name).grid(row=0, column=1, pady=10, padx=10)

        self.pill_type = tk.StringVar()
        ttk.Entry(self, textvariable=self.pill_type).grid(row=1, column=1, pady=10, padx=10)

        self.symptoms = tk.StringVar()
        ttk.Entry(self, textvariable=self.symptoms).grid(row=2, column=1, pady=10, padx=10)

        # Button
        ttk.Button(self, text="Add Record", command=self.add_record).grid(row=3, column=0, columnspan=2, pady=20)

        # Listbox to display records
        self.records = ttk.Treeview(self, columns=("Medication", "Type", "Symptoms"), show="headings")
        self.records.heading("Medication", text="Medication Name")
        self.records.heading("Type", text="Type of Pill")
        self.records.heading("Symptoms", text="Symptoms")
        self.records.grid(row=4, column=0, columnspan=2, pady=20, padx=20)

    def add_record(self):
        medication = self.med_name.get()
        pill_type = self.pill_type.get()
        symptoms = self.symptoms.get()

        if medication and pill_type and symptoms:
            self.records.insert("", tk.END, values=(medication, pill_type, symptoms))
            self.med_name.set("")
            self.pill_type.set("")
            self.symptoms.set("")
        else:
            messagebox.showerror("Error", "All fields are required!")


if __name__ == "__main__":
    app = PharmacyApp()
    app.mainloop()
