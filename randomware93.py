import customtkinter as ctk
import random

# Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("FAKE RANSOMWARE")
app.attributes("-fullscreen", True)
app.configure(bg="black")

# Disable close controls
app.protocol("WM_DELETE_WINDOW", lambda: None)
app.bind("<Alt-F4>", lambda e: "break")
app.bind("<Control-q>", lambda e: "break")
app.bind("<Escape>", lambda e: "break")

# === FRAME FOR BACKGROUND FLASHING ===
flash_frame = ctk.CTkFrame(app, width=1920, height=1080, fg_color="black")
flash_frame.pack(fill="both", expand=True)

# === UI ELEMENTS INSIDE FLASHING FRAME ===

label = ctk.CTkLabel(flash_frame, text="YOUR PC IS LOCKED!", font=("Courier", 48, "bold"), text_color="white", bg_color="black")
label.pack(pady=80)

msg_label = ctk.CTkLabel(flash_frame, text="Pay 100 BITCOINS or your files will be DELETED!", font=("Courier", 26), text_color="white", bg_color="black")
msg_label.pack(pady=10)

btc_addr_label = ctk.CTkLabel(
    flash_frame,
    text=f"BTC Address: {''.join(random.choices('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz', k=34))}",
    font=("Courier", 20),
    text_color="gray",
    bg_color="black"
)
btc_addr_label.pack(pady=10)

entry_label = ctk.CTkLabel(flash_frame, text="Enter decryption password:", font=("Courier", 20), text_color="white", bg_color="black")
entry_label.pack(pady=20)

password_entry = ctk.CTkEntry(flash_frame, show="*", width=300, font=("Courier", 18), placeholder_text="password")
password_entry.pack(pady=10)

# Unlock button (→ arrow)
def check_password():
    if password_entry.get() == "virus":
        app.destroy()

arrow_button = ctk.CTkButton(
    flash_frame,
    text="→",
    width=60,
    font=("Courier", 24, "bold"),
    command=check_password
)
arrow_button.pack(pady=10)

# === FLASHING FUNCTION ===

colors = ["black", "red"]
color_index = 0

def flash_bg():
    global color_index
    color = colors[color_index]
    
    flash_frame.configure(fg_color=color)
    label.configure(bg_color=color)
    msg_label.configure(bg_color=color)
    btc_addr_label.configure(bg_color=color)
    entry_label.configure(bg_color=color)
    password_entry.configure(bg_color=color)
    arrow_button.configure(bg_color=color)
    
    color_index = (color_index + 1) % 2
    app.after(500, flash_bg)

flash_bg()
app.mainloop()
