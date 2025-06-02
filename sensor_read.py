# sensor_read.py
# อ่านค่าจาก Digital input (เช่นปุ่มกด) และ Analog input (เช่น potentiometer)

from pyfirmata2 import Arduino, util   
import time

# ─────────────────── เชื่อมต่อกับบอร์ด (แก้ 'COM11' ให้ตรงกับเครื่องของคุณ)
board = Arduino('COM11')
board.samplingOn(30)

# ─────────────────── สร้าง Iterator Thread เพื่อจัดการ Serial Buffers
it = util.Iterator(board)
it.start()

# ─────────────────── กำหนดขาเป็น Input และประกาศ Callback
# get_pin('d:9:s')
#  • 'd'  = digital pin
#  • 'a'  = analog pin
#  • '2'  = หมายเลขขา D2 
#  • '0'  = หมายเลขขา A0 
#  • 'i'  = input mode  (รับค่าจากเซนเซอร์)
button_pin = board.get_pin('d:2:i')   # Digital D2  (input)
poten_pin = board.get_pin('a:0:i')   # Analog  A0  (input)

# ─────────────────── Callback ฟังค์ชัน 
def on_button(data):
    """
    จะถูกเรียกทุกครั้งที่สถานะปุ่มเปลี่ยน (0→1 หรือ 1→0)
    :ตัวอย่าง ปุ่มกดกำหนด data: 0.0 เมื่อกด, 1.0 เมื่อปล่อย
    """
    state = "กดอยู่" if data else "ไม่กด"
    print("🟦 สถานะปุ่ม D2:", state)

def on_poten(data):
    """
    จะถูกเรียกตามอัตรา sampling ของ Arduino (ค่า 0.0-1.0)
    """
    voltage = data * 5.0                  # แปลงเป็นโวลต์ (สมมติ Vref = 5 V)
    # แสดงผลแบบเรียบง่าย (ไม่ใช้ f-string ซับซ้อน)
    print("A0 =", round(data, 3), "≈", round(voltage, 2), "V")

# ─────────────────── ลงทะเบียน Callback แล้วเปิดรายงาน (enable_reporting)
button_pin.register_callback(on_button)
button_pin.enable_reporting()

poten_pin.register_callback(on_poten)
poten_pin.enable_reporting()

print("เริ่มรับข้อมูลผ่าน callback (กด Ctrl-C เพื่อหยุด)")

# ─────────────────── วนค้างไว้เฉย ๆ  (callback จะทำงานเบื้องหลัง)
try:
    while True:
        time.sleep(1)   # หน่วงยาวได้ เพราะเราไม่ได้โพลล์ค่าเอง
except KeyboardInterrupt:
    print("\n ผู้ใช้สั่งหยุดการทำงาน")
finally:
    board.exit()        # ปิดพอร์ตอย่างปลอดภัย