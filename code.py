# # import pyqrcode 
# # from pyqrcode import QRCode 
  
# # # String which represent the QR code 
# # s = "https://github.com/laxmanbalaraman/"
  
# # # Generate QR code 
# # url = pyqrcode.create(s) 
  
# # # Create and save the png file naming "myqr.png" 
# # url.png("myQr.png", scale = 8) 

# ##############################################################################

# import tkinter as tk
# from tkinter import messagebox
# import pyqrcode

# def generate_qr():
#     # Get the text from the entry widget
#     text = entry.get()
    
#     # Check if the input is empty
#     if not text:
#         messagebox.showerror("Error", "Please enter a link or text")
#         return
    
#     # Generate QR code
#     qr = pyqrcode.create(text)
    
#     # Save the QR code as PNG with filename based on input text
#     filename = f"{text}.png"
#     qr.png(filename, scale=8)
    
#     messagebox.showinfo("Success", "QR code generated successfully!")

# # Create the main window
# root = tk.Tk()
# root.title("QR Code Generator")

# # Create and configure the label
# label = tk.Label(root, text="Enter link or text:")
# label.pack(pady=10)

# # Create and configure the entry widget
# entry = tk.Entry(root, width=40)
# entry.pack()

# # Create and configure the button
# button = tk.Button(root, text="Generate QR Code", command=generate_qr)
# button.pack(pady=10)

# # Run the main event loop
# root.mainloop()


#####################################################################################################


import tkinter as tk
from tkinter import ttk, messagebox
import pyqrcode

def generate_qr():
    # Get the text from the entry widget
    text = entry.get()
    
    # Check if the input is empty
    if not text:
        messagebox.showerror("Error", "Please enter a link or text")
        return
    
    # Generate QR code
    qr = pyqrcode.create(text)
    
    # Save the QR code as PNG with filename based on input text
    filename = f"{text}.png"
    qr.png(filename, scale=8)
    
    messagebox.showinfo("Success", f"QR code generated successfully and saved as {filename}")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("300x200")

# Create and configure the style
style = ttk.Style()
style.configure("TButton", foreground="black", background="lightblue", font=("Helvetica", 10))

# Create and configure the label
label = ttk.Label(root, text="Enter link or text:")
label.pack(pady=10)

# Create and configure the entry widget
entry = ttk.Entry(root, width=40)
entry.pack()

# Create and configure the button
button = ttk.Button(root, text="Generate QR Code", command=generate_qr)
button.pack(pady=10)

# Run the main event loop
root.mainloop()
