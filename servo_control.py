# servo_control.py
# ควบคุม Servo Motor ด้วย pyfirmata โดยส่งองศา 0–180 ผ่านขา PWM

from pyfirmata import Arduino
import time

# เชื่อมต่อกับ Arduino ที่พอร์ต COM3
board = Arduino('COM3')

# ตั้งค่าขา D9 เป็น servo
# 🔸 'd'  = digital pin
# 🔸 '9'  = หมายเลขขาที่จะควบคุม servo
# 🔸 's'  = servo (รองรับค่ามุม 0 ถึง 180)
servo_pin = board.get_pin('d:9:s')

print("📍 เริ่มควบคุมเซอร์โวมอเตอร์ที่ D9")

while True:
    # หมุนจาก 0 → 180 องศา ทีละ 30 องศา
    for angle in range(0, 181, 30):  # 🔸 range(start, stop, step)
        print(f"➡ หมุนไปที่ {angle}°")
        servo_pin.write(angle)  # 🔸 ส่งค่าองศาไปยัง servo
        time.sleep(1)

    # หมุนกลับจาก 180 → 0 องศา
    for angle in range(180, -1, -30):
        print(f"⬅ หมุนกลับที่ {angle}°")
        servo_pin.write(angle)
        time.sleep(1)
