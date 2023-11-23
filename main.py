import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from tabulate import tabulate
from sinhvien import *
from NhanVien import NhanVien


# Bài 1: Chuyển đổi nhiệt độ từ Celsius sang Fahrenheit


def chuyen_do_Celsius_sang_Fahrenheit():
    while True:
        try:
            do_Celsius = float(input("Nhập nhiệt độ Celsius: "))
            do_Fahrenheit = do_Celsius * 9 / 5 + 32
            # Tạo bảng kết quả
            bang_ket_qua = [["Nhiệt độ Celsius", "Nhiệt độ Fahrenheit"],
                            [do_Celsius, do_Fahrenheit]]
            # In ra kết quả trong bảng
            print(tabulate(bang_ket_qua, headers="firstrow", tablefmt="pretty"))
            break
        except ValueError:
            print("Lỗi: Vui lòng nhập một số hợp lệ.")


def main_bai_1():
    print("Chào mừng bạn đến với chương trình của tôi!")

    hien_thi_bang_lua_chon()

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        chuyen_do_Celsius_sang_Fahrenheit()
    elif choice == 2:
        print("Kết thúc chương trình.")
    else:
        print("Lựa chọn không hợp lệ.")


# Bài 2: Tính tổng số nguyên tố, tổng ước số, và tổng số chẵn
def tong_so_nguyen_to_nho_hon_n(n):
    so_nguyen_to_nho_hon_n = [i for i in range(2, n) if la_so_nguyen_to(i)]
    return sum(so_nguyen_to_nho_hon_n)


def tinh_gia_tri_cho_n(n):
    try:
        if not isinstance(n, int):
            raise ValueError("Nhập không phải là số nguyên.")

        if not (50 <= n <= 150):
            raise ValueError("Nhập số tự nhiên n phải lớn hơn hoặc bằng 50 và nhỏ hơn hoặc bằng 150.")

        tong_so_nguyen_to = tong_so_nguyen_to_nho_hon_n(n)
        tong_ươc_so = sum([i for i in range(1, n + 1) if n % i == 0])
        tong_so_chan_for = sum([i for i in range(2, n + 1, 2)])
        tong_so_chan_while = 0
        i = 2
        while i <= n:
            tong_so_chan_while += i
            i += 2

        print(f"Các số nguyên tố nhỏ hơn {n}: {[i for i in range(2, n) if la_so_nguyen_to(i)]}")

        # Tạo bảng kết quả
        bang_ket_qua = [["Tổng số nguyên tố", "Tổng ước số", "Tổng số chẵn (for)", "Tổng số chẵn (while)"],
                        [tong_so_nguyen_to, tong_ươc_so, tong_so_chan_for, tong_so_chan_while]]

        # In ra kết quả trong bảng
        print(tabulate(bang_ket_qua, headers="firstrow", tablefmt="pretty"))

        return tong_so_nguyen_to, tong_ươc_so, tong_so_chan_for, tong_so_chan_while

    except ValueError as ve:
        print(f"Lỗi: {ve}")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None


def hambai2():
    while True:
        try:
            n = int(input("Nhập một số tự nhiên n (50 <= n <= 150): "))
            if 50 <= n <= 150:
                tinh_gia_tri_cho_n(n)
                break  # Thoát khỏi vòng lặp khi đã nhập đúng
            else:
                print("Số n không nằm trong khoảng [50, 150].")
        except ValueError:
            print("Lỗi: Vui lòng nhập một số tự nhiên.")


def main_bai_2():
    print("Chào mừng bạn đến với chương trình của tôi!")

    hien_thi_bang_lua_chon()

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        hambai2()
    elif choice == 2:
        print("Kết thúc chương trình.")
    else:
        print("Lựa chọn không hợp lệ.")


# Bài 3: Các hàm số
def dem_uoc_so(n):
    try:
        if not isinstance(n, int):
            raise ValueError("Lỗi: Vui lòng nhập một số tự nhiên.")

        if n < 1:
            raise ValueError("Lỗi: Số tự nhiên phải lớn hơn 0.")

        return len([i for i in range(1, n + 1) if n % i == 0])

    except ValueError as ve:
        print(ve)
        return None


