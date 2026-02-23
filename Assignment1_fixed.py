# Cấu trúc dữ liệu thư viện

laptops = [
 {
   "id" : "LT01",
   "name" : "Laptop Gaming Acer Nitro 5",
   "brand" :  "Acer",
   "price" : 200000000,
   "quantity": 100,
    "cpu": "intel i5",
    "ram": "16 Gb"
 }
]

#POLY-LAP/
# main.py
# product_manager.py
# products.json   (tự tạo khi chạy)
# Module Assignment1.py

import json

File_name = "laptops.json"

# 1. Load Dữ liệu

def load_data():
    try:
      with open(File_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# 2. Lưu dữ liệu

def save_data(laptops):
    with open (File_name, "w", encoding="utf-8" ) as file:
     json.dump(laptops, file, encoding="utf-8")

# Helper function to get next unique ID
def get_next_id(laptops):
    if not laptops:
        return "LT01"
    # Extract numeric parts of IDs (assuming format LTXX where XX is number)
    ids = [int(laptop["id"][2:]) for laptop in laptops if laptop["id"].startswith("LT")]
    if not ids:
        return "LT01"
    max_id = max(ids)
    return f"LT{max_id + 1:02d}"

# 3. Thêm dữ liệu mới cho sản phẩm

def add_laptop(laptops):

    new_id = get_next_id(laptops)
    name = input("Nhập tên sản phẩm: ")
    brand = input("Nhập thương hiệu: ")

    while True:
        try:
            price = int(input("Nhập giá: "))
            if price <= 0:
                print("❌ Giá phải là số nguyên dương. Vui lòng thử lại.")
                continue
            break
        except ValueError:
            print("❌ Giá phải là số nguyên. Vui lòng thử lại.")

    while True:
        try:
            quantity = int(input("Nhập số lượng tồn kho: "))
            if quantity < 0:
                print("❌ Số lượng không được âm. Vui lòng thử lại.")
                continue
            break
        except ValueError:
            print("❌ Số lượng phải là số nguyên. Vui lòng thử lại.")

    cpu = input("Nhập kiểu cpu:")
    ram= input("Nhập dung lượng ram:")
    laptop = {
        "id": new_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity,
        "cpu": cpu,
        "ram": ram
    }

    laptops.append(laptop)
    print("✅ Đã thêm sản phẩm thành công!")
    return laptops

# 4 Cập nhật sản phẩm
def update_laptop(laptops):
    pid = input("✏️ Nhập mã sản phẩm cần cập nhật: ")

    for laptop in laptops:
        if laptop["id"] == pid:
            laptop["name"] = input("Tên mới: ")
            laptop["brand"] = input("Thương hiệu mới: ")

            while True:
                try:
                    laptop["price"] = int(input("Giá mới: "))
                    if laptop["price"] <= 0:
                        print("❌ Giá phải là số nguyên dương. Vui lòng thử lại.")
                        continue
                    break
                except ValueError:
                    print("❌ Giá phải là số nguyên. Vui lòng thử lại.")

            while True:
                try:
                    laptop["quantity"] = int(input("Số lượng mới: "))
                    if laptop["quantity"] < 0:
                        print("❌ Số lượng không được âm. Vui lòng thử lại.")
                        continue
                    break
                except ValueError:
                    print("❌ Số lượng phải là số nguyên. Vui lòng thử lại.")

            print(" Cập nhật thành công!")
            return

    print("❌ Không tìm thấy sản phẩm.")

# 5. Xóa sản phẩm
def delete_laptop(laptops):
    pid = input("🗑️ Nhập mã sản phẩm cần xóa: ")

    for laptop in laptops:
        if laptop["id"] == pid:
            laptops.remove(laptop)
            print(" Đã xóa sản phẩm.")
            return

    print("❌ Không tìm thấy sản phẩm.")
    

# 6. Tìm kiếm theo tên
def search_laptop_by_name(laptops):
    keyword = input("🔍 Nhập từ khóa tìm kiếm: ").lower()
    found = False

    for laptop in laptops:
        if keyword in laptop["name"].lower():
            print(laptop)
            found = True

    if not found:
        print("❌ Không tìm thấy sản phẩm phù hợp.")

# 7. Hiển thị tất cả sản phẩm
def display_all_laptop(laptops):
    if not laptops:
        print("📦 Kho hàng trống.")
        return

    print("\n===== DANH SÁCH SẢN PHẨM =====")
    for p in laptops:
        # sai
        print(f"""
Mã SP     : {p['id']}

Tên       : {p['name']}
Thương hiệu: {p['brand']}
Giá       : {p['price']} VND
Số lượng  : {p['quantity']}
CPU : {p['cpu']}
RAM : {p['ram']}
------------------------------
""")
        

def aa():
    laptops = load_data()

    while True:
        print("""
====== POLY-LAP - QUẢN LÝ LAPTOP ======
1. Thêm sản phẩm
2. Cập nhật sản phẩm
3. Xóa sản phẩm
4. Tìm kiếm theo tên
5. Hiển thị tất cả sản phẩm
0. Thoát
""")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            laptops = add_laptop(laptops)
        elif choice == "2":
            update_laptop(laptops)
        elif choice == "3":
            delete_laptop(laptops)
        elif choice == "4":
            search_laptop_by_name(laptops)
        elif choice == "5":
            display_all_laptop(laptops)
        elif choice == "0":
            save_data(laptops)
            print("👋 Thoát chương trình. Dữ liệu đã được lưu.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    aa()
