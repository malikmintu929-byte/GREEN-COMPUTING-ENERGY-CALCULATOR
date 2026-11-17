
# PROJECT: GREEN COMPUTING ENERGY CALCULATOR:
import tkinter as tk
from tkinter import ttk, messagebox

#  WINDOW SETUP: 

root = tk.Tk()
root.title("Green Computing Energy Calculator")
root.geometry("750x720")
root.configure(bg="#EAF4EA")
root.resizable(False, False)

#  COLORS:

GREEN = "#187A45"
DARK_GREEN = "#105B34"
WHITE = "#FFFFFF"
BG = "#EAF4EA"

#  TITLE:

title = tk.Label(
    root,
    text="GREEN COMPUTING",
    font=("Arial", 23, "bold"),
    bg=BG,
    fg=DARK_GREEN
)
title.pack(pady=(18, 2))

subtitle = tk.Label(
    root,
    text="ENERGY CONSUMPTION CALCULATOR",
    font=("Arial", 12, "bold"),
    bg=BG,
    fg=GREEN
)
subtitle.pack(pady=(0, 15))

#  INPUT FRAME 

input_frame = tk.LabelFrame(
    root,
    text=" Enter Device Information ",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    fg=DARK_GREEN,
    padx=20,
    pady=15
)
input_frame.pack(padx=25, fill="x")

def create_input(label_text, row, default_value):
    label = tk.Label(
        input_frame,
        text=label_text,
        font=("Arial", 11),
        bg=WHITE
    )
    label.grid(row=row, column=0, sticky="w", pady=9)

    entry = ttk.Entry(input_frame, font=("Arial", 11), width=25)
    entry.grid(row=row, column=1, pady=9, padx=15)
    entry.insert(0, default_value)

    return entry

power_entry = create_input(
    "Device Power (Watt):", 0, " "
)

hours_entry = create_input(
    "Daily Usage (Hours):", 1, " "
)

rate_entry = create_input(
    "Electricity Rate (₹/unit):", 2, " "
)

factor_entry = create_input(
    "CO2 Factor (kg/kWh):", 3, " "
)

#RESULT FRAME

result_frame = tk.LabelFrame(
    root,
    text=" Energy Report ",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    fg=DARK_GREEN,
    padx=15,
    pady=12
)
result_frame.pack(padx=25, pady=15, fill="x")

result_labels = {}

results = [
    "Daily Energy:",
    "Monthly Energy:",
    "Monthly Electricity Bill:",
    "Estimated CO2 Emission:"
]

for i, name in enumerate(results):
    label = tk.Label(
        result_frame,
        text=name,
        font=("Arial", 11, "bold"),
        bg=WHITE
    )
    label.grid(row=i, column=0, sticky="w", pady=7)

    value = tk.Label(
        result_frame,
        text="--",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=GREEN
    )
    value.grid(row=i, column=1, sticky="w", padx=20)

    result_labels[name] = value

# ENERGY TIPS

tip_label = tk.Label(
    root,
    text="🌱 Energy Saving Tips",
    font=("Arial", 13, "bold"),
    bg=BG,
    fg=DARK_GREEN
)
tip_label.pack(pady=(5, 5))

tips = tk.Label(
    root,
    text=(
        "• Turn off unused computers.\n"
        "• Enable power-saving mode.\n"
        "• Use energy-efficient devices.\n"
        "• Recycle old electronic devices."
    ),
    font=("Arial", 10),
    bg=BG,
    justify="left",
    fg="#333333"
)
tips.pack(pady=5)

#  CALCULATION FUNCTION

def calculate_energy():

    try:
        power = float(power_entry.get())
        hours = float(hours_entry.get())
        rate = float(rate_entry.get())
        factor = float(factor_entry.get())

        # Input validation
        if power <= 0:
            raise ValueError("Power must be greater than zero.")

        if hours <= 0 or hours > 24:
            raise ValueError("Daily hours must be between 0 and 24.")

        if rate < 0:
            raise ValueError("Electricity rate cannot be negative.")

        if factor < 0:
            raise ValueError("CO2 factor cannot be negative.")

        # Daily energy calculation
        daily_energy = (power * hours) / 1000

        # Monthly energy calculation (30 days)
        monthly_energy = daily_energy * 30

        # Electricity bill
        monthly_bill = monthly_energy * rate

        # Estimated CO2 emission
        co2_emission = monthly_energy * factor

        # Display results
        result_labels["Daily Energy:"].config(
            text=f"{daily_energy:.2f} kWh"
        )

        result_labels["Monthly Energy:"].config(
            text=f"{monthly_energy:.2f} kWh"
        )

        result_labels["Monthly Electricity Bill:"].config(
            text=f"₹ {monthly_bill:.2f}"
        )

        result_labels["Estimated CO2 Emission:"].config(
            text=f"{co2_emission:.2f} kg CO2"
        )

    except ValueError as error:
        messagebox.showerror(
            "Invalid Input",
            str(error) if str(error) else "Please enter valid numbers."
        )

#  RESET FUNCTION 

def reset_calculator():

    power_entry.delete(0, tk.END)
    hours_entry.delete(0, tk.END)
    rate_entry.delete(0, tk.END)
    factor_entry.delete(0, tk.END)

    power_entry.insert(0, " ")
    hours_entry.insert(0, " ")
    rate_entry.insert(0, " ")
    factor_entry.insert(0, " ")

    for label in result_labels.values():
        label.config(text="0")

# BUTTONS 

button_frame = tk.Frame(root, bg=BG)
button_frame.pack(pady=12)

calculate_button = tk.Button(
    button_frame,
    text="CALCULATE ENERGY",
    font=("Arial", 11, "bold"),
    bg=GREEN,
    fg=WHITE,
    width=19,
    pady=9,
    cursor="hand2",
    command=calculate_energy
)
calculate_button.grid(row=0, column=0, padx=8)

reset_button = tk.Button(
    button_frame,
    text="RESET",
    font=("Arial", 11, "bold"),
    bg="#555555",
    fg=WHITE,
    width=12,
    pady=9,
    cursor="hand2",
    command=reset_calculator
)
reset_button.grid(row=0, column=1, padx=8)

#  FOOTER 

footer = tk.Label(
    root,
    text="Save Energy | Reduce E-Waste | Protect Earth",
    font=("Arial", 10, "bold"),
    bg=BG,
    fg=DARK_GREEN
)
footer.pack(pady=12)

#  RUN APPLICATION :

root.mainloop()