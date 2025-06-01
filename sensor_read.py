# sensor_read.py
# อ่านค่าจาก Digital input (เช่นปุ่มกด) และ Analog input (เช่น potentiometer)

from pyfirmata import Arduino, util
import time

# สร้างการเชื่อมต่อกับบอร์ด
board = Arduino('COM3')

# เริ่ม iterator เพื่อให้ Arduino ส่งค่ากลับมาอย่างต่อเนื่อง
it = util.Iterator(board)
it.start()

# ตั้งค่าขา Digital D2 เป็น input
# 🔸 'd'  = digital pin
# 🔸 '2'  = ใช้ขา D2
# 🔸 'i'  = input (ใช้รับข้อมูลจากอุปกรณ์ เช่น ปุ่ม)
button_pin = board.get_pin('d:2:i')

# ตั้งค่าขา Analog A0 เป็น input
# 🔸 'a'  = analog pin
# 🔸 '0'  = ใช้ขา A0
# 🔸 'i'  = input
analog_pin = board.get_pin('a:0:i')

print("📍 เริ่มอ่านค่าจากปุ่ม (Digital) และ Potentiometer (Analog)")

while True:
    # อ่านสถานะปุ่มกด (ค่าจะเป็น True/False หรือ None)
    button_value = button_pin.read()
    if button_value is not None:
        state = "กดอยู่" if button_value else "ไม่กด"
        print(f"🟦 สถานะปุ่ม: {state}")

    # อ่านค่าจากเซ็นเซอร์ analog (เช่น potentiometer)
    analog_value = analog_pin.read()
    if analog_value is not None:
        # 🔸 analog_value มีค่าระหว่าง 0.0 ถึง 1.0
        voltage = analog_value * 5  # คูณเพื่อประมาณแรงดัน (ในระบบ 5V)
        print(f"📈 ค่าจาก A0: {analog_value:.3f} → ประมาณ {voltage:.2f} V")

    time.sleep(0.5)
