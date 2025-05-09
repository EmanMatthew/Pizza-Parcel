import tkinter as tk
from tkinter import messagebox

class Pizza:
    def __init__(self, size, toppings, total_cost):
        self.size = size
        self.toppings = toppings
        self.total_cost = total_cost

    def __str__(self):
        return f"Size: {self.size}, Toppings: {', '.join(self.toppings)}, Cost: £{self.total_cost:.2f}"

class MargheritaPizza(Pizza):
    def __init__(self, size, topping_count=0):
        base_toppings = ["Garlic", "Sliced mozzarella", "Basil", "Extra virgin oil"]
        base_prices = {"S": 3.25, "M": 5.50, "L": 7.15}
        topping_prices = [0, 0.75, 1.35, 2.00, 2.50]
        total_cost = base_prices[size] + topping_prices[topping_count]
        toppings = base_toppings + [f"Extra x{topping_count}"] if topping_count else base_toppings
        super().__init__(size, toppings, total_cost)

class PepperoniPizza(Pizza):
    def __init__(self, size, topping_count=0):
        base_toppings = ["Pepperoni", "Mozzarella"]
        base_prices = {"S": 3.25, "M": 5.50, "L": 7.15}
        topping_prices = [0, 0.75, 1.35, 2.00, 2.50]
        total_cost = base_prices[size] + topping_prices[topping_count]
        toppings = base_toppings + [f"Extra x{topping_count}"] if topping_count else base_toppings
        super().__init__(size, toppings, total_cost)

class HamAndPineapplePizza(Pizza):
    def __init__(self, size, topping_count=0):
        base_toppings = ["Mozzarella", "Ham", "Pineapple"]
        base_prices = {"S": 3.25, "M": 5.50, "L": 7.15}
        topping_prices = [0, 0.75, 1.35, 2.00, 2.50]
        total_cost = base_prices[size] + topping_prices[topping_count]
        toppings = base_toppings + [f"Extra x{topping_count}"] if topping_count else base_toppings
        super().__init__(size, toppings, total_cost)

class PizzaOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Order System")
        self.root.geometry("500x600")

        self.pizzas = []
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

        tk.Label(frame, text="Pizza Type:").grid(row=4, column=0, sticky="e", padx=5, pady=2)
        self.pizza_type_var = tk.StringVar(value="Custom")
        type_menu = tk.OptionMenu(frame, self.pizza_type_var, "Custom", "Margherita Pizza", "Pepperoni Pizza", "Ham & Pineapple Pizza", command=self.toggle_custom_fields)
        type_menu.grid(row=4, column=1, padx=5, pady=2)

        tk.Label(frame, text="Select Size:").grid(row=5, column=0, sticky="e", padx=5, pady=2)
        self.size_var = tk.StringVar(value="S")
        tk.OptionMenu(frame, self.size_var, "S", "M", "L").grid(row=5, column=1, padx=5, pady=2)

        tk.Label(frame, text="Extra Toppings?").grid(row=6, column=0, sticky="e", padx=5, pady=2)
        self.topping_var = tk.StringVar(value="N")
        topping_menu = tk.OptionMenu(frame, self.topping_var, "Y", "N", command=self.toggle_topping_entry)
        topping_menu.grid(row=6, column=1, padx=5, pady=2)

        tk.Label(frame, text="Number of Toppings:").grid(row=7, column=0, sticky="e", padx=5, pady=2)
        self.topping_entry = tk.Entry(frame)
        self.topping_entry.grid(row=7, column=1, padx=5, pady=2)
        self.topping_entry.config(state="disabled")

        tk.Button(frame, text="Add Pizza", command=self.add_pizza).grid(row=8, column=0, columnspan=2, pady=5)

        self.order_listbox = tk.Listbox(self.root, width=50, height=6)
        self.order_listbox.pack(pady=10)

        tk.Button(self.root, text="Remove Selected Pizza", command=self.remove_pizza).pack(pady=5)

        tk.Label(self.root, text="Delivery for £2.50?").pack()
        self.delivery_var = tk.StringVar(value="N")
        tk.OptionMenu(self.root, self.delivery_var, "Y", "N").pack()

        tk.Button(self.root, text="Finish Order", command=self.display_receipt).pack(pady=10)

    def toggle_custom_fields(self, value):
        self.topping_var.set("N")
        self.topping_entry.delete(0, tk.END)
        self.topping_entry.config(state="disabled")

    def toggle_topping_entry(self, value):
        if value == "Y":
            self.topping_entry.config(state="normal")
        else:
            self.topping_entry.delete(0, tk.END)
            self.topping_entry.config(state="disabled")

    def add_pizza(self):
        try:
            if len(self.pizzas) >= 6:
                messagebox.showerror("Error", "You cannot order more than 6 pizzas.")
                return

            pizza_type = self.pizza_type_var.get()
            size = self.size_var.get()
            topping_count = int(self.topping_entry.get()) if self.topping_var.get() == "Y" else 0

            if topping_count < 0 or topping_count > 4:
                messagebox.showerror("Error", "Number of toppings must be between 0 and 4.")
                return

            if pizza_type == "Margherita Pizza":
                pizza = MargheritaPizza(size, topping_count)
            elif pizza_type == "Pepperoni Pizza":
                pizza = PepperoniPizza(size, topping_count)
            elif pizza_type == "Ham & Pineapple Pizza":
                pizza = HamAndPineapplePizza(size, topping_count)
            else:
                base_prices = {"S": 3.25, "M": 5.50, "L": 7.15}
                topping_prices = [0, 0.75, 1.35, 2.00, 2.50]
                total_cost = base_prices[size] + topping_prices[topping_count]
                toppings = [f"Extra x{topping_count}"] if topping_count else []
                pizza = Pizza(size, toppings, total_cost)

            self.pizzas.append(pizza)
            self.order_listbox.insert(tk.END, str(pizza))
            messagebox.showinfo("Success", "Pizza added to order!")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of toppings.")

    def remove_pizza(self):
        selected_index = self.order_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a pizza to remove.")
            return

        index = selected_index[0]
        del self.pizzas[index]
        self.order_listbox.delete(index)
        messagebox.showinfo("Success", "Pizza removed from order.")

    def display_receipt(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        phone = self.phone_entry.get()

        if not name or not address or not phone.isdigit() or len(phone) != 11:
            messagebox.showerror("Error", "Please enter valid customer details.")
            return

        if len(self.pizzas) < 1:
            messagebox.showerror("Error", "You must order at least one pizza.")
            return

        total_pizza_cost = sum(pizza.total_cost for pizza in self.pizzas)
        receipt = f"Customer: {name}\nAddress: {address}\nPhone: {phone}\n\nOrder Summary:\n"

        for i, pizza in enumerate(self.pizzas, 1):
            receipt += f"Pizza {i}: {pizza}\n"

        if total_pizza_cost > 20:
            discount = total_pizza_cost * 0.1
            total_pizza_cost -= discount
            receipt += f"\nDiscount Applied: -£{discount:.2f}\n"

        if self.delivery_var.get() == "Y":
            total_pizza_cost += 2.50
            receipt += f"\nDelivery Fee: £2.50\n"

        receipt += f"Total Cost: £{total_pizza_cost:.2f}"
        messagebox.showinfo("Order Receipt", receipt)

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaOrderApp(root)
    root.mainloop()
