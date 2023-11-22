import random
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp


# Bài 1: Chuyển đổi nhiệt độ từ Celsius sang Fahrenheit
def celsius_to_fahrenheit():
    try:
        celsius = float(input("Nhập nhiệt độ Celsius: "))
        fahrenheit = celsius * 9 / 5 + 32
        print(f"Nhiệt độ Fahrenheit tương ứng: {fahrenheit}")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số hợp lệ.")


# Bài 2: Tính tổng số nguyên tố, tổng ước số, và tổng số chẵn
def calculate_values_for_n(n):
    try:
        if not isinstance(n, int):
            raise ValueError("Nhập không phải là số nguyên.")

        if n < 2:
            raise ValueError("Nhập số tự nhiên n phải lớn hơn hoặc bằng 2.")

        prime_sum = sum([i for i in range(n) if is_prime(i)])
        divisor_sum = sum([i for i in range(1, n + 1) if n % i == 0])
        even_sum_for = sum([i for i in range(2, n + 1, 2)])
        even_sum_while = 0
        i = 2
        while i <= n:
            even_sum_while += i
            i += 2
        return prime_sum, divisor_sum, even_sum_for, even_sum_while

    except ValueError as ve:
        print(f"Lỗi: {ve}")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None


# Bài 3: Các hàm số
def count_divisors(n):
    try:
        if not isinstance(n, int):
            raise ValueError("Lỗi: Vui lòng nhập một số tự nhiên.")

        if n < 1:
            raise ValueError("Lỗi: Số tự nhiên phải lớn hơn 0.")

        return len([i for i in range(1, n + 1) if n % i == 0])

    except ValueError as ve:
        print(ve)
        return None


def is_prime(n):
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


def count_odd_divisors(n):
    try:
        if not isinstance(n, int):
            raise ValueError("Lỗi: Vui lòng nhập một số tự nhiên.")

        if n < 1:
            raise ValueError("Lỗi: Số tự nhiên phải lớn hơn 0.")

        return len([i for i in range(1, n + 1) if n % i == 0 and i % 2 == 1])

    except ValueError as ve:
        print(ve)
        return None


def count_primes_below_n(n):
    try:
        if not isinstance(n, int):
            raise ValueError("Lỗi: Vui lòng nhập một số tự nhiên.")

        if n < 2:
            return 0

        return len([i for i in range(2, n) if is_prime(i)])

    except ValueError as ve:
        print(ve)
        return None


def sum_divisors(n):
    try:
        if not isinstance(n, int):
            raise ValueError("Lỗi: Vui lòng nhập một số tự nhiên.")

        if n < 1:
            raise ValueError("Lỗi: Số tự nhiên phải lớn hơn 0.")

        return sum([i for i in range(1, n) if n % i == 0])

    except ValueError as ve:
        print(ve)
        return None


def main_bai_3():
    try:
        n = int(input("Nhập một số tự nhiên n (50 <= n <= 150): "))
        if 50 <= n <= 150:
            print(f"Số ước số thực sự của {n}: {count_divisors(n)}")
            print(f"{n} {'là' if is_prime(n) else 'không phải'} số nguyên tố")
            print(f"Số ước số lẻ của {n}: {count_odd_divisors(n)}")
            print(f"Số nguyên tố nhỏ hơn {n}: {count_primes_below_n(n)}")
            print(f"Tổng các ước số thực sự của {n}: {sum_divisors(n)}")
        else:
            print("Số n không nằm trong khoảng [50, 150]")
    except ValueError as ve:
        print(f"Lỗi: {ve}")


# Bài 4: Tạo dãy C từ A và B
def create_sequence_C(A, B):
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


# Bài 5: Kiểm tra xâu Str2 trong Str1
def check_string_in_string(Str1, Str2):
    try:
        if not (isinstance(Str1, str) and isinstance(Str2, str)):
            raise ValueError("Lỗi: Str1 và Str2 phải là xâu ký tự.")

        count = Str1.count(Str2)
        print(f"Str2 {'có' if count > 0 else 'không có'} trong Str1")
        print(f"Str2 xuất hiện {count} lần trong Str1")

    except ValueError as ve:
        print(ve)


# Bài 6: Tạo tập hợp A, B, C
def create_sets():
    try:
        A = set(random.sample(range(1, 1000), 100))
        B = set(random.sample(A, 20))
        C = set(random.sample(B, 10))
        return A, B, C
    except ValueError as ve:
        print(f"Lỗi: {ve}")
        return set(), set(), set()


