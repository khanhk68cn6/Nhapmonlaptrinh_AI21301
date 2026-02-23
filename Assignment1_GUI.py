"""
Assignment1 GUI Version - Phiên bản có giao diện đồ họa
Poly-Lap - Quản lý Laptop
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# ==================== DATA LAYER ====================

File_name = "laptops.json"

def load_data():
    """Load data from JSON file"""
    try:
        with open(File_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(laptops):
    """Save data to JSON file"""
    with open(File_name, "w", encoding="utf-8") as file:
        json.dump(laptops, file, ensure_ascii=False, indent=4)

def get_next_id(laptops):
    """Get next unique ID"""
    if not laptops:
        return "LT01"
    ids = [int(laptop["id"][2:]) for laptop in laptops if laptop["id"].startswith("LT")]
    if not ids:
        return "LT01"
    max_id = max(ids)
    return f"LT{max_id + 1:02d}"

# ==================== GUI APPLICATION ====================

class PolyLapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("POLY-LAP - Quản lý Laptop")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f0f0")
        
        self.laptops = load_data()
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Title
        title_label = tk.Label(
            self.root, 
            text="🖥️ POLY-LAP - QUẢN LÝ LAPTOP", 
            font=("Arial", 24, "bold"),
            bg="#2c3e50", 
            fg="white",
            pady=10
        )
        title_label.pack(fill=tk.X)
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Button Frame (Left side)
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)
        
        # Buttons
        btn_style = {
            "font": ("Arial", 12),
            "bg": "#3498db",
            "fg": "white",
            "activebackground": "#2980b9",
            "activeforeground": "white",
            "width": 20,
            "height": 2,
            "cursor": "hand2"
        }
        
        buttons = [
            ("➕ Thêm sản phẩm", self.add_laptop_gui),
            ("✏️ Cập nhật sản phẩm", self.update_laptop_gui),
            ("🗑️ Xóa sản phẩm", self.delete_laptop_gui),
            ("🔍 Tìm kiếm theo tên", self.search_laptop_gui),
            ("📋 Hiển thị tất cả", self.display_all_gui),
            ("📊 Thống kê biểu đồ", self.show_statistics),
            ("💾 Lưu dữ liệu", self.save_data_gui),
            ("❌ Thoát", self.exit_app)
        ]
        
        for text, command in buttons:
            btn = tk.Button(button_frame, text=text, command=command, **btn_style)
            btn.pack(pady=5)
        
        # Display Frame (Right side)
        display_frame = tk.Frame(main_frame, bg="white", relief=tk.SUNKEN, bd=2)
        display_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        # Treeview for displaying data
        columns = ("ID", "Tên", "Thương hiệu", "Giá", "Số lượng", "CPU", "RAM")
        self.tree = ttk.Treeview(display_frame, columns=columns, show="headings", height=25)
        
        # Column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(display_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Status bar
        self.status_label = tk.Label(
            self.root, 
            text="Sẵn sàng | Tổng sản phẩm: 0", 
            font=("Arial", 10),
            bg="#34495e", 
            fg="white",
            pady=5
        )
        self.status_label.pack(fill=tk.X)
        
        self.update_status()
    
    def update_status(self):
        """Update status bar"""
        self.status_label.config(text=f"Sẵn sàng | Tổng sản phẩm: {len(self.laptops)}")
    
    # ==================== CRUD OPERATIONS ====================
    
    def add_laptop_gui(self):
        """Add new laptop via GUI"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Thêm sản phẩm mới")
        dialog.geometry("400x450")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Input fields
        fields = {}
        labels = ["Tên sản phẩm:", "Thương hiệu:", "Giá (VND):", "Số lượng:", "CPU:", "RAM:"]
        row_vars = []
        
        for i, label_text in enumerate(labels):
            tk.Label(dialog, text=label_text, font=("Arial", 11)).grid(row=i, column=0, sticky="w", padx=10, pady=5)
            entry = tk.Entry(dialog, font=("Arial", 11), width=25)
            entry.grid(row=i, column=1, padx=10, pady=5)
            fields[label_text] = entry
        
        def submit():
            name = fields["Tên sản phẩm:"].get()
            brand = fields["Thương hiệu:"].get()
            price = fields["Giá (VND):"].get()
            quantity = fields["Số lượng:"].get()
            cpu = fields["CPU:"].get()
            ram = fields["RAM:"].get()
            
            # Validation
            if not name or not brand:
                messagebox.showerror("Lỗi", "Tên và thương hiệu không được để trống!")
                return
            
            try:
                price = int(price)
                if price <= 0:
                    messagebox.showerror("Lỗi", "Giá phải là số nguyên dương!")
                    return
            except ValueError:
                messagebox.showerror("Lỗi", "Giá phải là số nguyên!")
                return
            
            try:
                quantity = int(quantity)
                if quantity < 0:
                    messagebox.showerror("Lỗi", "Số lượng không được âm!")
                    return
            except ValueError:
                messagebox.showerror("Lỗi", "Số lượng phải là số nguyên!")
                return
            
            # Add laptop
            new_id = get_next_id(self.laptops)
            laptop = {
                "id": new_id,
                "name": name,
                "brand": brand,
                "price": price,
                "quantity": quantity,
                "cpu": cpu,
                "ram": ram
            }
            
            self.laptops.append(laptop)
            messagebox.showinfo("Thành công", f"✅ Đã thêm sản phẩm: {name}")
            dialog.destroy()
            self.update_status()
        
        tk.Button(dialog, text="Thêm sản phẩm", command=submit, bg="#27ae60", fg="white", 
                 font=("Arial", 12), width=15).grid(row=6, column=0, columnspan=2, pady=20)
    
    def update_laptop_gui(self):
        """Update laptop via GUI"""
        pid = simpledialog.askstring("Cập nhật sản phẩm", "Nhập mã sản phẩm cần cập nhật:")
        
        if not pid:
            return
        
        laptop = None
        for lp in self.laptops:
            if lp["id"] == pid:
                laptop = lp
                break
        
        if not laptop:
            messagebox.showerror("Lỗi", "❌ Không tìm thấy sản phẩm!")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Cập nhật - {pid}")
        dialog.geometry("400x450")
        dialog.transient(self.root)
        dialog.grab_set()
        
        fields = {}
        labels = ["Tên sản phẩm:", "Thương hiệu:", "Giá (VND):", "Số lượng:", "CPU:", "RAM:"]
        defaults = [laptop["name"], laptop["brand"], str(laptop["price"]), 
                   str(laptop["quantity"]), laptop["cpu"], laptop["ram"]]
        
        for i, (label_text, default) in enumerate(zip(labels, defaults)):
            tk.Label(dialog, text=label_text, font=("Arial", 11)).grid(row=i, column=0, sticky="w", padx=10, pady=5)
            entry = tk.Entry(dialog, font=("Arial", 11), width=25)
            entry.insert(0, default)
            entry.grid(row=i, column=1, padx=10, pady=5)
            fields[label_text] = entry
        
        def submit():
            laptop["name"] = fields["Tên sản phẩm:"].get()
            laptop["brand"] = fields["Thương hiệu:"].get()
            
            try:
                laptop["price"] = int(fields["Giá (VND):"].get())
                if laptop["price"] <= 0:
                    messagebox.showerror("Lỗi", "Giá phải là số nguyên dương!")
                    return
            except ValueError:
                messagebox.showerror("Lỗi", "Giá phải là số nguyên!")
                return
            
            try:
                laptop["quantity"] = int(fields["Số lượng:"].get())
                if laptop["quantity"] < 0:
                    messagebox.showerror("Lỗi", "Số lượng không được âm!")
                    return
            except ValueError:
                messagebox.showerror("Lỗi", "Số lượng phải là số nguyên!")
                return
            
            laptop["cpu"] = fields["CPU:"].get()
            laptop["ram"] = fields["RAM:"].get()
            
            messagebox.showinfo("Thành công", "✅ Cập nhật sản phẩm thành công!")
            dialog.destroy()
        
        tk.Button(dialog, text="Lưu thay đổi", command=submit, bg="#e67e22", fg="white", 
                 font=("Arial", 12), width=15).grid(row=6, column=0, columnspan=2, pady=20)
    
    def delete_laptop_gui(self):
        """Delete laptop via GUI"""
        pid = simpledialog.askstring("Xóa sản phẩm", "Nhập mã sản phẩm cần xóa:")
        
        if not pid:
            return
        
        for laptop in self.laptops:
            if laptop["id"] == pid:
                confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa sản phẩm {laptop['name']}?")
                if confirm:
                    self.laptops.remove(laptop)
                    messagebox.showinfo("Thành công", "🗑️ Đã xóa sản phẩm!")
                    self.update_status()
                return
        
        messagebox.showerror("Lỗi", "❌ Không tìm thấy sản phẩm!")
    
    def search_laptop_gui(self):
        """Search laptop by name via GUI"""
        keyword = simpledialog.askstring("Tìm kiếm", "Nhập từ khóa tìm kiếm:")
        
        if not keyword:
            return
        
        # Clear treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        found = False
        for laptop in self.laptops:
            if keyword.lower() in laptop["name"].lower():
                self.tree.insert("", tk.END, values=(
                    laptop["id"],
                    laptop["name"],
                    laptop["brand"],
                    f"{laptop['price']:,}",
                    laptop["quantity"],
                    laptop["cpu"],
                    laptop["ram"]
                ))
                found = True
        
        if found:
            messagebox.showinfo("Kết quả", f"✅ Tìm thấy {sum(1 for lp in self.laptops if keyword.lower() in lp['name'].lower())} sản phẩm!")
        else:
            messagebox.showinfo("Kết quả", "❌ Không tìm thấy sản phẩm nào!")
    
    def display_all_gui(self):
        """Display all laptops in treeview"""
        # Clear treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        if not self.laptops:
            messagebox.showinfo("Thông báo", "📦 Kho hàng trống!")
            return
        
        for laptop in self.laptops:
            self.tree.insert("", tk.END, values=(
                laptop["id"],
                laptop["name"],
                laptop["brand"],
                f"{laptop['price']:,}",
                laptop["quantity"],
                laptop["cpu"],
                laptop["ram"]
            ))
        
        messagebox.showinfo("Thành công", f"✅ Hiển thị {len(self.laptops)} sản phẩm!")
    
    def show_statistics(self):
        """Show statistics with charts (like MATLAB)"""
        if not self.laptops:
            messagebox.showinfo("Thông báo", "❌ Không có dữ liệu để thống kê!")
            return
        
        # Create chart window
        chart_window = tk.Toplevel(self.root)
        chart_window.title("📊 Thống kê - Biểu đồ")
        chart_window.geometry("900x600")
        
        # Prepare data
        brands = {}
        prices = []
        quantities = []
        names = []
        
        for laptop in self.laptops:
            brand = laptop["brand"]
            brands[brand] = brands.get(brand, 0) + 1
            prices.append(laptop["price"])
            quantities.append(laptop["quantity"])
            names.append(laptop["name"][:15] + "..." if len(laptop["name"]) > 15 else laptop["name"])
        
        # Create matplotlib figure
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle("POLY-LAP - Thống kê doanh số", fontsize=16, fontweight="bold")
        
        # Chart 1: Bar chart - Number of products by brand
        ax1.bar(brands.keys(), brands.values(), color=["#3498db", "#e74c3c", "#2ecc71", "#f39c12", "#9b59b6"])
        ax1.set_title("Số lượng sản phẩm theo thương hiệu")
        ax1.set_xlabel("Thương hiệu")
        ax1.set_ylabel("Số lượng")
        ax1.tick_params(axis="x", rotation=45)
        
        # Chart 2: Pie chart - Market share by brand
        ax2.pie(brands.values(), labels=brands.keys(), autopct="%1.1f%%", 
               colors=["#3498db", "#e74c3c", "#2ecc71", "#f39c12", "#9b59b6"])
        ax2.set_title("Tỷ trọng thương hiệu")
        
        # Chart 3: Price distribution
        ax3.hist(prices, bins=10, color="#3498db", edgecolor="white")
        ax3.set_title("Phân bố giá sản phẩm")
        ax3.set_xlabel("Giá (VND)")
        ax3.set_ylabel("Số lượng")
        ax3.ticklabel_format(style="plain", axis="x")
        
        # Chart 4: Top products by quantity
        sorted_laptops = sorted(self.laptops, key=lambda x: x["quantity"], reverse=True)[:5]
        top_names = [lp["name"][:12] + "..." if len(lp["name"]) > 12 else lp["name"] for lp in sorted_laptops]
        top_quantities = [lp["quantity"] for lp in sorted_laptops]
        
        bars = ax4.barh(top_names[::-1], top_quantities[::-1], color="#2ecc71")
        ax4.set_title("Top 5 sản phẩm tồn kho cao nhất")
        ax4.set_xlabel("Số lượng tồn kho")
        
        # Add value labels on bars
        for bar, val in zip(bars, top_quantities[::-1]):
            ax4.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, 
                    str(val), va="center", fontweight="bold")
        
        plt.tight_layout()
        
        # Embed matplotlib in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Close button
        tk.Button(chart_window, text="Đóng", command=chart_window.destroy, 
                 bg="#95a5a6", fg="white", font=("Arial", 12)).pack(pady=10)
    
    def save_data_gui(self):
        """Save data via GUI"""
        save_data(self.laptops)
        messagebox.showinfo("Thành công", "💾 Dữ liệu đã được lưu!")
    
    def exit_app(self):
        """Exit application"""
        confirm = messagebox.askyesno("Xác nhận", "Bạn có muốn lưu dữ liệu trước khi thoát?")
        if confirm:
            save_data(self.laptops)
        self.root.destroy()

# ==================== MAIN ====================

if __name__ == "__main__":
    root = tk.Tk()
    app = PolyLapApp(root)
    root.mainloop()
