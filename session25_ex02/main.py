'''
Phân tích
1. Hậu quả của thuộc tính tự do (public): Làm sai lệch dữ liệu hệ thống ,các phép toán cộng trừ điểm sau này sẽ bị lỗi
2. Dùng @points.setter
3. Vì is_eligible_for_voucher chỉ kiểm tra giá trị hóa đơn (bill_amount) hoàn toàn ko liên quan đến self.customer_name hay self.points
4. DÙng @staticmethod
Sự khác biệt
 @classmethod: bắt buộc phải nhận tham số đầu tiên là cls, để truy cập, sửa đổi biến
 @staticmethod: không nhận bất kỳ tham số mặc định nào (không có self, không có cls), nó hoạt động như một hàm độc lập
'''

# Sửa lỗi
class MemberCard:
    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        if type(points) == int and points >= 0:
            self.__points = points
        else:
            self.__points = 0

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, new_points):
        if type(new_points) == int and new_points >= 0:
            self.__points = new_points
        else:
            print("Dữ liệu điểm không hợp lệ!")

    def add_points(self, amount):
        if amount > 0:
            self.__points += amount

    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000

card1 = MemberCard("Le Van C", 100)

card1.points = -50 
card1.points = "một trăm"

result = MemberCard.is_eligible_for_voucher(250000) 

print(f"Khách hàng: {card1.customer_name} | Điểm hiện tại: {card1.points}")
print(f"Hóa đơn 250k có được tặng Voucher không? {result}")