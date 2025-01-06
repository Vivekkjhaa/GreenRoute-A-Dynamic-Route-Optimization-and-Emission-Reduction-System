import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from backend import noofdelivery, disttravelled, salary, fuelsaved, vehicletype, startdelivery
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk

def show_loading_screen():
    title = "Welcome to My App"
    message = "Loading... Please wait."
    image_path = "src\\icon.jpg"

    def animate_spinner():
        """Creates and animates a spinning circle."""
        canvas.delete("all")

        # Get canvas dimensions for responsiveness
        width = canvas.winfo_width() or 200
        height = 200  # Fixed height for spinner

        # Set the size and position of the spinner
        radius = 40  # Spinner radius
        thickness = 6  # Spinner line thickness

        # Draw the spinner arc
        canvas.create_arc(
            width / 2 - radius,
            height / 2 - radius,
            width / 2 + radius,
            height / 2 + radius,  # Bounding box
            start=angle[0],
            extent=60,  # Angle of the arc
            width=thickness,  # Line thickness for smooth spinner
            outline="#FFFFFF",  # White spinner color
            style=tk.ARC,
        )

        # Update the angle to rotate the spinner
        angle[0] += 8  # Increment by smaller degrees for smooth animation

        if angle[0] >= 360:
            angle[0] = 0  # Reset the angle to start over

        # Continue the animation
        root.after(16, animate_spinner)  # Redraw every 16 ms for smooth animation

    def load_image(path, size):
        """Load and resize an image using Pillow."""
        try:
            img = Image.open(path)
            img = img.resize(size, Image.Resampling.LANCZOS)  # High-quality resizing
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading image: {e}")
            return None  # Return None if image fails to load

    # Create the main window
    root = tk.Tk()
    root.title(title)
    root.geometry("1920x1080")
    root.resizable(True, True)
    root.configure(bg="#000000")  # Black background

    # Top Title Label
    title_label = tk.Label(
        root,
        text=title,
        font=("Arial", 36, "bold"),
        bg="#000000",
        fg="#FFFFFF",
    )
    title_label.pack(pady=20)

    # Center Image
    if image_path:
        center_image = load_image(image_path, (300, 300))  # Resize to 300x300
        '''if center_image:
            #image_label = tk.Label(root, image=center_image, bg="#000000")
            image_label.pack(expand=True)
        else:
            print("Failed to load image.")'''

    # Bottom Message
    message_label = tk.Label(
        root,
        text=message,
        font=("Arial", 18),
        bg="#000000",
        fg="#FFFFFF",
    )
    message_label.pack(pady=10, side=tk.BOTTOM)

    # Spinner Canvas
    canvas = tk.Canvas(root, bg="#000000", bd=0, highlightthickness=0)
    canvas.pack(pady=20, side=tk.BOTTOM)

    angle = [0]  # Mutable angle to allow updates in the nested function
    animate_spinner()  # Start the spinner animation

    # Close the loading screen after 5 seconds
    root.after(5000, root.destroy)

    root.mainloop()

deliveries = []

def save_delivery_data(address, delivery_date, vehicle_type):
    """Function to save delivery data into the deliveries list"""
    deliveries.append({
        "from": "Unknown",  # You can customize this as per your use case
        "to": "Unknown",    # Same here
        "orderId": f"#{len(deliveries)+1}",
        "status": "Pending",
        "progress": 0,
        "weight": "Unknown",  # Add your own logic to handle weight
        "price": "Unknown",   # Add your own logic to handle price
        "departure": delivery_date,
        "driver": "Unknown", # You can customize this
    })

def display_delivery_tracking(deliveries):
    """Function to display all the deliveries in a new window"""
    # Create a new top-level window to show the deliveries
    delivery_window = tk.Toplevel()
    delivery_window.title("All Deliveries")
    delivery_window.geometry("1000x600")
    
    # Frame for the delivery list
    delivery_frame = tk.Frame(delivery_window, bg="#212121")
    delivery_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
    
    # Loop through all deliveries and add them to the list
    for delivery in deliveries:
        card_frame = tk.Frame(delivery_frame, bg="#2A2A2A", padx=10, pady=10)
        card_frame.pack(fill=tk.X, pady=5)

        # Title
        title = tk.Label(
            card_frame,
            text=f"Package from {delivery['from']} to {delivery['to']}",
            font=("Arial", 14, "bold"),
            bg="#2A2A2A",
            fg="white"
        )
        title.pack(anchor="w")

        # Order ID and Status
        order_status = tk.Label(
            card_frame,
            text=f"Order ID: {delivery['orderId']} | Status: {delivery['status']}",
            font=("Arial", 12),
            bg="#2A2A2A",
            fg="white"
        )
        order_status.pack(anchor="w")

        # Progress bar
        progress_bar = ttk.Progressbar(
            card_frame,
            value=delivery["progress"],
            maximum=100
        )
        progress_bar.pack(fill=tk.X, pady=5)

        # Driver info placeholder
        driver_info = tk.Frame(card_frame, bg="#2A2A2A")
        driver_info.pack(fill=tk.X, pady=5)

        driver_label = tk.Label(
            driver_info,
            text=f"Driver: {delivery['driver']}",
            font=("Arial", 12),
            bg="#2A2A2A",
            fg="white"
        )
        driver_label.pack(side=tk.LEFT)

        contact_btn = tk.Button(
            driver_info,
            text="Contact",
            font=("Arial", 10),
            bg="#1E88E5",
            fg="white",
            bd=0,
            padx=10
        )
        contact_btn.pack(side=tk.RIGHT)

    delivery_window.mainloop()

