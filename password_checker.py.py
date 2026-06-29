import tkinter as tk
import re

def check_password_strength():
    password = entry.get()
    
    # Logic same hai, bas UI presentation upgrade hogi
    if len(password) < 8:
        msg, color, sugg = "Too Short!", "red", "Suggestion: Use 8+ characters."
    elif not re.search("[a-z]", password):
        msg, color, sugg = "Weak", "orange", "Suggestion: Add lowercase letters."
    elif not re.search("[A-Z]", password):
        msg, color, sugg = "Weak", "orange", "Suggestion: Add uppercase letters."
    elif not re.search("[0-9]", password):
        msg, color, sugg = "Fair", "yellow", "Suggestion: Add a number."
    elif not re.search("[!@#$%^&*]", password):
        msg, color, sugg = "Good", "blue", "Suggestion: Add a special symbol (!@#$)."
    else:
        msg, color, sugg = "Strong!", "green", "Your password is secure!"
    
    result_label.config(text=msg, fg=color)
    suggestion_label.config(text=sugg)

# GUI Setup - Ab thoda styling ke saath
root = tk.Tk()
root.title("Cyber Shield: Password Guard")
root.geometry("450x350")
root.configure(bg="#f0f0f0") # Light grey background

# Heading
tk.Label(root, text="Password Strength Analyzer", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=20)

# Entry with better padding
entry = tk.Entry(root, show="*", width=35, font=("Arial", 12))
entry.pack(pady=10)

# Stylish Button
check_button = tk.Button(root, text="Analyze Password", command=check_password_strength, 
                         bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=10)
check_button.pack(pady=15)

# Labels for Output
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f0f0")
result_label.pack(pady=5)

suggestion_label = tk.Label(root, text="", font=("Arial", 10, "italic"), bg="#f0f0f0", fg="#555")
suggestion_label.pack(pady=5)

root.mainloop()