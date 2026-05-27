


while True:
    choice = input("""
===== HỆ THỐNG QUẢN LÝ GIỎ HÀNG =====
1. Xem chi tiết giỏ hàng và Tổng tiền
2. Thêm sản phẩm mới hoặc Tăng số lượng
3. Cập nhật số lượng sản phẩm
4. Xóa sản phẩm khỏi giỏ hàng
5. Thoát chương trình
================================================
Nhập lựa chọn của bạn (1-5): 
""")

    # Khởi tạo giỏ hàng lần đầu
    if 'cart_items' not in globals():
        cart_items = [
            ["P001", "Dien thoai iPhone 15", 1, 25000000],
            ["P002", "Op lung Silicon", 2, 150000]
        ]

    if choice == "1":
        print("\n-- DANH SÁCH SẢN PHẨM TRONG GIỎ HÀNG --")
        if not cart_items:
            print("Giỏ hàng hiện đang trống.")
        else:
            print("="*80)
            print(f"{'STT':<4} {'Mã SP':<8} {'Tên Sản Phẩm':<30} {'Số Lượng':<10} {'Đơn Giá':<15} {'Thành Tiền':<15}")
            print("="*80)
            
            total_qty = 0
            total_money = 0
            
            for i, item in enumerate(cart_items, 1):
                code, name, qty, price = item
                subtotal = qty * price
                total_qty += qty
                total_money += subtotal
                print(f"{i:<4} {code:<8} {name[:28]:<30} {qty:<10} {price:>12,}đ {subtotal:>13,}đ")
            
            print("="*80)
            print(f"Tổng số lượng: {total_qty} sản phẩm")
            print(f"Tổng tiền: {total_money:,} VNĐ")
            print("="*80)

    elif choice == "2":
        code = input("Nhập mã sản phẩm: ").strip().upper()
        name = input("Nhập tên sản phẩm: ").strip()
        qty = int(input("Nhập số lượng: "))
        price = int(input("Nhập đơn giá: "))
        
        # Kiểm tra tồn tại để cộng dồn
        found = False
        for item in cart_items:
            if item[0] == code:
                item[2] += qty
                print(f"Đã tăng số lượng {code} thêm {qty}.")
                found = True
                break
        
        if not found:
            cart_items.append([code, name, qty, price])
            print(f"Đã thêm sản phẩm {code} thành công!")

    elif choice == "3":
        code = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
        qty = int(input("Nhập số lượng mới: "))
        
        for item in cart_items:
            if item[0] == code:
                item[2] = qty
                print(f"Đã cập nhật số lượng {code} thành {qty}.")
   
                break


    elif choice == "4":
        code = input("Nhập mã sản phẩm cần xóa: ").strip().upper()

        for i in range(len(cart_items)):
            if cart_items[i][0] == code:
                cart_items.pop(i)
                print(f"Đã xóa sản phẩm {code} thành công!")
                break
 

    elif choice == "5":
        print("Hệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!")
        break
    
    else:
        print("Lựa chọn không hợp lệ! Vui lòng nhập từ 1 đến 5.")

                    