def deliveryscreen():
    # Initialize the delivery screen window
    delivery_window = tk.Toplevel()  # Create a new top-level window
    delivery_window.title("Start Delivery")
    delivery_window.geometry("600x400")
    delivery_window.configure(bg="#1E1E1E")

    # Header Label
    header_label = tk.Label(
        delivery_window,
        text="Enter Delivery Details",
        font=("Arial", 24, "bold"),
        bg="#1E1E1E",
        fg="#FFFFFF"
    )
    header_label.pack(pady=20)

    # Create a frame for the form inputs
    form_frame = tk.Frame(delivery_window, bg="#1E1E1E")
    form_frame.pack(pady=20)

    # Address Input
    address_label = tk.Label(
        form_frame,
        text="Delivery Address:",
        font=("Arial", 14),
        bg="#1E1E1E",
        fg="#FFFFFF"
    )
    address_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
    address_entry = tk.Entry(form_frame, font=("Arial", 14), width=40)
    address_entry.grid(row=0, column=1, padx=10, pady=5)

    # Delivery Date Input
    date_label = tk.Label(
        form_frame,
        text="Delivery Date (YYYY-MM-DD):",
        font=("Arial", 14),
        bg="#1E1E1E",
        fg="#FFFFFF"
    )
    date_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    date_entry = tk.Entry(form_frame, font=("Arial", 14), width=40)
    date_entry.grid(row=1, column=1, padx=10, pady=5)

    # Vehicle Type Input
    vehicle_label = tk.Label(
        form_frame,
        text="Vehicle Type:",
        font=("Arial", 14),
        bg="#1E1E1E",
        fg="#FFFFFF"
    )
    vehicle_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    vehicle_entry = tk.Entry(form_frame, font=("Arial", 14), width=40)
    vehicle_entry.grid(row=2, column=1, padx=10, pady=5)

    # Submit Button to save the data
    def on_submit():
        address = address_entry.get()
        delivery_date = date_entry.get()
        vehicle_type = vehicle_entry.get()

        if not address or not delivery_date or not vehicle_type:
            messagebox.showerror("Error", "All fields are required!")
        else:
            # Save the data
            save_delivery_data(address, delivery_date, vehicle_type)
            # Reset the form fields after saving
            address_entry.delete(0, tk.END)
            date_entry.delete(0, tk.END)
            vehicle_entry.delete(0, tk.END)
            

    submit_button = tk.Button(
        delivery_window,
        text="Submit Delivery",
        font=("Arial", 16),
        bg="#4CAF50",  # Green color
        fg="#FFFFFF",
        command=on_submit,
        relief="raised",
        width=20,
        height=2
    )
    submit_button.pack(pady=20)

    # Button to view all deliveries
    show_button = tk.Button(
        delivery_window,
        text="View All Deliveries",
        font=("Arial", 16),
        bg="#1E88E5",  # Blue color
        fg="#FFFFFF",
        command=lambda: display_delivery_tracking(deliveries),
        relief="raised",
        width=20,
        height=2
    )
    show_button.pack(pady=10)

    # Start the delivery screen window
    #delivery_window.mainloop()

