
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


    cart_items = [
            ["P001", "Dien thoai iPhone 15", 1, 13000000],
            ["P002", "Op lung Silicon", 2, 150000]
    ]
    sum_items = 0
    if choice == "1":
        print("\n-- CHI TIẾT GIỎ HÀNG --")
        print(f"STT | MÃ SP | {'TÊN SẢN PHẨM':<20} | SL | {'ĐƠN GIÁ':>12} | THÀNH TIỀN")
        print('-' * 70)
        
        total_quantity = 0   
        total_amount = 0 
        
        for i, cart in enumerate(cart_items, 1):
            subtotal = cart[2] * cart[3]
            total_quantity += cart[2]
            total_amount += subtotal
            
            print(f"{i:<3} | {cart[0]:<6} | {cart[1]:<20} | {cart[2]:>3} | {cart[3]:>12,} | {subtotal:>12,}")
        print(f"Tổng số lượng: {total_quantity} sản phẩm")
        print(f"Tổng thanh toán: {total_amount:,} VNĐ")
         
            

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

                    