# Bài 7: Xử lý từ điển A
def process_dictionary(A):
    try:
        max_value = max(A.values())
        max_subjects = [subject for subject, score in A.items() if score == max_value]
        even_scores = {subject: score for subject, score in A.items() if score % 2 == 0}
        avg_score = sum(A.values()) / len(A)
        new_dict = {subject: score for subject, score in A.items() if score > 7}
        reversed_dict = {v: k for k, v in A.items()}
        return max_value, max_subjects, even_scores, avg_score, new_dict, reversed_dict
    except Exception as e:
        print(f"Lỗi không xác định trong quá trình xử lý từ điển: {e}")
        return None, None, None, None, None, None


# Bài 8: Module và Package
# Module student_math.py:


def addition(a, b):
    return a + b


def multiplication(a, b):
    return a * b


def power(a, b):
    return a ** b


def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError as ve:
        print(f"Lỗi khi tính căn bậc 2: {ve}")
        return None


def quadratic_eq(a, b, c):
    try:
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return x1, x2
        elif discriminant == 0:
            x = -b / (2 * a)
            return x
        else:
            return "No real roots"
    except ValueError as ve:
        print(f"Lỗi khi giải phương trình bậc 2: {ve}")
        return None


# Main program for Bài 8
def main_bai_8():
    a = random.randint(1, 100)
    b = random.randint(1, 5)
    c = random.randint(1, 50)

    try:
        print(f"Tổng: {addition(a, b)}")
        print(f"Tích: {multiplication(a, b)}")
        print(f"Mũ: {power(a, b)}")
        sqrt_result = square_root(a)
        if sqrt_result is not None:
            print(f"Căn bậc 2: {sqrt_result}")
        print(f"Giải phương trình bậc 2: {quadratic_eq(a, b, c)}")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")


# Bài 9: Đọc và ghi tệp
def read_write_file():
    try:
        with open('fin.txt', 'r', encoding='utf-8') as fin:
            n = int(fin.readline().strip())
            data = fin.readlines()

        with open('fout.txt', 'w', encoding='utf-8') as fout:
            total_sum = 0
            fout.write(str(total_sum) + '\n')
            for line in data:
                try:
                    numbers = [float(num) for num in line.split()]
                    sum_numbers = sum(numbers)
                    total_sum += sum_numbers
                    fout.write(f"{sum_numbers}\n")
                    fout.seek(0)
                    fout.write(str(total_sum))
                except ValueError as ve:
                    print(f"Lỗi khi đọc dòng từ tệp fin.txt: {ve}")
        print("Ghi tệp fout.txt thành công!")
    except FileNotFoundError:
        print("Không tìm thấy tệp fin.txt.")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")


# Bài 10: Xử lý ngoại lệ
def handle_exceptions():
    try:
        a = int(input("Nhập số nguyên a: "))
        b = int(input("Nhập số nguyên b: "))
        result = a / b
        print(f"{a}/{b} = {result}")
    except ValueError as ve:
        print(f"Lỗi: a và b phải là số nguyên. Chi tiết: {ve}")
    except ZeroDivisionError:
        print("Lỗi: b không được bằng 0.")


# Bài 11: Lập trình với đối tượng
class NhanVien:
    def __init__(self, hoten, tuoi, luong):
        self.hoten = hoten
        self.tuoi = tuoi
        self.luong = luong


def input_nhanvien_list():
    nhanvien_list = []
    try:
        n = int(input("Nhập số lượng nhân viên: "))
        if n < 5:
            raise ValueError("Số lượng nhân viên phải ít nhất là 5.")
        for i in range(n):
            hoten = input(f"Nhập tên của nhân viên {i + 1}: ")
            tuoi = int(input(f"Nhập tuổi của nhân viên {i + 1}: "))
            luong = float(input(f"Nhập lương của nhân viên {i + 1}: "))
            nhanvien = NhanVien(hoten, tuoi, luong)
            nhanvien_list.append(nhanvien)
    except ValueError as ve:
        print(f"Lỗi: {ve}")
    return nhanvien_list


def sort_nhanvien_by_age(nhanvien_list):
    try:
        sorted_nhanvien_list = sorted(nhanvien_list, key=lambda x: x.tuoi, reverse=True)
        return sorted_nhanvien_list
    except Exception as e:
        print(f"Lỗi khi sắp xếp danh sách: {e}")
        return []


def write_nhanvien_to_file(nhanvien_list):
    try:
        with open('NhanVien.txt', 'w') as file:
            for nhanvien in nhanvien_list:
                file.write(f"{nhanvien.hoten}, {nhanvien.tuoi}, {nhanvien.luong}\n")
        print("Ghi tệp NhanVien.txt thành công!")
    except Exception as e:
        print(f"Lỗi khi ghi tệp: {e}")