def main_screen():
    # Initialize the main window
    root = tk.Tk()
    root.title("Dynamic Route Optimization and Emission Reduction System")
    root.geometry("1920x1080")
    root.configure(bg="#1E1E1E")

    # Header Section
    header_frame = tk.Frame(root, bg="#2E2E2E", height=100)
    header_frame.pack(fill="x")

    # Application Title
    title_label = tk.Label(
        header_frame,
        text="Dynamic Route Optimization and Emission Reduction System",
        font=("Arial", 24, "bold"),
        bg="#2E2E2E",
        fg="#FFFFFF"
    )
    title_label.pack(pady=30)

    # Main Content Frame
    content_frame = tk.Frame(root, bg="#1E1E1E")
    content_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Left Panel for Function Values
    left_frame = tk.Frame(content_frame, bg="#1E1E1E", width=400, pady=10, padx=20)
    left_frame.pack(side="left", fill="y", expand=False)

    tk.Label(
        left_frame,
        text="Function Outputs",
        font=("Arial", 18, "bold"),
        bg="#1E1E1E",
        fg="#FFFFFF"
    ).pack(pady=10)

    # Display Values from Functions
    function_values = {
        "Number of Deliveries": noofdelivery(),
        "Distance Travelled (km)": disttravelled(),
        "Driver Salary ($)": salary(),
        "Fuel Saved (liters)": fuelsaved(),
        "Vehicle Type": vehicletype(),
        "Start Delivery Status": startdelivery(),
    }

    for name, value in function_values.items():
        tk.Label(
            left_frame,
            text=f"{name}: {value}",
            bg="#1E1E1E",
            fg="#FFFFFF",
            font=("Arial", 14),
            pady=10
        ).pack(anchor="w", padx=10)

    # Start Delivery Button
    def open_delivery_screen():
        # Call the delivery screen when the button is clicked
        deliveryscreen()

    start_button = tk.Button(
        content_frame,
        text="Start Delivery",
        font=("Arial", 16),
        bg="#4CAF50",  # Green color for the button
        fg="#FFFFFF",
        command=open_delivery_screen,  # Trigger the delivery screen
        relief="raised",
        width=20,
        height=2
    )
    start_button.pack(pady=20)

    # Footer Section
    footer_frame = tk.Frame(root, bg="#2E2E2E", height=50)
    footer_frame.pack(fill="x", side="bottom")

    footer_label = tk.Label(
        footer_frame,
        text="© 2024 Dynamic Route Optimization. All Rights Reserved.",
        font=("Arial", 12),
        bg="#2E2E2E",
        fg="#FFFFFF"
    )
    footer_label.pack(pady=10)

    # Start the main loop
    root.mainloop()

def display_delivery_tracking(deliveries):
    # Create the main app window
    root = tk.Tk()
    root.title("Delivery Tracking")
    root.geometry("1000x600")
    root.configure(bg="#212121")  # Dark background

    # Sidebar for navigation
    sidebar = tk.Frame(root, bg="#1E1E1E", width=80)
    sidebar.pack(side=tk.LEFT, fill=tk.Y)

    icons = ["Home", "Location", "Settings"]
    for icon in icons:
        btn = tk.Button(
            sidebar,
            text=icon,
            font=("Arial", 12),
            bg="#1E1E1E",
            fg="white",
            bd=0,
            activebackground="#333333",
            activeforeground="white"
        )
        btn.pack(pady=20)

    # Main content divided into two sections (left and right)
    main_frame = tk.Frame(root, bg="#212121")
    main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Left section for delivery list
    delivery_frame = tk.Frame(main_frame, bg="#212121", width=400)
    delivery_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

    # Scrollable area for deliveries
    canvas = tk.Canvas(delivery_frame, bg="#212121", highlightthickness=0)
    scrollbar = ttk.Scrollbar(delivery_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#212121")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Add delivery cards to scrollable frame
    for delivery in deliveries:
        card_frame = tk.Frame(scrollable_frame, bg="#2A2A2A", padx=10, pady=10)
        card_frame.pack(fill=tk.X, pady=5)

        # Title
        title = tk.Label(
            card_frame,
            text=f"Package from {delivery['from']} to {delivery['to']}",
            font=("Arial", 14, "bold"),
            bg="#2A2A2A",
            fg="white"
        )
        title.pack(anchor="w")

        # Order ID and Status
        order_status = tk.Label(
            card_frame,
            text=f"Order ID: {delivery['orderId']} | Status: {delivery['status']}",
            font=("Arial", 12),
            bg="#2A2A2A",
            fg="white"
        )
        order_status.pack(anchor="w")

        # Progress bar
        progress_bar = ttk.Progressbar(
            card_frame,
            value=delivery["progress"],
            maximum=100
        )
        progress_bar.pack(fill=tk.X, pady=5)

        # Driver and contact
        driver_info = tk.Frame(card_frame, bg="#2A2A2A")
        driver_info.pack(fill=tk.X, pady=5)

        driver_label = tk.Label(
            driver_info,
            text=f"Driver: {delivery['driver']}",
            font=("Arial", 12),
            bg="#2A2A2A",
            fg="white"
        )
        driver_label.pack(side=tk.LEFT)

        contact_btn = tk.Button(
            driver_info,
            text="Contact",
            font=("Arial", 10),
            bg="#1E88E5",
            fg="white",
            bd=0,
            padx=10
        )
        contact_btn.pack(side=tk.RIGHT)

    # Right section for map
    map_frame = tk.Frame(main_frame, bg="black")
    map_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=10, expand=True)

    map_label = tk.Label(
        map_frame,
        text="Map Placeholder",
        font=("Arial", 16),
        bg="black",
        fg="white"
    )
    map_label.pack(expand=True)

    # Run the app
    root.mainloop()
