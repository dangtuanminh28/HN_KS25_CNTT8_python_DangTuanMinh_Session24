import re

class MemberCard():
    point_value_vnd = 1000
    def __init__(self, card_id: str, name: str, points: int = 0):
        self.card_id = card_id
        self.name = name
        self.__points = points
        self.__tier = "Standard"
        self._update_tier()

    def _update_tier(self):
        if self.__points >= 100:
            self.__tier = "VIP"
        else:
            self.__tier = "Standard"

    @property
    def points(self):
        return self.__points

    @property
    def tier(self):
        return self.__tier

    def add_points(self, amount: int):
        """Tích điểm trực tiếp"""
        if amount > 0:
            self.__points += amount
            self._update_tier()

    def earn_points(self, bill_amount: int) -> int:
        """Chức năng 3: Tích điểm dựa trên tổng tiền hóa đơn"""
        points_earned = bill_amount // 10000
        if points_earned > 0:
            self.add_points(points_earned)
        return points_earned

    def use_points(self, amount: int) -> bool:
        """Sử dụng điểm đổi ưu đãi"""
        if (amount > 0) and (amount <= self.__points):
            self.__points -= amount
            self._update_tier()
            return True
        return False

    @staticmethod
    def is_valid_card_id(card_id: str) -> bool:
        """Chức năng 2: Kiểm tra định dạng mã thẻ định dạng RCxx"""
        return bool(re.match(r"^RC\d{2}$", card_id))

    def redeem_points(self, points_to_use: int) -> int:
        """Chức năng 4: Đổi điểm lấy tiền giảm giá"""
        if (points_to_use > 0) and (points_to_use <= self.__points):
            self.__points -= points_to_use
            self._update_tier()
            discount_amount = points_to_use * MemberCard.point_value_vnd
            return discount_amount
        return -1
    
    @classmethod
    def update_point_value(cls, new_value: int):
        """Chức năng 5: Cập nhật tỷ giá quy đổi điểm trên toàn hệ thống"""
        if new_value > 0:
            cls.point_value_vnd = new_value

member_list = [
    MemberCard("RC01", "Nguyen Van A", 150),
    MemberCard("RC02", "Tran Thi B", 20),
    MemberCard("RC03", "Pham Thi C", 105)
]

def show_member_list():
    """Chức năng 1. Xem danh sách thẻ thành viên"""
    print("=== DANH SÁCH THẺ THÀNH VIÊN ===")
    if not member_list:
        print("Hệ thống chưa có thẻ thành viên nào.")
        return
        
    for i, member in enumerate(member_list, start=1):
        print(f"{i}. Mã: {member.card_id:<4} | Tên: {member.name:<15} | "
              f"Điểm: {member.points:<4} | Hạng: {member.tier}")
        

def add_member():
    """Chức năng 2. Đăng ký thẻ mới"""
    print("--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")
    while True:
        card_id = input("Nhập mã thẻ: ").strip().upper()
        
        if not card_id:
            print("Mã thẻ không được để trống! Vui lòng nhập lại.")
            continue
            
        if not MemberCard.is_valid_card_id(card_id):
            print("Mã thẻ không hợp lệ! Phải bắt đầu bằng 'RC' và 2 chữ số (Ví dụ: RC04).")
            continue
        for count in member_list:
            if card_id == count.card_id:
                print("Mã thẻ đã tồn tại trong hệ thống! Vui lòng nhập lại.")
                break
        else:
            break
            
    while True:
        name = input("Nhập tên khách hàng: ").strip().title()
        if not name:
            print("Tên khách hàng không được để trống! Vui lòng nhập lại.")
            continue
        break

    new_card = MemberCard(card_id, name)
    member_list.append(new_card)
    
    print("\nĐăng ký thẻ thành viên thành công!")
    print(f"Mã thẻ: {new_card.card_id}")
    print(f"Tên khách hàng: {new_card.name}")
    print(f"Điểm ban đầu: {new_card.points}")
    print(f"Hạng thẻ: {new_card.tier}")


