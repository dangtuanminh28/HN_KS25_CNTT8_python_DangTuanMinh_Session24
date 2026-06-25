'''
Phân tích
1. Vi phạm tính chất: Việc gán trực tiếp từ bên ngoài vi phạm Tính đóng gói
2. Kích hoạt Name Mangling: Đổi tên biến thành __total_amount
3. Dùng @property
4. self.vat_rate = new_rate đang tạo một biến mới nằm riêng bên trong order_table1, làm cho nó bị tách rời khỏi biến chung của lớp
5. Dùng @classmethod , tham số thay thế cho self: cls
'''

# Sửa lỗi
class CoffeeOrder:
    vat_rate = 0.10

    def __init__(self, table_number):
        self.table_number = table_number
        self.__total_amount = 0

    def add_item(self, price):
        if price > 0:
            self.__total_amount += price

    def get_total_amount(self):
        return self.__total_amount

    def calculate_final_bill(self):
        return self.__total_amount + (self.__total_amount * CoffeeOrder.vat_rate)

    def update_vat_rate(self, new_rate):
        CoffeeOrder.vat_rate = new_rate

order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")

order_table1.add_item(50000)
order_table2.add_item(30000)

order_table1.total_amount = 0 

order_table1.update_vat_rate(0.08)

print(f"Tổng tiền Bàn 1 (sau VAT): {order_table1.calculate_final_bill()} VNĐ")
print(f"Thuế VAT đang áp dụng cho Bàn 1: {order_table1.vat_rate}")
print(f"Thuế VAT đang áp dụng cho Bàn 2: {order_table2.vat_rate}")