def la_so_nguyen_to(n):
    try:
        if not isinstance(n, int):
            raise ValueError("Lỗi: Vui lòng nhập một số tự nhiên.")

        if n < 2:
            return 0

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return 0

        return 1

    except ValueError as ve:
        print(ve)
        return None


def dem_uoc_le(n):
    try:
        if not isinstance(n, int):
            raise ValueError("Lỗi: Vui lòng nhập một số tự nhiên.")

        if n < 1:
            raise ValueError("Lỗi: Số tự nhiên phải lớn hơn 0.")

        return len([i for i in range(1, n + 1) if n % i == 0 and i % 2 == 1])

    except ValueError as ve:
        print(ve)
        return None


def dem_so_nguyen_to_duoi_n(n):
    try:
        if not isinstance(n, int):
            raise ValueError("Lỗi: Vui lòng nhập một số tự nhiên.")

        if n < 2:
            return 0

        return len([i for i in range(2, n) if la_so_nguyen_to(i)])

    except ValueError as ve:
        print(ve)
        return None


def tong_uoc_so(n):
    try:
        if not isinstance(n, int):
            raise ValueError("Lỗi: Vui lòng nhập một số tự nhiên.")

        if n < 1:
            raise ValueError("Lỗi: Số tự nhiên phải lớn hơn 0.")

        return sum([i for i in range(1, n) if n % i == 0])

    except ValueError as ve:
        print(ve)
        return None


def hambai3():
    while True:
        try:
            n = int(input("Nhập một số tự nhiên n (50 <= n <= 150): "))
            if 50 <= n <= 150:
                # Tạo bảng kết quả
                bang_ket_qua = [
                    ["Số các ước số thực sự", f"{n} {'là' if la_so_nguyen_to(n) else 'không phải'} số nguyên tố",
                     "Số ước số lẻ", "Số nguyên tố nhỏ hơn n", "Tổng ước số thực sự"],
                    [dem_uoc_so(n), la_so_nguyen_to(n), dem_uoc_le(n), dem_so_nguyen_to_duoi_n(n), tong_uoc_so(n)]
                ]

                # In ra kết quả trong bảng
                print(tabulate(bang_ket_qua, headers="firstrow", tablefmt="pretty"))
                break
            else:
                print("Số n không nằm trong khoảng [50, 150]")
        except ValueError as ve:
            print(f"Lỗi: {ve}")


def main_bai_3():
    print("Chào mừng bạn đến với chương trình của tôi!")

    hien_thi_bang_lua_chon()

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        hambai3()
    elif choice == 2:
        print("Kết thúc chương trình.")
    else:
        print("Lựa chọn không hợp lệ.")


# Bài 4: Tạo dãy C từ A và B
def tao_day_so_C(A, B):
    try:
        if not (isinstance(A, list) and isinstance(B, list)):
            raise ValueError("Lỗi: A và B phải là danh sách (list) các số tự nhiên.")

        if len(A) != len(B):
            raise ValueError("Lỗi: A và B phải có cùng số phần tử.")

        C = [max(a, b) for a, b in zip(A, B)]
        return C

    except ValueError as ve:
        print(ve)
        return None


def hambai4():
    while True:
        try:
            A = [int(x) for x in input("Nhập dãy số A (cách nhau bằng dấu cách): ").split()]
            B = [int(x) for x in input("Nhập dãy số B (cách nhau bằng dấu cách): ").split()]
            C = tao_day_so_C(A, B)
            if C is not None:
                print(f"Dãy C: {C}")
                break
            else:
                print("Xảy ra lỗi. Vui lòng kiểm tra đầu vào.")
        except ValueError:
            print("Lỗi: Vui lòng nhập các số tự nhiên.")


def main_bai_4():
    print("Chào mừng bạn đến với chương trình của tôi!")

    hien_thi_bang_lua_chon()

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        hambai4()
    elif choice == 2:
        print("Kết thúc chương trình.")
    else:
        print("Lựa chọn không hợp lệ.")