def read_nhanvien_from_file():
    try:
        with open('NhanVien.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                hoten, tuoi, luong = data
                print(f"Họ tên: {hoten}, Tuổi: {tuoi}, Lương: {luong}")
    except FileNotFoundError:
        print("Không tìm thấy tệp NhanVien.txt.")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")


# BÀI 12

def generate_vector_x(m):
    try:
        x = np.random.randint(-3, 7, m)
        return x
    except Exception as e:
        print(f"Lỗi khi tạo vecto x: {e}")
        return None


def generate_matrix_A(m, n):
    try:
        A = np.random.randint(0, 10, size=(m, n))
        return A
    except Exception as e:
        print(f"Lỗi khi tạo ma trận A: {e}")
        return None


def generate_matrix_B(m, n):
    try:
        B = np.random.randint(0, 10, size=(m, n))
        return B
    except Exception as e:
        print(f"Lỗi khi tạo ma trận B: {e}")
        return None


def generate_matrix_C(n, m):
    try:
        C = np.random.randint(0, 10, size=(n, m))
        return C
    except Exception as e:
        print(f"Lỗi khi tạo ma trận C: {e}")
        return None


def multiply_vector_matrix(x, A):
    try:
        result = np.dot(x, A)
        return result
    except Exception as e:
        print(f"Lỗi khi tính tích của vecto x và ma trận A: {e}")
        return None


def multiply_matrices(A, B):
    try:
        result = np.dot(A, B)
        return result
    except Exception as e:
        print(f"Lỗi khi tính tích hai ma trận: {e}")
        return None


def multiply_transpose_matrix_B(C, B):
    try:
        result = np.dot(C.T, B)
        return result
    except Exception as e:
        print(f"Lỗi khi tính tích hai ma trận (chuyển vị C) và B: {e}")
        return None


# Bài 13
def func_y(x):
    try:
        y = x ** 4 - 2 * x ** 2 - 3
        return y
    except Exception as e:
        print(f"Lỗi khi tính giá trị của hàm số y: {e}")
        return None


def func_derivative_y(x, order=1):
    try:
        if order == 1:
            y_prime = 4 * x ** 3 - 4 * x
            return y_prime
        elif order == 2:
            y_double_prime = 12 * x ** 2 - 4
            return y_double_prime
        elif order == 3:
            y_triple_prime = 24 * x
            return y_triple_prime
        else:
            raise ValueError("Chỉ hỗ trợ đến đạo hàm bậc 3.")
    except Exception as e:
        print(f"Lỗi khi tính giá trị đạo hàm: {e}")
        return None


# Bài 14
def plot_saddle_surface():
    try:
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        x, y = np.meshgrid(x, y)
        z = (x / 3) ** 2 - (y / 2) ** 2

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, cmap='viridis')
        ax.set_title('Đồ thị mặt yên ngựa')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
    except Exception as e:
        print(f"Lỗi khi vẽ đồ thị mặt yên ngựa: {e}")


def plot_hyperbolic_surface():
    try:
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        x, y = np.meshgrid(x, y)
        z = (x / 3) ** 2 + (y / 5) ** 2 - (2 / 2) ** 2

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, cmap='viridis')
        ax.set_title('Đồ thị mặt hyperbolic 1 tầng')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
    except Exception as e:
        print(f"Lỗi khi vẽ đồ thị mặt hyperbolic 1 tầng: {e}")


def plot_sphere_surface():
    try:
        phi = np.linspace(0, np.pi, 100)
        theta = np.linspace(0, 2 * np.pi, 100)
        phi, theta = np.meshgrid(phi, theta)
        x = 2 * np.sin(phi) * np.cos(theta) - 2
        y = 2 * np.sin(phi) * np.sin(theta) + 1
        z = 2 * np.cos(phi) + 4

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, cmap='viridis')
        ax.set_title('Đồ thị mặt cầu')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
    except Exception as e:
        print(f"Lỗi khi vẽ đồ thị mặt cầu: {e}")


# Bài 15
def solve_linear_system():
    try:
        x, y, z = sp.symbols('x y z')
        eq1 = sp.Eq(2 * x - 5 * y + z, -5)
        eq2 = sp.Eq(4 * x + 2 * y - 2 * z, 2)
        eq3 = sp.Eq(x + y - z, 0)
        solution = sp.solve((eq1, eq2, eq3), (x, y, z))
        print(f"Giải hệ phương trình: {solution}")
    except Exception as e:
        print(f"Lỗi khi giải hệ phương trình: {e}")


