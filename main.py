import getmac
import socket
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

def get_ip_and_mac_addresses(domain_name):
    domain_extensions = ["com", "org", "net"]  # Add more as needed
    addresses = []

    for ext in domain_extensions:
        full_domain = f"www.{domain_name}.{ext}"
        try:
            ip_address = socket.gethostbyname(full_domain)
            mac_address = getmac.get_mac_address(ip=ip_address)
            addresses.append((full_domain, ip_address, mac_address))
        except Exception as e:
            pass  # Continue to the next extension if not found or if any other exception occurs

    return addresses

def on_entry_click(event):
    if site_name_entry.get() == "Enter a site name or type 'suggestion' for help (e.g., google)":
        site_name_entry.delete(0, tk.END)
        site_name_entry.config(foreground="black")  # Change text color

def on_entry_focusout(event):
    if site_name_entry.get() == "":
        site_name_entry.insert(0, "Enter a site name or type 'suggestion' for help (e.g., google)")
        site_name_entry.config(foreground="grey")  # Change text color

def fetch_addresses():
    site_name = site_name_entry.get()
    if site_name:
        if site_name == "suggestion":
            result_text.config(state=tk.NORMAL)
            result_text.delete('1.0', tk.END)
            result_text.insert(tk.END, "Please enter a valid site name.")
            result_text.config(state=tk.DISABLED)
        else:
            addresses = get_ip_and_mac_addresses(site_name)
            if addresses:
                result_text.config(state=tk.NORMAL)
                result_text.delete('1.0', tk.END)
                for domain, ip_address, mac_address in addresses:
                    result_text.insert(tk.END, f"Domain: {domain}\n")
                    result_text.insert(tk.END, f"IP Address: {ip_address}\n")
                    result_text.insert(tk.END, f"MAC Address: {mac_address}\n\n")
                result_text.config(state=tk.DISABLED)
                save_button.config(state=tk.NORMAL)  # Enable the save button
            else:
                result_text.config(state=tk.NORMAL)
                result_text.delete('1.0', tk.END)
                result_text.insert(tk.END, f"Failed to retrieve IP and MAC addresses for {site_name}")
                result_text.config(state=tk.DISABLED)
                save_button.config(state=tk.DISABLED)  # Disable the save button

def save_to_file():
    addresses_text = result_text.get("1.0", tk.END)
    with open("addresses.txt", "w") as file:
        file.write(addresses_text)
    save_button.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("IP and MAC Address Finder")

# Set the window size
root.geometry("765x400")

# Make the main window unresizable
root.resizable(False, False)

# Apply a themed style for better aesthetics
style = ThemedStyle(root)
style.set_theme("radiance")  # Choose a theme (e.g., "radiance")

# Create and configure widgets
frame = ttk.Frame(root)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create the entry field with a larger font size
site_name_entry = ttk.Entry(frame, width=70)
site_name_entry.grid(column=0, row=0, padx=10, pady=(50, 10), sticky=(tk.W, tk.E))  # Remove columnspan
site_name_entry.insert(0, "Enter a site name or type 'suggestion' for help (e.g., google)")
site_name_entry.config(foreground="grey")  # Set default text color
site_name_entry.bind("<FocusIn>", on_entry_click)  # Handle click event
site_name_entry.bind("<FocusOut>", on_entry_focusout)  # Handle focus-out event

# Create a fetch button
fetch_button = ttk.Button(frame, text="Fetch Addresses", command=fetch_addresses)
fetch_button.grid(column=1, row=0, padx=10, pady=(50, 10), sticky=(tk.W, tk.E))  # Remove columnspan

# Create a result text box
result_text = tk.Text(root, wrap=tk.WORD, width=70, height=15, state=tk.DISABLED)
result_text.grid(column=0, row=1, padx=10, pady=10, sticky=(tk.W, tk.E), columnspan=2)

# Create a save button
save_button = ttk.Button(frame, text="Save to File", command=save_to_file, state=tk.DISABLED)
save_button.grid(column=2, row=0, padx=10, pady=(50, 10), sticky=(tk.W, tk.E))

# Create a watermark label
watermark_label = ttk.Label(frame, text="Made by Denis Dimov", font=("Helvetica", 10))
watermark_label.grid(column=0, row=1, padx=10, pady=(0, 10), sticky=(tk.W, tk.S))

# Configure column weights for centering
frame.grid_columnconfigure(0, weight=1)  # Make the input field expand horizontally
frame.grid_columnconfigure(1, weight=0)  # Keep the button fixed in size

root.mainloop()
