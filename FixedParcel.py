import tkinter as tk
from tkinter import messagebox


class Parcel:
    def __init__(self, height, width, length, weight, cost, signature, tracking):
        self.height = height
        self.width = width
        self.length = length
        self.weight = weight
        self.cost = cost
        self.signature = signature
        self.tracking = tracking

    def __str__(self):
        return f"Size: {self.height}x{self.width}x{self.length} cm, Weight: {self.weight} kg, Cost: £{self.cost:.2f}, Signature: {self.signature}, Tracking: {self.tracking}"


class ParcelOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Parcel Order System")
        self.root.geometry("600x550")
        self.parcels = []
        self.create_layout()

    def create_layout(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Customer Details", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2)

        tk.Label(frame, text="Name:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(frame, text="Address:").grid(row=2, column=0, sticky="e", padx=5, pady=2)
        self.address_entry = tk.Entry(frame)
        self.address_entry.grid(row=2, column=1, padx=5, pady=2)

        tk.Label(frame, text="Phone Number:").grid(row=3, column=0, sticky="e", padx=5, pady=2)
        self.phone_entry = tk.Entry(frame)
        self.phone_entry.grid(row=3, column=1, padx=5, pady=2)

        tk.Label(frame, text="Parcel Height (cm):").grid(row=4, column=0, sticky="e", padx=5, pady=2)
        self.height_entry = tk.Entry(frame)
        self.height_entry.grid(row=4, column=1, padx=5, pady=2)

        tk.Label(frame, text="Parcel Width (cm):").grid(row=5, column=0, sticky="e", padx=5, pady=2)
        self.width_entry = tk.Entry(frame)
        self.width_entry.grid(row=5, column=1, padx=5, pady=2)

        tk.Label(frame, text="Parcel Length (cm):").grid(row=6, column=0, sticky="e", padx=5, pady=2)
        self.length_entry = tk.Entry(frame)
        self.length_entry.grid(row=6, column=1, padx=5, pady=2)

        tk.Label(frame, text="Parcel Weight (kg):").grid(row=7, column=0, sticky="e", padx=5, pady=2)
        self.weight_entry = tk.Entry(frame)
        self.weight_entry.grid(row=7, column=1, padx=5, pady=2)

        tk.Label(frame, text="Signature? (£2.00)").grid(row=8, column=0, sticky="e", padx=5, pady=2)
        self.signature_var = tk.StringVar(value="N")
        tk.OptionMenu(frame, self.signature_var, "Y", "N").grid(row=8, column=1, padx=5, pady=2)

        tk.Label(frame, text="Tracking? (£5.00)").grid(row=9, column=0, sticky="e", padx=5, pady=2)
        self.tracking_var = tk.StringVar(value="N")
        tk.OptionMenu(frame, self.tracking_var, "Y", "N").grid(row=9, column=1, padx=5, pady=2)

        tk.Button(frame, text="Add Parcel", command=self.add_parcel).grid(row=10, column=0, columnspan=2, pady=5)
        tk.Button(frame, text="Remove Last Parcel", command=self.remove_last_parcel).grid(row=11, column=0,
                                                                                          columnspan=2, pady=5)
        tk.Button(frame, text="Finish Order", command=self.display_receipt).grid(row=12, column=0, columnspan=2,
                                                                                 pady=10)

    def add_parcel(self):
        if len(self.parcels) >= 6:
            messagebox.showerror("Error", "Cannot add more than 6 parcels per order.")
            return

        try:
            height, width, length, weight = float(self.height_entry.get()), float(self.width_entry.get()), float(
                self.length_entry.get()), float(self.weight_entry.get())
            size = height + width + length

            if size > 450 or weight > 30:
                messagebox.showerror("Error", "Parcels over 450 cm or 30 kg cannot be collected.")
                return

            if size <= 95 and weight <= 2:
                cost = 5.00
            elif size <= 150 and weight <= 15:
                cost = 20.00
            elif size <= 450 and weight <= 30:
                cost = 30.00
            else:
                messagebox.showerror("Error", "Invalid parcel dimensions.")
                return

            if self.signature_var.get() == "Y":
                cost += 2.00
            if self.tracking_var.get() == "Y":
                cost += 5.00

            self.parcels.append(
                Parcel(height, width, length, weight, cost, self.signature_var.get(), self.tracking_var.get()))
            messagebox.showinfo("Success", "Parcel added to order!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

    def remove_last_parcel(self):
        if self.parcels:
            self.parcels.pop()
            messagebox.showinfo("Success", "Last parcel removed!")
        else:
            messagebox.showerror("Error", "No parcels to remove.")

    def display_receipt(self):
        name, address, phone = self.name_entry.get(), self.address_entry.get(), self.phone_entry.get()
        if not name or not address or not phone.replace(" ", "").isdigit() or len(phone.replace(" ", "")) not in [10,
                                                                                                                  11]:
            messagebox.showerror("Error", "Please enter valid customer details.")
            return
        if not self.parcels:
            messagebox.showerror("Error", "Please add at least one parcel before finishing the order.")
            return

        total_cost = sum(parcel.cost for parcel in self.parcels)
        receipt = f"Customer: {name}\nAddress: {address}\nPhone: {phone}\n\nOrder Summary:\n" + "\n".join(
            [f"Parcel {i + 1}: {p}" for i, p in enumerate(self.parcels)]) + f"\nTotal Cost: £{total_cost:.2f}"
        messagebox.showinfo("Order Receipt", receipt)


if __name__ == "__main__":
    root = tk.Tk()
    app = ParcelOrderApp(root)
    root.mainloop()
