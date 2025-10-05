# Biến là gì?
# Biến (variable) giống như chiếc hộp chứa dữ liệu.
# Mỗi biến có một tên và một giá trị.
# Tên biến phải tuân theo các quy tắc đặt tên trong Python.
# Ví dụ:   
#  - Tên biến phải bắt đầu bằng chữ cái hoặc dấu gạch dưới (_).
#  - Tên biến không được chứa khoảng trắng.
#  - Tên biến không được trùng với từ khóa của Python (như: if, else, for, while, def, class, v.v.).
#  - Tên biến phân biệt chữ hoa và chữ thường (ví dụ: myVar và myvar là hai biến khác nhau).
#  - Tên biến nên có ý nghĩa để dễ hiểu (ví dụ: age, name, total_price).
# Cách khai báo biến trong Python:
age = 25  # Biến age có giá trị là 25
name = "Alice"  # Biến name có giá trị là "Alice"
is_student = True  # Biến is_student có giá trị là True (kiểu boolean)
# In giá trị của biến
print("Age:", age)  # In ra: Age: 25
print("Name:", name)  # In ra: Name: Alice
print("Is Student:", is_student)  # In ra: Is Student: True
# Thay đổi giá trị của biến
age = 26  # Bây giờ biến age có giá trị mới là 26
print("Updated Age:", age)  # In ra: Updated Age: 26
# Các kiểu dữ liệu cơ bản trong Python:
# 1. Số nguyên (Integer)
num1 = 10
num2 = -5
# 2. Số thực (Float)
pi = 3.14
temperature = -2.5
# 3. Chuỗi (String)
greeting = "Hello, World!"
name = 'Bob'
# 4. Boolean (True/False)
is_raining = False
is_sunny = True
# 5. Danh sách (List)
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
# 6. Tuple (Bộ)
coordinates = (10.0, 20.0)
point = (5, 15)
# 7. Từ điển (Dictionary)
person = {"name": "Alice", "age": 25, "city": "New York"}
car = {"make": "Toyota", "model": "Camry", "year": 2020}
# 8. Tập hợp (Set)
unique_numbers = {1, 2, 3, 4, 5}
unique_fruits = {"apple", "banana", "cherry"}
# 9. None (Giá trị rỗng)
data = None
result = None
# In kiểu dữ liệu của biến
print("Type of num1:", type(num1))  # In ra: Type of num1: <class 'int'>
print("Type of pi:", type(pi))  # In ra: Type of pi: <class 'float'>
print("Type of greeting:", type(greeting))  # In ra: Type of greeting: <class 'str'>
print("Type of is_raining:", type(is_raining))  # In ra: Type of is_raining: <class 'bool'>
print("Type of fruits:", type(fruits))  # In ra: Type of fruits: <class 'list'>
print("Type of coordinates:", type(coordinates))  # In ra: Type of coordinates: <class 'tuple'>
print("Type of person:", type(person))  # In ra: Type of person: <class 'dict'>
print("Type of unique_numbers:", type(unique_numbers))  # In ra: Type of unique
print("Type of data:", type(data))  # In ra: Type of data: <class 'NoneType'>
# Thực hành:
# 1. Tạo biến để lưu tên, tuổi và điểm trung bình của một học sinh.
student_name = "John Doe"
student_age = 20
student_gpa = 3.75
print("Student Name:", student_name)
print("Student Age:", student_age)
print("Student GPA:", student_gpa)
# 2. Tạo biến để lưu thông tin về một cuốn sách (tiêu đề, tác giả, năm xuất bản, giá).
book_title = "To Kill a Mockingbird"
book_author = "Harper Lee"
book_year = 1960
book_price = 15.99
print("Book Title:", book_title)
print("Book Author:", book_author)
print("Book Year:", book_year)
print("Book Price:", book_price)
# 3. Tạo biến để lưu trạng thái của một đơn hàng (đã thanh toán hay chưa, số lượng sản phẩm, tổng tiền).
order_paid = True
order_quantity = 3
order_total = 45.00
print("Order Paid:", order_paid)
print("Order Quantity:", order_quantity)
print("Order Total:", order_total)
# 4. Tạo biến để lưu thông tin về một chiếc xe (hãng, mẫu, năm sản xuất, màu sắc).
car_make = "Honda"
car_model = "Civic"
car_year = 2022
car_color = "Red"
print("Car Make:", car_make)
print("Car Model:", car_model)
print("Car Year:", car_year)
print("Car Color:", car_color)
# 5. Toán tử và biểu thức
# Toán tử số học
a = 10
b = 3
print("Addition:", a + b)  # In ra: Addition: 13
print("Subtraction:", a - b)  # In ra: Subtraction: 7
print("Multiplication:", a * b)  # In ra: Multiplication: 30
print("Division:", a / b)  # In ra: Division: 3.333
print("Floor Division:", a // b)  # In ra: Floor Division: 3
print("Modulus:", a % b)  # In ra: Modulus: 1
print("Exponentiation:", a ** b)  # In ra: Exponentiation: 1000
# Toán tử so sánh
x = 5
y = 10
print("Equal:", x == y)  # In ra: Equal: False
print("Not Equal:", x != y)  # In ra: Not Equal: True
print("Greater Than:", x > y)  # In ra: Greater Than: False
print("Less Than:", x < y)  # In ra: Less Than: True
print("Greater Than or Equal:", x >= y)  # In ra: Greater Than or Equal: False
print("Less Than or Equal:", x <= y)  # In ra: Less Than or Equal: True
# Toán tử logic
p = True
q = False
print("AND:", p and q)  # In ra: AND: False
print("OR:", p or q)  # In ra: OR: True
print("NOT p:", not p)  # In ra: NOT p: False
print("NOT q:", not q)  # In ra: NOT q: True
# Toán tử gán
count = 0
count += 5  # Tương đương với count = count + 5
print("Count after += 5:", count)  # In ra: Count after += 5: 5
count *= 2  # Tương đương với count = count * 2
print("Count after *= 2:", count)  # In ra: Count after *= 2: 10
count -= 3  # Tương đương với count = count - 3
print("Count after -= 3:", count)  # In ra: Count after -= 3: 7
count //= 2  # Tương đương với count = count // 2
print("Count after //= 2:", count)  # In ra: Count after //= 2: 3
count %= 2  # Tương đương với count = count % 2
print("Count after %= 2:", count)  # In ra: Count after %= 2: 1
count **= 3  # Tương đương với count = count ** 3
print("Count after **= 3:", count)  # In ra: Count after **= 3: 1
# Bài tập thực hành:
# 1. Tính diện tích và chu vi của một hình chữ nhật với chiều dài là 5 và chiều rộng là 3.
length = 5
width = 3
area = length * width
perimeter = 2 * (length + width)
print("Area of Rectangle:", area)  # In ra: Area of Rectangle: 15
print("Perimeter of Rectangle:", perimeter)  # In ra: Perimeter of Rectangle: 16
# 2. Tính tổng, hiệu, tích và thương của hai số a = 15 và b = 4.
a = 15
b = 4
sum_ab = a + b
difference_ab = a - b
product_ab = a * b
quotient_ab = a / b
print("Sum:", sum_ab)  # In ra: Sum: 19
print("Difference:", difference_ab)  # In ra: Difference: 11
print("Product:", product_ab)  # In ra: Product: 60
print("Quotient:", quotient_ab)  # In ra: Quotient: 3
# 3. Kiểm tra xem số x = 7 có lớn hơn số y = 10 hay không.
x = 7
y = 10
is_x_greater = x > y
print("Is x greater than y?", is_x_greater)  # In ra: Is x greater than y? False
# 4. Kiểm tra xem biến is_raining có phải là True hay không.
is_raining = False
print("Is it raining?", is_raining)  # In ra: Is it raining? False
# 5. Cập nhật giá trị của biến score bằng cách tăng thêm 10 điểm.
score = 50
score += 10
print("Updated Score:", score)  # In ra: Updated Score: 60
# --- IGNORE ---
# First day of learning programming with python
# input / output cơ bản
name = input("Enter your name: ")  # Yêu cầu người dùng nhập tên
print("Hello,", name)  # In lời chào với tên người dùng
age = int(input("Enter your age: "))  # Yêu cầu người dùng nhập tuổi và chuyển đổi sang kiểu số nguyên
print("You are", age, "years old.")  # In tuổi người dùng
height = float(input("Enter your height in meters: "))  # Yêu cầu người dùng nhập chiều cao và chuyển đổi sang kiểu số thực
print("Your height is", height, "meters.")  # In chiều cao người dùng