# Bài 5: Kiểm tra xâu Str2 trong Str1
def xu_ly_xau(Str1, Str2, k):
    while True:
        try:
            if not (isinstance(Str1, str) and isinstance(Str2, str)):
                raise ValueError("Lỗi: Str1 và Str2 phải là xâu ký tự.")

            if not isinstance(k, int):
                raise ValueError("Lỗi: k phải là một số nguyên.")

            if k < 0 or k >= len(Str1):
                raise ValueError(f"Lỗi: k phải nằm trong khoảng từ 0 đến {len(Str1) - 1}.")

            print(f"a) {'Có' if Str2 in Str1 else 'Không có'} xâu Str2 trong xâu Str1")

            if Str2 in Str1:
                index = Str1.find(Str2)
                print(f"b) Xâu Str2 xuất hiện lần đầu tiên tại vị trí: {index}")

            new_str = Str1[:k] + Str2 + Str1[k:]
            print(f"c) Kết quả sau khi chèn xâu Str2 vào vị trí {k} trong xâu Str1: {new_str}")
            break
        except ValueError as ve:
            print(ve)


def hambai5():
    while True:
        try:
            Str1 = input("Nhập xâu Str1: ")
            Str2 = input("Nhập xâu Str2: ")
            k = int(input(f"Nhập số k (0 <= k < {len(Str1)}): "))
            xu_ly_xau(Str1, Str2, k)
            break
        except ValueError as ve:
            print(f"Lỗi: {ve}")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")


def main_bai_5():
    print("Chào mừng bạn đến với chương trình của tôi!")

    hien_thi_bang_lua_chon()

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        hambai5()
    elif choice == 2:
        print("Kết thúc chương trình.")
    else:
        print("Lựa chọn không hợp lệ.")


# Bài 6: Tạo tập hợp A, B, C
def sinh_tap_hop():
    try:
        A = set(random.sample(range(1, 1000), 100))
        B = set(random.sample(list(A), 20))
        C = set(random.sample(list(B), 10))
        return A, B, C
    except ValueError as ve:
        print(f"Lỗi: {ve}")
        return set(), set(), set()


def hambai6():
    try:
        tap_hop_A, tap_hop_B, tap_hop_C = sinh_tap_hop()
        print(f"a) Tập hợp A: {tap_hop_A}")
        print(f"b) Tập hợp B: {tap_hop_B}")
        print(f"c) Tập hợp C: {tap_hop_C}")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")


def main_bai_6():
    print("Chào mừng bạn đến với chương trình của tôi!")

    hien_thi_bang_lua_chon()

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        hambai6()
    elif choice == 2:
        print("Kết thúc chương trình.")
    else:
        print("Lựa chọn không hợp lệ.")


# Bài 7: Xử lý từ điển A
def xu_ly_tu_dien(A):
    try:
        diem_lon_nhat = max(A.values())
        mon_diem_lon_nhat = [(mon, diem) for mon, diem in A.items() if diem == diem_lon_nhat]
        diem_chan = {mon: diem for mon, diem in A.items() if diem % 2 == 0}
        diem_trung_binh = sum(A.values()) / len(A)
        tu_dien_moi = {mon: diem for mon, diem in A.items() if diem > 7}
        tu_dien_nguoc = {diem: mon for mon, diem in A.items()}

        return diem_lon_nhat, mon_diem_lon_nhat, diem_chan, diem_trung_binh, tu_dien_moi, tu_dien_nguoc
    except Exception as e:
        print(f"Lỗi không xác định trong quá trình xử lý từ điển: {e}")
        return None, None, None, None, None, None


def hambai7():
    try:
        A = {"Toán": 9, "Văn": 5, "Sử": 8, "Địa": 7}
        diem_lon_nhat, mon_diem_lon_nhat, diem_chan, diem_trung_binh, tu_dien_moi, tu_dien_nguoc = xu_ly_tu_dien(A)

        if diem_lon_nhat is not None:
            # Tổ chức dữ liệu thành danh sách 2 chiều
            bang_ket_qua = [
                ["Điểm lớn nhất", "Môn và điểm lớn nhất", "Điểm số chẵn", "Trung bình điểm", "Từ điển mới",
                 "Đảo ngược từ điển"],
                [diem_lon_nhat, mon_diem_lon_nhat, diem_chan, diem_trung_binh, tu_dien_moi, tu_dien_nguoc]
            ]

            # In ra kết quả trong bảng
            print(tabulate(bang_ket_qua, headers="firstrow", tablefmt="pretty"))
    except Exception as e:
        print(f"Lỗi không xác định: {e}")


