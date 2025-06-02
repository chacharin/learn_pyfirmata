# digital_output.py
# ควบคุมขา Digital เช่นเปิด/ปิด LED โดยใช้ pyfirmata

from pyfirmata2 import Arduino          
import time                            

# ─────────────────── เชื่อมต่อบอร์ด
# Arduino('COM11')
#   'COM11' คือ Serial Port ของบอร์ดบน Windows
#   ถ้าเป็น Linux / macOS ให้แก้เป็น '/dev/ttyUSB___' หรือ '/dev/ttyACM____'
board = Arduino('COM11')  # ⬅ เปลี่ยนตามพอร์ตของคุณ

# ─────────────────── กำหนดขา D13 เป็น Output
led_pin = board.get_pin('d:13:o')

print("เริ่มควบคุม LED บน D13")

# ─────────────────── วนลูปเปิด/ปิด
while True:
    led_pin.write(1)          # เขียนค่า  1 เปิด LED
    print("💡 เปิด LED")
    time.sleep(1)

    led_pin.write(0)          # เขียนค่า  0 ปิด LED
    print("🌑 ปิด LED")
    time.sleep(1)