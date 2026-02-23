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

# ========== INPUT VALIDATION HELPER FUNCTIONS ==========

def get_valid_string_input(prompt, field_name):
    """
    Validates that user input is not empty.
    
    Args:
        prompt (str): The message to display to the user
        field_name (str): The name of the field being validated (for error messages)
        
    Returns:
        str: A non-empty string from user input
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(f"❌ {field_name} không được để trống. Vui lòng nhập lại.")

def validate_product_id(pid, laptops):
    """
    Validates that product ID exists in the inventory.
    
    Args:
        pid (str): The product ID to validate
        laptops (list): List of all laptops
    
    Returns:
        bool: True if valid, False otherwise
    """
    for laptop in laptops:
        if laptop["id"] == pid.upper():
            return True
    print(f"❌ Không tìm thấy sản phẩm với mã '{pid}'.")
    return False

def validate_menu_choice(choice):
    """
    Validates that menu choice is a valid number between 0-5.
    
    Args:
        choice (str): User's menu selection
    
    Returns:
        int or None: Valid choice as integer, or None if invalid
    """
    try:
        num = int(choice)
        if num < 0 or num > 5:
            print("❌ Lựa chọn không hợp lệ! Vui lòng chọn từ 0-5.")
            return None
        else:
            return num
    except ValueError:
        print("❌ Lựa chọn phải là số! Vui lòng nhập lại.")
        return None


# 3. Thêm dữ liệu mới cho sản phẩm

def add_laptop(laptops):

    new_id = get_next_id(laptops)
    name = get_valid_string_input("Nhập tên sản phẩm: ", "Tên sản phẩm")
    brand = get_valid_string_input("Nhập thương hiệu: ", "Thương hiệu")

    MAX_PRICE = 1000000000  # 1 tỷ USD
    
    while True:
        try:
            price_input = input("Nhập giá (VND): ")
            price = int(price_input)
            if price <= 0:
                print("❌ Giá phải là số nguyên dương. Vui lòng thử lại.")
                continue
            if price > MAX_PRICE:
                print(f"❌ Giá không được vượt quá {MAX_PRICE:,} VND (1 tỷ USD). Vui lòng thử lại.")
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

    cpu = get_valid_string_input("Nhập kiểu CPU: ", "CPU")
    ram = get_valid_string_input("Nhập dung lượng RAM: ", "RAM")
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
    pid = input("✏️ Nhập mã sản phẩm cần cập nhật: ").upper()

    # Validate product ID exists
    found = False
    for laptop in laptops:
        if laptop["id"] == pid:
            found = True
            laptop["name"] = get_valid_string_input("Tên mới: ", "Tên sản phẩm")
            laptop["brand"] = get_valid_string_input("Thương hiệu mới: ", "Thương hiệu")

            # Price update with skip option and limit
            MAX_PRICE = 1000000000  # 1 tỷ USD
            print(f"Giá hiện tại: {laptop['price']} VND")
            while True:
                price_input = input("Giá mới (Nhập số để thay đổi, để trống để giữ nguyên): ").strip()
                if price_input == "":
                    print("➡️ Giá không thay đổi.")
                    break
                try:
                    price = int(price_input)
                    if price <= 0:
                        print("❌ Giá phải là số nguyên dương. Vui lòng thử lại.")
                        continue
                    if price > MAX_PRICE:
                        print(f"❌ Giá không được vượt quá {MAX_PRICE:,} VND (1 tỷ USD). Vui lòng thử lại.")
                        continue
                    laptop["price"] = price
                    break
                except ValueError:
                    print("❌ Giá phải là số nguyên. Vui lòng thử lại.")

            # Quantity update
            print(f"Số lượng hiện tại: {laptop['quantity']}")
            while True:
                quantity_input = input("Số lượng mới (Nhập số để thay đổi, để trống để giữ nguyên): ").strip()
                if quantity_input == "":
                    print("➡️ Số lượng không thay đổi.")
                    break
                try:
                    quantity = int(quantity_input)
                    if quantity < 0:
                        print("❌ Số lượng không được âm. Vui lòng thử lại.")
                        continue
                    laptop["quantity"] = quantity
                    break
                except ValueError:
                    print("❌ Số lượng phải là số nguyên. Vui lòng thử lại.")

            print("✅ Cập nhật thành công!")
            return

    if not found:
        print(f"❌ Không tìm thấy sản phẩm với mã '{pid}'.")

# 5. Xóa sản phẩm
def delete_laptop(laptops):
    pid = input("🗑️ Nhập mã sản phẩm cần xóa: ").upper()

    # Validate product ID exists
    found = False
    for laptop in laptops:
        if laptop["id"] == pid:
            found = True
            laptops.remove(laptop)
            print("✅ Đã xóa sản phẩm thành công!")
            return

    if not found:
        print(f"❌ Không tìm thấy sản phẩm với mã '{pid}'.")
    

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
        
        # Validate menu choice
        valid_choice = validate_menu_choice(choice)
        if valid_choice is None:
            continue  # Invalid choice, ask again
            
        if valid_choice == 1:
            laptops = add_laptop(laptops)
        elif valid_choice == 2:
            update_laptop(laptops)
        elif valid_choice == 3:
            delete_laptop(laptops)
        elif valid_choice == 4:
            search_laptop_by_name(laptops)
        elif valid_choice == 5:
            display_all_laptop(laptops)
        elif valid_choice == 0:
            save_data(laptops)
            print("👋 Thoát chương trình. Dữ liệu đã được lưu.")
            break

if __name__ == "__main__":
    aa()