def shop_earn_points():
    """Chức năng 3. Khách mua hàng (Tích điểm)"""
    print("--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")
    target_member = None
    while True:
        card_id = input("Nhập mã thẻ: ").strip().upper()
        if not card_id:
            print("Mã thẻ không được để trống! Vui lòng nhập lại.")
            continue
            
        for member in member_list:
            if member.card_id == card_id:
                target_member = member
                break
        if target_member:
            break
        else:
            print("Mã thẻ không tồn tại trong hệ thống! Vui lòng kiểm tra lại.")

    while True:
        try:
            bill_amount = int(input("Nhập tổng tiền hóa đơn: "))
            if bill_amount <= 0:
                print("Số tiền hóa đơn phải lớn hơn 0 VNĐ! Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Hóa đơn không hợp lệ! Vui lòng nhập vào một số nguyên.")

    old_tier = target_member.tier
    points_earned = target_member.earn_points(bill_amount)
    
    print(f"Khách hàng: {target_member.name}")
    print(f"Hóa đơn: {bill_amount:,} VNĐ")
    print(f"Số điểm được tích: {points_earned}")
    print(f"Tổng điểm hiện tại: {target_member.points}")
    
    if old_tier == "Standard" and target_member.tier == "VIP":
        print("Chúc mừng! Khách hàng đã được nâng hạng lên VIP.")
    
    print(f"Hạng thẻ hiện tại: {target_member.tier}")


def shop_spent_point():
    """Chức năng 4. Khách dùng điểm (Đổi ưu đãi)"""
    print("--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")
    target_member = None
    while True:
        card_id = input("Nhập mã thẻ: ").strip().upper()
        if not card_id:
            print("Mã thẻ không được để trống! Vui lòng nhập lại.")
            continue
        for member in member_list:
            if member.card_id == card_id:
                target_member = member
                break
        else:
            print("Mã thẻ không tồn tại trong hệ thống! Vui lòng kiểm tra lại.")
            continue
        break

    while True:
        try:
            points_to_use = int(input("Nhập số điểm muốn sử dụng: "))
            if points_to_use <= 0:
                print("Số điểm sử dụng phải lớn hơn 0! Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Số điểm không hợp lệ! Vui lòng nhập vào một số nguyên.")

    discount_amount = target_member.redeem_points(points_to_use)
    
    if discount_amount != -1:
        print(f"Đã trừ {points_to_use} điểm.")
        print(f"Khách hàng được giảm giá {discount_amount:,} VNĐ vào hóa đơn!")
        print(f"Số điểm còn lại: {target_member.points}")
        print(f"Hạng thẻ hiện tại: {target_member.tier}")
    else:
        print("Không thể đổi điểm!")
        print("Số điểm muốn sử dụng vượt quá số điểm hiện có.")
        print(f"Điểm hiện tại của khách: {target_member.points}")
        print("Điểm cũ được giữ nguyên:")
        print(f"Số điểm sau giao dịch: {target_member.points}")

def update_point():
    """Chức năng 5. Cập nhật tỷ giá quy đổi điểm (Hệ thống)"""
    print("--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")
    print(f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
    
    while True:
        try:
            new_value = int(input("Nhập tỷ giá mới cho 1 điểm: "))
            if new_value <= 0:
                print("Tỷ giá phải lớn hơn 0 VNĐ! Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Tỷ giá không hợp lệ! Vui lòng nhập vào một số nguyên (Ví dụ: 2000).")

    MemberCard.update_point_value(new_value)
    print("Cập nhật tỷ giá thành công!")
    print(f"Tỷ giá mới: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")

def main():
    while True :
        print("""
===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====
1. Xem danh sách thẻ thành viên
2. Đăng ký thẻ mới
3. Khách mua hàng (Tích điểm)
4. Khách dùng điểm (Đổi ưu đãi)
5. Cập nhật tỷ giá quy đổi điểm (Hệ thống)
6. Thoát chương trình
====================================================== 
""")
        choice = input("Chọn chức năng (1-6): ").strip()
        if choice == '1' :
            show_member_list()
        elif choice == '2' :
            add_member()
        elif choice == '3' :
            shop_earn_points()
        elif choice == '4' :
            shop_spent_point()
        elif choice == '5' :
            update_point()
        elif choice == '6' :
            print("")
            break
        else :
            print("Vui lòng nhập lại!")

if __name__  == "__main__" :
    main()