def calculate_limit():
    try:
        x = sp.symbols('x')
        f = ((x ** 3 - 3 * x ** 2) ** (1 / 3) + (x ** 2 - 2 * x) ** (1 / 2))
        limit_result = sp.limit(f, x, 5)
        print(f"Giới hạn của hàm f khi x tiến tới 5: {limit_result}")
    except Exception as e:
        print(f"Lỗi khi tính giới hạn: {e}")


def calculate_derivative():
    try:
        x = sp.symbols('x')
        f = (2 * x - 1) / (x + 2)
        derivative = sp.diff(f, x)
        print(f"Đạo hàm của hàm f: {derivative}")
    except Exception as e:
        print(f"Lỗi khi tính đạo hàm: {e}")


def calculate_indefinite_integral():
    try:
        x = sp.symbols('x')
        f = x / (x ** 2 + 1)
        indefinite_integral = sp.integrate(f, x)
        print(f"Nguyên hàm của hàm f: {indefinite_integral}")
    except Exception as e:
        print(f"Lỗi khi tính nguyên hàm: {e}")


def calculate_definite_integral():
    try:
        x = sp.symbols('x')
        f = (1 - x * sp.tan(x)) / (x ** 2 * sp.cos(x) + x)
        definite_integral = sp.integrate(f, (x, 0, 2 * sp.pi / 3))
        print(f"Tích phân của hàm f từ 0 đến 2pi/3: {definite_integral}")
    except Exception as e:
        print(f"Lỗi khi tính tích phân: {e}")