def main_bai_7():
    print("Chào mừng bạn đến với chương trình của tôi!")

    hien_thi_bang_lua_chon()

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        hambai7()
    elif choice == 2:
        print("Kết thúc chương trình.")
    else:
        print("Lựa chọn không hợp lệ.")


# Bài 8: Module và Package

def hambai8():
    try:
        a, b, c = sinh_so_nguyen()

        # Tổ chức dữ liệu thành danh sách 2 chiều
        bang_ket_qua = [
            ["Phép toán", "Kết quả"],
            ["a) Tổng (a + b)", tinh_tong(a, b)],
            ["b) Tích (a * b)", tinh_tich(a, b)],
            ["c) Mũ (a ** b)", tinh_mu(a, b)],
            ["d) Căn bậc 2 (sqrt(a))", tinh_can_bac_hai(a)],
            ["e) Tan (tan(a))", tinh_tan(a)],
            ["f) Giải phương trình bậc 2 (ax^2 + bx + c = 0)", giai_ptb2(a, b, c)]
        ]

        # In ra kết quả trong bảng
        print(tabulate(bang_ket_qua, headers="firstrow", tablefmt="pretty", colalign=("left", "left")))

    except Exception as e:
        print(f"Lỗi không xác định: {e}")


def main_bai_8():
    print("Chào mừng bạn đến với chương trình của tôi!")

    hien_thi_bang_lua_chon()

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        hambai8()
    elif choice == 2:
        print("Kết thúc chương trình.")
    else:
        print("Lựa chọn không hợp lệ.")


# Bài 9: Đọc và ghi tệp
def doc_ghi_tep():
    try:
        with open('fin.txt', 'r', encoding='utf-8') as fin:
            n = int(fin.readline().strip())
            data = fin.readlines()

        with open('fout.txt', 'w', encoding='utf-8') as fout:
            tong_tat_ca = 0
            fout.write(str(tong_tat_ca) + '\n')
            for line in data:
                try:
                    so = [float(num) for num in line.split()]
                    tong_so = sum(so)
                    tong_tat_ca += tong_so
                    fout.write(f"{tong_so}\n")
                except ValueError as ve:
                    print(f"Lỗi khi đọc dòng từ tệp fin.txt: {ve}")
            fout.seek(0)
            fout.write(str(tong_tat_ca))

        print("Ghi tệp fout.txt thành công!")
    except FileNotFoundError:
        print("Không tìm thấy tệp fin.txt.")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")


def hien_thi_bang_lua_chon():
    table = [
        ["1", "Tiếp tục Chương Trình"],
        ["2", "Thực hiện chương trình khác"]
    ]
    headers = ["Lựa chọn", "Chức năng"]

    print(tabulate(table, headers, tablefmt="fancy_grid"))


def main_bai_9():
    print("Chào mừng bạn đến với chương trình của tôi!")

    hien_thi_bang_lua_chon()

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        doc_ghi_tep()
    elif choice == 2:
        print("Kết thúc chương trình.")
    else:
        print("Lựa chọn không hợp lệ.")


# Bài 10: Xử lý ngoại lệ
def xu_ly_ngoai_le():
    while True:
        try:
            a = int(input("Nhập số nguyên a: "))
            b = int(input("Nhập số nguyên b: "))
            result = a / b
            print(f"{a}/{b} = {result}")
            break
        except ValueError as ve:
            print(f"Lỗi: a và b phải là số nguyên. Chi tiết: {ve}")
        except ZeroDivisionError:
            print("Lỗi: b không được bằng 0.")


def main_bai_10():
    print("Chào mừng bạn đến với chương trình của tôi!")

    hien_thi_bang_lua_chon()

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        xu_ly_ngoai_le()
    elif choice == 2:
        print("Kết thúc chương trình.")
    else:
        print("Lựa chọn không hợp lệ.")


# Bài 11: Lập trình với đối tượng


