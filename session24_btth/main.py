class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.__price = price
        self.is_available = True

    @property
    def get_price(self) :
        return self.__price
    
    @property
    def toggle_available(self):
        if self.is_available:
            return "Đang bán"
        else:
            return "Ngừng bán"
    
menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]

def show_drink() :
    if not menu :
        print("Danh sách trống!")
    else :
        print("--- DANH SÁCH ĐỒ UỐNG ---")
        print("Mã món | Tên món          | Giá bán | Trạng thái")
        print("-------------------------------------------------")
        for count in menu :
            print(f"{count.code:<5} | {count.name:<17} | {count.get_price:<7} | {count.toggle_available}")

def add_drink() :
    while True:
        add_code = input("Nhập mã món: ").strip().upper()
        if add_code == '':
            print("Mã ko được để trống!")
            continue
            
        for count in menu:
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
            new_drink = Drink(add_code, add_name, add_price)
            menu.append(new_drink)
            print(f"Thành công: Đã thêm món {add_name} vào thực đơn!")
            break
        
def update_drink() :
    while True:
        update_code = input("Nhập mã món cần cập nhật: ").strip().upper()
        if update_code == "" :
            print("Mã ko để trống!")
            continue
        for count in menu :
            if update_code == count.code :
                count.is_available = not count.is_available
                print(f"Đã cập nhật trạng thái món {update_code}")
                print(f"Trạng thái hiện tại: {count.toggle_available}")
                break
        else :
            print("Mã ko tồn tại!")
            continue
        break

def main() :
    while True :
        print("""
=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===

1. Xem danh sách đồ uống
2. Thêm đồ uống mới
3. Cập nhật trạng thái kinh doanh
4. Thoát chương trình

==============================================
""")
        choice = input("Chọn chức năng (1-4): ").strip()
        if choice == '1' :
            show_drink()
        elif choice == '2':
            add_drink()
        elif choice == '3':
            update_drink()
        elif choice == '4':
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
            break
        else :
            print("Vui lòng nhập")

if __name__ == "__main__" :
    main()