# Chương trình chính
def main():
    while True:
        try:
            print("_______________________________________________________|")
            print("|                      MENU BÀI TẬP                    |")
            print("|______________________________________________________|")
            print("|1.  Viết chương trình chuyển đổi nhiệt độ             |")
            print("|2.  Tính tổng số nguyên tố, tổng ước số, tổng số chẵn |")
            print("|3.  Xử lý hàm số                                      |")
            print("|4.  Tạo dãy số và ước số chung lớn nhất               |")
            print("|5.  Kiểm tra xâu và chèn xâu vào xâu khác             |")
            print("|6.  Sinh tập hợp ngẫu nhiên                           |")
            print("|7.  Xử lý từ điển                                     |")
            print("|8.  Sử dụng module và phép toán cơ bản                |")
            print("|9.  Đọc và ghi tệp                                    |")
            print("|10. Xử lý ngoại lệ                                    |")
            print("|11. Xử lý đối tượng                                   |")
            print("|12. Sử dụng thư viện NumPy                            |")
            print("|13. Vẽ đồ thị đạo hàm                                 |")
            print("|14. Vẽ các hình không gian                            |")
            print("|15. Sử dụng thư viện SymPy                            |")
            print("|______________________________________________________|")
            print("|0.  Thoát chương trình                                |")
            print("|______________________________________________________|")
            choice = int(input("Chọn bài tập (0-15):"))
            if choice == 0:
                print("Kết thúc chương trình.")
                break
            elif choice == 1:
                celsius_to_fahrenheit()
            elif choice == 2:
                while True:
                    try:
                        n = int(input("Nhập một số tự nhiên n (50 <= n <= 150): "))
                        if 50 <= n <= 150:
                            prime_sum, divisor_sum, even_sum_for, even_sum_while = calculate_values_for_n(n)
                            print(f"Tổng số nguyên tố nhỏ hơn {n}: {prime_sum}")
                            print(f"Tổng các ước số của {n}: {divisor_sum}")
                            print(f"Tổng số chẵn từ 1 đến {n} (sử dụng vòng lặp for): {even_sum_for}")
                            print(f"Tổng số chẵn từ 1 đến {n} (sử dụng vòng lặp while): {even_sum_while}")
                            break  # Thoát khỏi vòng lặp khi đã nhập đúng
                        else:
                            print("Số n không nằm trong khoảng [50, 150].")
                    except ValueError:
                        print("Lỗi: Vui lòng nhập một số tự nhiên.")
            elif choice == 3:
                main_bai_3()
            elif choice == 4:
                try:
                    A = [int(x) for x in input("Nhập dãy số A (cách nhau bằng dấu cách): ").split()]
                    B = [int(x) for x in input("Nhập dãy số B (cách nhau bằng dấu cách): ").split()]
                    C = create_sequence_C(A, B)
                    if C is not None:
                        print(f"Dãy C: {C}")
                    else:
                        print("Xảy ra lỗi. Vui lòng kiểm tra đầu vào.")
                except ValueError:
                    print("Lỗi: Vui lòng nhập các số tự nhiên.")
            elif choice == 5:
                try:
                    Str1 = input("Nhập xâu Str1: ")
                    Str2 = input("Nhập xâu Str2: ")
                    check_string_in_string(Str1, Str2)
                except Exception as e:
                    print(f"Lỗi không xác định: {e}")
            elif choice == 6:
                try:
                    A, B, C = create_sets()
                    print(f"Tập hợp A: {A}")
                    print(f"Tập hợp B: {B}")
                    print(f"Tập hợp C: {C}")
                except Exception as e:
                    print(f"Lỗi không xác định: {e}")
            elif choice == 7:
                A = {"Toan": 9, "Van": 5, "Su": 8, "Dia": 7, "Hoa": 6}
                max_value, max_subjects, even_scores, avg_score, new_dict, reversed_dict = process_dictionary(A)
                if max_value is not None:
                    print(f"Điểm lớn nhất: {max_value}")
                    print(f"Môn và điểm có điểm lớn nhất: {max_subjects}")
                    print(f"Các điểm số chẵn: {even_scores}")
                    print(f"Trung bình tất cả các điểm: {avg_score}")
                    print(f"Từ điển mới với các môn lớn hơn 7 điểm: {new_dict}")
                    print(f"Đảo ngược từ điển A: {reversed_dict}")
            elif choice == 8:
                main_bai_8()
            elif choice == 9:
                read_write_file()
            elif choice == 10:
                handle_exceptions()
            elif choice == 11:
                try:
                    nhanvien_list = input_nhanvien_list()
                    sorted_nhanvien_list = sort_nhanvien_by_age(nhanvien_list)
                    write_nhanvien_to_file(sorted_nhanvien_list)
                    read_nhanvien_from_file()
                except Exception as e:
                    print(f"Lỗi chương trình chính: {e}")
            elif choice == 12:
                try:
                    m = 3
                    n = 4

                    x = generate_vector_x(m)
                    A = generate_matrix_A(m, n)
                    B = generate_matrix_B(m, n)
                    C = generate_matrix_C(n, m)

                    if x is not None and A is not None and B is not None and C is not None:
                        print(f"Vecto x: {x}")
                        print(f"Ma trận A:\n{A}")
                        print(f"Ma trận B:\n{B}")
                        print(f"Ma trận C:\n{C}")

                        result_x_A = multiply_vector_matrix(x, A)
                        result_A_B = multiply_matrices(A, B)
                        result_Ct_B = multiply_transpose_matrix_B(C, B)

                        print(f"Tích của vecto x và ma trận A:\n{result_x_A}")
                        print(f"Tích hai ma trận A và B:\n{result_A_B}")
                        print(f"Tích hai ma trận (chuyển vị C) và B:\n{result_Ct_B}")
                except Exception as e:
                    print(f"Lỗi chương trình chính: {e}")
            elif choice == 13:
                try:
                    x_values = np.linspace(-10, 10, 1000)

                    y_values = func_y(x_values)
                    y_prime_values = func_derivative_y(x_values, order=1)
                    y_double_prime_values = func_derivative_y(x_values, order=2)
                    y_triple_prime_values = func_derivative_y(x_values, order=3)

                    if y_values is not None and y_prime_values is not None and y_double_prime_values is not None and y_triple_prime_values is not None:
                        plt.figure(figsize=(10, 6))

                        plt.plot(x_values, y_values, label='y = x^4 - 2x^2 - 3')
                        plt.plot(x_values, y_prime_values, label="y'")
                        plt.plot(x_values, y_double_prime_values, label="y''")
                        plt.plot(x_values, y_triple_prime_values, label="y'''")

                        plt.title('Đồ thị hàm số và đạo hàm')
                        plt.xlabel('x')
                        plt.ylabel('y')
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                except Exception as e:
                    print(f"Lỗi chương trình chính: {e}")

            elif choice == 14:
                try:
                    plot_saddle_surface()
                    plot_hyperbolic_surface()
                    plot_sphere_surface()
                except Exception as e:
                    print(f"Lỗi chương trình chính: {e}")
            elif choice == 15:
                try:
                    solve_linear_system()
                    calculate_limit()
                    calculate_derivative()
                    calculate_indefinite_integral()
                    calculate_definite_integral()
                except Exception as e:
                    print(f"Lỗi chương trình chính: {e}")
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