def nhap_du_lieu_nhan_vien():
    danh_sach_nhan_vien = []
    while True:
        try:
            so_luong_nhan_vien = int(input("Nhập số lượng nhân viên: "))
            for i in range(so_luong_nhan_vien):
                hoten = input(f"Nhập họ tên của nhân viên {i + 1}: ")
                tuoi = int(input(f"Nhập tuổi của nhân viên {i + 1}: "))
                luong = float(input(f"Nhập lương của nhân viên {i + 1}: "))
                nhan_vien = NhanVien(hoten, tuoi, luong)
                danh_sach_nhan_vien.append(nhan_vien)
                break
        except ValueError as ve:
            print(f"Lỗi: {ve}. Vui lòng nhập lại thông tin.")
    return danh_sach_nhan_vien


def sap_xep_theo_tuoi_giam_dan(danh_sach_nhan_vien):
    return sorted(danh_sach_nhan_vien, key=lambda x: x.tuoi, reverse=True)


def ghi_danh_sach_nhan_vien_vao_tep_tin(danh_sach_nhan_vien):
    try:
        with open('NhanVien.txt', 'w', encoding='utf-8') as file:
            for nhan_vien in danh_sach_nhan_vien:
                file.write(f"{nhan_vien.hoten}, {nhan_vien.tuoi}, {nhan_vien.luong}\n")
        print("Ghi tệp NhanVien.txt thành công!")
    except Exception as e:
        print(f"Lỗi khi ghi tệp: {e}")


def doc_danh_sach_nhan_vien_tu_tep_tin():
    danh_sach_nhan_vien = []
    try:
        with open('NhanVien.txt', 'r', encoding='utf-8') as file:
            for line in file:
                hoten, tuoi, luong = line.strip().split(', ')
                nhan_vien = NhanVien(hoten, int(tuoi), float(luong))
                danh_sach_nhan_vien.append(nhan_vien)
    except FileNotFoundError:
        print("Không tìm thấy tệp NhanVien.txt.")
    except Exception as e:
        print(f"Lỗi khi đọc tệp: {e}")
    return danh_sach_nhan_vien


def in_danh_sach_nhan_vien(danh_sach_nhan_vien):
    if not danh_sach_nhan_vien:
        print("Danh sách nhân viên trống.")
        return

    headers = ["Họ Tên", "Tuổi", "Lương"]
    table_data = [[nv.hoten, nv.tuoi, nv.luong] for nv in danh_sach_nhan_vien]
    print(tabulate(table_data, headers, tablefmt="fancy_grid"))


##### HÀM MAIN BÀI 11 ####
def hambai11():
    try:
        danh_sach_nhan_vien = nhap_du_lieu_nhan_vien()
        print("\nDanh sách nhân viên sau khi nhập:")
        in_danh_sach_nhan_vien(danh_sach_nhan_vien)

        danh_sach_nhan_vien_sap_xep = sap_xep_theo_tuoi_giam_dan(danh_sach_nhan_vien)
        print("\nDanh sách nhân viên sau khi sắp xếp theo tuổi giảm dần:")
        in_danh_sach_nhan_vien(danh_sach_nhan_vien_sap_xep)

        ghi_danh_sach_nhan_vien_vao_tep_tin(danh_sach_nhan_vien)
        print("\nDanh sách nhân viên sau khi ghi vào tệp NhanVien.txt:")
        in_danh_sach_nhan_vien(doc_danh_sach_nhan_vien_tu_tep_tin())
    except Exception as e:
        print(f"Lỗi chung: {e}")


def main_bai_11():
    print("Chào mừng bạn đến với chương trình của tôi!")

    hien_thi_bang_lua_chon()

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        hambai11()
    elif choice == 2:
        print("Kết thúc chương trình.")
    else:
        print("Lựa chọn không hợp lệ.")


#####  BÀI 12 ####
def tao_vecto_x(m):
    return np.arange(-3, 6)[:m]


def tao_ma_tran_A_B(m, n):
    A = np.random.randint(-10, 11, size=(m, n))
    B = np.random.randint(-10, 11, size=(n, m))  # Đảo số hàng và số cột của ma trận B
    return A, B


def tao_ma_tran_C(n, m):
    return np.random.randint(-10, 11, size=(n, m))


