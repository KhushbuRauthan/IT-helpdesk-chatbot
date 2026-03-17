import tkinter as tk
from tkinter import scrolledtext

def chatbot():

    user = entry.get().lower().strip()

    if user == "":
        return

    chat.insert(tk.END,"You: " + user + "\n","user")

    if "password" in user:
        response = "You can reset your password using the password reset portal."

    elif "wifi" in user or "internet" in user:
        response = "Restart your router and check if the network cables are connected."

    elif "slow" in user or "performance" in user:
        response = "Restart your computer and close unused programs."

    elif "email" in user:
        response = "Check your internet connection and verify email settings."

    elif "vpn" in user:
        response = "Reconnect to VPN and verify your login credentials."

    elif "software" in user:
        response = "Try reinstalling the software or contact IT support."

    elif "printer" in user:
        response = "Check printer cables and restart the printer."

    elif "update" in user:
        response = "Go to system settings and check for updates."

    elif "login" in user:
        response = "Ensure your username and password are correct."

    elif "account locked" in user:
        response = "Wait 10 minutes and try again or contact IT support."

    else:
        response = "I cannot solve this automatically. Please contact the IT helpdesk."

    chat.insert(tk.END,"Bot: " + response + "\n\n","bot")

    entry.delete(0,tk.END)
    chat.yview(tk.END)


window = tk.Tk()
window.title("IT Helpdesk Chatbot")
window.geometry("560x520")
window.configure(bg="#1e1e2f")


title = tk.Label(
    window,
    text="IT Helpdesk Support Chatbot",
    font=("Arial",16,"bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=12)


chat = scrolledtext.ScrolledText(
    window,
    width=65,
    height=20,
    bg="#2c2c3e",
    fg="white",
    font=("Arial",10),
    bd=0
)
chat.pack(pady=10)


chat.tag_config("user",foreground="#00ffcc")
chat.tag_config("bot",foreground="#ffd166")


entry = tk.Entry(
    window,
    width=40,
    font=("Arial",12),
    bd=0
)
entry.pack(pady=8,ipady=6)


send = tk.Button(
    window,
    text="Send Message",
    command=chatbot,
    bg="#4CAF50",
    fg="white",
    font=("Arial",12,"bold"),
    width=18,
    height=2,
    bd=0,
    activebackground="#45a049",
    cursor="hand2"
)

send.pack(pady=12)


window.mainloop()