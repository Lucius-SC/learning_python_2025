# Học cú pháp cơ bản:
print("Hello, Fintech world!")
name = input("What's your name? ")
print("Welcome,", name)
# Biến: đặt tên theo quy tắc (snake_case)
balance = 1000
interest_rate = 0.05
# Kiểu dữ liệu: int, float, str, bool
is_active = True
# Toán tử: +, -, *, /, //, %, **
new_balance = balance + (balance * interest_rate)
print("New balance after interest:", new_balance)
# Ép kiểu:
balance_str = str(balance)
print("Balance as string:", balance_str)
age = int(input("Enter your age: "))
print("You are", age, "years old")
# Thực hành mini: Viết chương trình tính số tiền sau 1 năm gửi tiết kiệm:
principal = float(input("Enter the principal amount: "))
rate = 0.05
amount = principal * (1 + rate)
print("Amount after 1 year:", amount)