def tinh_tich_vecto_ma_tran(x, A):
    return np.dot(x, A)


def tinh_tich_hai_ma_tran(A, B):
    return np.dot(A, B)


def tinh_tich_hai_ma_tran_chuyen_vi(C, B):
    Ct = np.transpose(C)
    return np.dot(Ct, B)


def hambai12():
    while True:
        try:
            m = int(input("Nhập số phần tử của vecto x và số hàng của ma trận A: "))
            n = int(input("Nhập số cột của ma trận A và B: "))

            # a) Tạo vecto x
            x = tao_vecto_x(m)

            # b) Tạo ma trận A và B
            A, B = tao_ma_tran_A_B(m, n)

            # c) Tạo ma trận C
            C = tao_ma_tran_C(n, m)

            # In thông tin
            print("\nVecto x:")
            print(x)

            print("\nMa trận A:")
            print(A)

            print("\nMa trận B:")
            print(B)

            print("\nMa trận C:")
            print(C)

            # a) Tính tích của vecto x và ma trận A
            tich_x_A = tinh_tich_vecto_ma_tran(x, A)
            print("\nTích của vecto x và ma trận A:")
            print(tich_x_A)

            # b) Tính tích hai ma trận A và B
            tich_A_B = tinh_tich_hai_ma_tran(A, B)
            print("\nTích hai ma trận A và B:")
            print(tich_A_B)

            # c) Tính tích hai ma trận Ct và B
            tich_Ct_B = tinh_tich_hai_ma_tran_chuyen_vi(C, B)
            print("\nTích hai ma trận Ct và B:")
            print(tich_Ct_B)
            break
        except ValueError as ve:
            print(f"Lỗi chương trình chính: {ve}")
        except Exception as e:
            print(f"Lỗi chương trình chính: {e}")


##### HÀM MAIN BÀI 12 ####
def main_bai_12():
    print("Chào mừng bạn đến với chương trình của tôi!")

    hien_thi_bang_lua_chon()

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        hambai12()
    elif choice == 2:
        print("Kết thúc chương trình.")
    else:
        print("Lựa chọn không hợp lệ.")


#####  BÀI 13 ####
def tinh_gia_tri_ham_so(x):
    try:
        y = x ** 4 - 2 * x ** 2 - 3
        return y
    except Exception as e:
        print(f"Lỗi khi tính giá trị của hàm số y: {e}")
        return None


def tinh_gia_tri_dao_ham(x, bac_dao_ham=1):
    try:
        if bac_dao_ham == 1:
            y_prime = 4 * x ** 3 - 4 * x
            return y_prime
        elif bac_dao_ham == 2:
            y_double_prime = 12 * x ** 2 - 4
            return y_double_prime
        elif bac_dao_ham == 3:
            y_triple_prime = 24 * x
            return y_triple_prime
        else:
            raise ValueError("Chỉ hỗ trợ đến đạo hàm bậc 3.")
    except Exception as e:
        print(f"Lỗi khi tính giá trị đạo hàm: {e}")
        return None


def hambai13():
    try:
        x_gia_tri = np.linspace(-10, 10, 1000)

        y_gia_tri = tinh_gia_tri_ham_so(x_gia_tri)
        y_prime_gia_tri = tinh_gia_tri_dao_ham(x_gia_tri, bac_dao_ham=1)
        y_double_prime_gia_tri = tinh_gia_tri_dao_ham(x_gia_tri, bac_dao_ham=2)
        y_triple_prime_gia_tri = tinh_gia_tri_dao_ham(x_gia_tri, bac_dao_ham=3)

        if all(val is not None for val in [y_gia_tri, y_prime_gia_tri, y_double_prime_gia_tri, y_triple_prime_gia_tri]):
            plt.figure(figsize=(10, 6))

            plt.plot(x_gia_tri, y_gia_tri, label='y = x^4 - 2x^2 - 3')
            plt.plot(x_gia_tri, y_prime_gia_tri, label="y'")
            plt.plot(x_gia_tri, y_double_prime_gia_tri, label="y''")
            plt.plot(x_gia_tri, y_triple_prime_gia_tri, label="y'''")

            plt.title('Đồ thị hàm số và đạo hàm')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.legend()
            plt.grid(True)
            plt.show()
    except Exception as e:
        print(f"Lỗi chương trình chính: {e}")


