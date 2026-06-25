class MenuItem :
    service_charge = 0.0
    def __init__(self, code, name, base_price):
        self.code = code
        self.name = name
        self.__base_price = base_price
        self.__is_available = True

    @property
    def base_price(self) -> int:
        return self.__base_price
    
    @base_price.setter
    def base_price(self, new_price: int):
        if new_price > 0:
            self.__base_price = new_price
            print("Cập nhật giá gốc thành công!")
        else:
            print("Giá đồ uống phải lớn hơn 0!")
            print("Giá cũ được giữ nguyên.")

    @property
    def is_available(self) -> bool:
        return self.__is_available
        
    def toggle_availability(self) -> str:
        """Chuyển trạng thái hàng"""
        self.__is_available = not self.__is_available
        if self.__is_available:
            return "Đang bán"
        else:
            return "Hết hàng"

    @staticmethod
    def is_valid_item_id(item_code: str) -> bool:
        """Kiểm tra mã id gồm 2 chữ cái in hoa và 2 chữ số"""
        if len(item_code) != 4:
            return False
        
        char_part = item_code[:2]
        num_part = item_code[2:]
        if char_part.isalpha() and char_part.isupper() and num_part.isdigit():
            return True
        
        return False
    
    @classmethod
    def update_service_charge(cls, new_rate: float):
        cls.service_charge = new_rate
        print("Cập nhật phụ phí dịch vụ thành công!")

    def calculate_total_price(self) -> int:
        total = self.__base_price + (self.__base_price * MenuItem.service_charge)
        return int(total)

menu_db = [
    MenuItem("CF01", "Cà phê sữa", 35000),
    MenuItem("TS01", "Trà sữa matcha", 45000),
    MenuItem("TD01", "Trà đào cam sả", 40000)
]

def show_drink() :
    if not menu_db :
        print("Danh sách trống!")
    else :
        print("--- THỰC ĐƠN RIKKEI COFFEE ---")
        for i, count in enumerate(menu_db, start=1) :
            total_price = count.calculate_total_price()
            if count.is_available:
                str_status = "Đang bán"
            else:
                str_status = "Hết hàng"
            print(f"{i}. Mã: {count.code:<5} | Tên: {count.name:<17} | "
                  f"Trạng thái: {str_status:<10} | Giá niêm yết: {total_price:,} VND")

validate_code = MenuItem.is_valid_item_id
def add_drink() :
    while True:
        add_code = input("Nhập mã món: ").strip().upper()
        if add_code == '':
            print("Mã ko được để trống!")
            continue
        if not validate_code(add_code):
            print("Mã món không đúng định dạng! (Phải gồm 2 chữ cái in hoa và 2 chữ số, ví dụ: CF01)")
            continue
        for count in menu_db:
            if add_code == count.code:
                print("Mã đã tồn tại! Vui lòng nhập lại.")
                break
        else:
            break 

    while True :
        add_name = input("Nhập tên món: ").strip()
        if add_name == '' :
            print("Tên ko được để trống!")
            continue
        else :
            break
    
    while True :
        add_price_str = input("Nhập giá món: ").strip()
        if add_price_str == '' :
            print("Giá ko để trống!")
            continue
        try:
            add_price = int(add_price_str)
        except ValueError:
            print("Giá phải là số!")
            continue

        if add_price <= 0 :
            print("Giá phải lớn hơn 0!")
            continue
        else :
            new_drink = MenuItem(add_code, add_name, add_price)
            menu_db.append(new_drink)
            print(f"Thành công: Đã thêm món {add_name} vào thực đơn!")
            break
        
def update_drink():
    while True:
        update_code = input("Nhập mã món cần cập nhật: ").strip().upper()
        if update_code == "":
            print("Mã ko để trống!")
            continue
        for count in menu_db:
            if update_code == count.code:
                new_update_code = count.toggle_availability() 
                print(f">> Đã cập nhật thành công {count.name} thành {new_update_code}")
                break
        else:
            print("Mã ko tồn tại!")
            continue
        break

def update_price_drink():
    print("--- ĐIỀU CHỈNH GIÁ GỐC CỦA MÓN ---")
    while True:
        search_code = input("Nhập mã món cần đổi giá: ").strip().upper()
        if search_code == "":
            print("Mã món không được để trống!")
            continue
        for count in menu_db:
            if search_code == count.code:
                target_item = count
                break
        else:
            print("Mã món không tồn tại! Vui lòng nhập lại.")
            continue
        break

    while True:
        new_price_str = input("Nhập giá tiền mới: ").strip()
        if new_price_str == "":
            print("Giá tiền không được để trống!")
            continue
        try:
            new_price = int(new_price_str)
        except ValueError:
            print("Giá tiền phải là số nguyên!")
            continue

        old_price = target_item.base_price
        target_item.base_price = new_price
        if target_item.base_price == old_price:
            print("Vui lòng nhập lại giá hợp lệ!")
            continue
        break

def change_service_charge(cls_target):
    print("--- CẬP NHẬT PHỤ PHÍ DỊCH VỤ TOÀN HỆ THỐNG ---")
    current_percent = int(cls_target.service_charge * 100)
    print(f"Phụ phí hiện tại: {current_percent}%")
    while True:
        new_rate_str = input("Nhập phụ phí mới. Ví dụ 0.1 tương ứng 10%: ").strip()
        if new_rate_str == "":
            print("Phụ phí không được để trống!")
            continue
        try:
            new_rate = float(new_rate_str)
        except ValueError:
            print("Phụ phí phải là một số thập phân!")
            continue
        if new_rate < 0:
            print("Phụ phí dịch vụ không được nhỏ hơn 0!")
            continue

        cls_target.update_service_charge(new_rate)
        break
def main() :
    while True :
        print("""
=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===
1. Xem thực đơn & Giá niêm yết
2. Thêm món mới vào menu
3. Cập nhật trạng thái (Hết hàng/Còn hàng)
4. Điều chỉnh giá gốc của món
5. Cập nhật phụ phí dịch vụ toàn hệ thống
6. Thoát chương trình
==============================================
""")
        choice = input("Chọn chức năng (1-6): ").strip()
        if choice == '1' :
            show_drink()
        elif choice == '2':
            add_drink()
        elif choice == '3':
            update_drink()
        elif choice == '4':
            update_price_drink()
        elif choice == '5':
            change_service_charge(MenuItem)
        elif choice == '6':
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
            break
        else :
            print("Vui lòng nhập(1-6)!")

if __name__ == "__main__" :
    main()