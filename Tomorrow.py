from datetime import datetime, timedelta

def ngay_mai(day: int, month: int, year: int):
    try:
        ngay_hien_tai = datetime(year, month, day)
        ngay_tiep_theo = ngay_hien_tai + timedelta(days=1)
        return ngay_tiep_theo.strftime("%d-%m-%Y")
    except ValueError:
        return "Ngày không hợp lệ!"

# Nhập ngày, tháng, năm từ người dùng
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

# Xuất kết quả
print("Ngày mai là:", ngay_mai(day, month, year))