##### HÀM MAIN BÀI 13 ####
def main_bai_13():
    print("Chào mừng bạn đến với chương trình của tôi!")

    hien_thi_bang_lua_chon()

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        hambai13()
    elif choice == 2:
        print("Kết thúc chương trình.")
    else:
        print("Lựa chọn không hợp lệ.")


#####  BÀI 14 ####
def ve_mat_yen_ngua():
    try:
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        x, y = np.meshgrid(x, y)
        z = (x / 3) ** 2 - (y / 2) ** 2

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, cmap='plasma', color='purple', alpha=0.8)  # Thay đổi màu sắc ở đây

        ax.set_title('Đồ thị mặt yên ngựa')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
    except Exception as e:
        print(f"Lỗi khi vẽ đồ thị mặt yên ngựa: {e}")



def ve_mat_hyperbolic():
    try:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        u = np.linspace(-3, 3, 100)
        v = np.linspace(-3, 3, 100)
        u, v = np.meshgrid(u, v)
        a = 3
        b = 5
        c = 2
        x = a * np.cosh(u) * np.cos(v)
        y = b * np.cosh(u) * np.sin(v)
        z = c * np.sinh(u)

        ax.plot_surface(x, y, z, cmap='plasma', color='purple', alpha=0.8)  # Thay đổi màu sắc ở đây

        ax.set_title("Đồ thị mặt hyperbolic 1 tầng")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        plt.show()
    except Exception as e:
        print(f"Lỗi khi vẽ đồ thị mặt yên ngựa: {e}")


def ve_mat_cau():
    try:
        phi = np.linspace(0, np.pi, 100)
        theta = np.linspace(0, 2 * np.pi, 100)
        phi, theta = np.meshgrid(phi, theta)
        x = 2 * np.sin(phi) * np.cos(theta) - 2
        y = 2 * np.sin(phi) * np.sin(theta) + 1
        z = 2 * np.cos(phi) + 4

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, cmap='plasma', color='purple', alpha=0.8)  # Thay đổi màu sắc ở đây
        ax.set_title('Đồ thị mặt cầu')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
    except Exception as e:
        print(f"Lỗi khi vẽ đồ thị mặt cầu: {e}")


def hambai14():
    try:
        ve_mat_yen_ngua()
        ve_mat_hyperbolic()
        ve_mat_cau()
    except Exception as e:
        print(f"Lỗi chương trình chính: {e}")


##### HÀM MAIN BÀI 14 ####
def main_bai_14():
    print("Chào mừng bạn đến với chương trình của tôi!")

    hien_thi_bang_lua_chon()

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        hambai14()
    elif choice == 2:
        print("Kết thúc chương trình.")
    else:
        print("Lựa chọn không hợp lệ.")


#####  BÀI 15  ####

def giai_he_phuong_trinh_tuyen_tinh():
    try:
        x, y, z = sp.symbols('x y z')
        pt1 = sp.Eq(2 * x - 5 * y + z, -5)
        pt2 = sp.Eq(4 * x + 2 * y - 2 * z, 2)
        pt3 = sp.Eq(x + y - z, 0)
        ket_qua = sp.solve((pt1, pt2, pt3), (x, y, z))
        print(f"Giải hệ phương trình: {ket_qua}")
    except Exception as e:
        print(f"Lỗi khi giải hệ phương trình: {e}")


def tinh_gioi_han():
    try:
        x = sp.symbols('x')
        f = ((x ** 3 - 3 * x ** 2) ** (1 / 3) + (x ** 2 - 2 * x) ** (1 / 2))
        ket_qua_gioi_han = sp.limit(f, x, 5)
        print(f"Giới hạn của hàm f khi x tiến tới 5: {ket_qua_gioi_han}")
    except Exception as e:
        print(f"Lỗi khi tính giới hạn: {e}")


