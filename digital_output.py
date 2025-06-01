# digital_output.py
# ควบคุมขา Digital เช่นเปิด/ปิด LED โดยใช้ pyfirmata

from pyfirmata import Arduino
import time

# สร้างการเชื่อมต่อกับ Arduino ที่พอร์ต 'COM3'
# 🔸 หากใช้ Linux ให้ใช้ '/dev/ttyUSB0' หรือ '/dev/ttyACM0'
board = Arduino('COM3')

# สร้างอ้างอิงถึงขา Digital D13 เพื่อใช้งานเป็น output
# 🔸 'd'  = digital pin
# 🔸 '13' = หมายเลขขา (D13)
# 🔸 'o'  = output (ใช้ส่งข้อมูล เช่น เปิด/ปิด)
led_pin = board.get_pin('d:13:o')

print("📍 เริ่มควบคุม LED ที่ D13")

while True:
    led_pin.write(1)  # 🔸 1 = ON (HIGH voltage) → เปิด LED
    print("💡 เปิด LED")
    time.sleep(1)

    led_pin.write(0)  # 🔸 0 = OFF (LOW voltage) → ปิด LED
    print("🌑 ปิด LED")
    time.sleep(1)
