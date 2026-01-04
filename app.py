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

from flask import Flask, render_template, request, send_from_directory, flash
import pyqrcode
import os
import re

app = Flask(__name__)
app.secret_key = "change-this-secret"

QR_FOLDER = "static/qr"
os.makedirs(QR_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    filename = None

    if request.method == "POST":
        text = request.form.get("text", "").strip()

        if not text:
            flash("Please enter a link or text", "error")
            return render_template("index.html")

        # Make filename safe
        safe_name = re.sub(r"[^a-zA-Z0-9_-]", "_", text)[:50]
        filename = f"{safe_name}.svg"

        qr = pyqrcode.create(text)
        qr.svg(os.path.join(QR_FOLDER, filename), scale=8)

        flash("QR code generated successfully!", "success")

    return render_template("index.html", filename=filename)

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(QR_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