def tinh_dao_ham():
    try:
        x = sp.symbols('x')
        f = (2 * x - 1) / (x + 2)
        dao_ham = sp.diff(f, x)
        print(f"Đạo hàm của hàm f: {dao_ham}")
    except Exception as e:
        print(f"Lỗi khi tính đạo hàm: {e}")


def tinh_nguyen_ham_vo_han():
    try:
        x = sp.symbols('x')
        f = x / (x ** 2 + 1)
        nguyen_ham_vo_han = sp.integrate(f, x)
        print(f"Nguyên hàm của hàm f: {nguyen_ham_vo_han}")
    except Exception as e:
        print(f"Lỗi khi tính nguyên hàm: {e}")


def tinh_tich_phan_xac_dinh():
    try:
        x = sp.symbols('x')
        f = (1 - x * sp.tan(x)) / (x ** 2 * sp.cos(x) + x)
        tich_phan_xac_dinh = sp.integrate(f, (x, 0, 2 * sp.pi / 3))
        print(f"Tích phân của hàm f từ 0 đến 2pi/3: {tich_phan_xac_dinh}")
    except Exception as e:
        print(f"Lỗi khi tính tích phân: {e}")


def hambai15():
    try:
        giai_he_phuong_trinh_tuyen_tinh()
        tinh_gioi_han()
        tinh_dao_ham()
        tinh_nguyen_ham_vo_han()
        tinh_tich_phan_xac_dinh()
    except Exception as e:
        print(f"Lỗi chương trình chính: {e}")


##### HÀM MAIN BÀI 15  ####

def main_bai_15():
    print("Chào mừng bạn đến với chương trình của tôi!")

    hien_thi_bang_lua_chon()

    choice = int(input("Nhập lựa chọn của bạn: "))

    if choice == 1:
        hambai15()
    elif choice == 2:
        print("Kết thúc chương trình.")
    else:
        print("Lựa chọn không hợp lệ.")
        #####MENU CHÍNH ####

def print_menu():
    menu = [
        ["1", "Viết chương trình chuyển đổi nhiệt độ"],
        ["2", "Tính tổng số nguyên tố, tổng ước số, tổng số chẵn"],
        ["3", "Xử lý hàm số"],
        ["4", "Tạo dãy số và ước số chung lớn nhất"],
        ["5", "Kiểm tra xâu và chèn xâu vào xâu khác"],
        ["6", "Sinh tập hợp ngẫu nhiên"],
        ["7", "Xử lý từ điển"],
        ["8", "Sử dụng module và phép toán cơ bản"],
        ["9", "Đọc và ghi tệp"],
        ["10", "Xử lý ngoại lệ"],
        ["11", "Xử lý đối tượng"],
        ["12", "Sử dụng thư viện NumPy"],
        ["13", "Vẽ đồ thị đạo hàm"],
        ["14", "Vẽ các hình không gian"],
        ["15", "Sử dụng thư viện SymPy"],
        ["0", "Thoát chương trình"]
    ]
    print(tabulate(menu, headers=["Chọn", "Bài tập"], tablefmt="pretty", colalign=("left", "left")))


# Chương trình chính
def main():
    while True:
        try:
            print_menu()
            choice = int(input("Chọn bài tập (0-15):"))
            if choice == 0:
                print("Kết thúc chương trình.")
                break
            elif choice == 1:
                main_bai_1()
            elif choice == 2:
                main_bai_2()
            elif choice == 3:
                main_bai_3()
            elif choice == 4:
                main_bai_4()
            elif choice == 5:
                main_bai_5()
            elif choice == 6:
                main_bai_6()
            elif choice == 7:
                main_bai_7()
            elif choice == 8:
                main_bai_8()
            elif choice == 9:
                main_bai_9()
            elif choice == 10:
                main_bai_10()
            elif choice == 11:
                main_bai_11()
            elif choice == 12:
                main_bai_12()
            elif choice == 13:
                main_bai_13()
            elif choice == 14:
                main_bai_14()
            elif choice == 15:
                hambai15()
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        except ValueError:
            print("Lỗi: Vui lòng nhập một số tự nhiên.")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")
        try:
            input("Nhấn Enter để tiếp tục...")
        except KeyboardInterrupt:
            print("Thoát khỏi chương trình.")
            break


if __name__ == "__main__":
    main()
