# Arduino Control with PyFirmata

โปรเจกต์นี้สาธิตการควบคุม Arduino ด้วย Python โดยใช้ไลบรารี **pyFirmata** ซึ่งสามารถใช้งานร่วมกับ Arduino ที่อัปโหลด **StandardFirmata** ผ่าน Arduino IDE ได้

---

## 📦 Requirements

ติดตั้งไลบรารีที่จำเป็นก่อนเริ่มต้น:
```bash
pip install pyfirmata
```

Arduino ของคุณต้องอัปโหลด **StandardFirmata** ผ่าน Arduino IDE:
1. ไปที่ **File > Examples > Firmata > StandardFirmata**
2. อัปโหลดลงบอร์ด

---

## 🔧 โครงสร้างโปรแกรม

| ไฟล์              | บทบาท                         | ขาที่ใช้  |
|------------------|-------------------------------|-----------|
| `digital_output.py` | เปิด/ปิด LED ด้วยขา Digital      | D13       |
| `sensor_read.py`    | อ่านค่าจากเซ็นเซอร์ Digital + Analog | D2 (ปุ่ม), A0 (potentiometer) |
| `servo_control.py`  | ควบคุม Servo Motor           | D9 (PWM)  |

---

## 🔌 1. digital_output.py

ควบคุมขา Digital เพื่อเปิด/ปิด LED

```python
led_pin = board.get_pin('d:13:o')  # digital, pin 13, output
led_pin.write(1)  # เปิด LED
led_pin.write(0)  # ปิด LED
```

---

## 📊 2. sensor_read.py

อ่านค่าจากปุ่มกด (digital input) และ potentiometer (analog input)

```python
button_pin = board.get_pin('d:2:i')  # digital pin 2 as input
analog_pin = board.get_pin('a:0:i')  # analog pin A0 as input

value = button_pin.read()           # True/False
analog_value = analog_pin.read()    # 0.0 to 1.0 → *5 = แรงดัน
```

---

## 🔧 3. servo_control.py

ควบคุม Servo Motor ที่ขา D9 โดยระบุองศา (0-180)

```python
servo_pin = board.get_pin('d:9:s')  # digital pin 9, servo mode
servo_pin.write(90)  # หมุนไปที่ 90 องศา
```

---

## ℹ️ คำอธิบายรูปแบบ get_pin()

```python
get_pin('type:pin:mode')
```

| ตัวอักษร | ความหมาย |
|----------|-----------|
| `d`      | digital pin |
| `a`      | analog pin  |
| `o`      | output      |
| `i`      | input       |
| `s`      | servo       |

---

## 🧠 หมายเหตุ

- ใช้ `util.Iterator(board).start()` สำหรับ input ทุกชนิด (อ่านค่าต่อเนื่อง)
- `write(1)` สำหรับเปิดไฟ, `write(0)` สำหรับปิด หรือ `write(90)` สำหรับ servo
- พอร์ต `COM3` ต้องเปลี่ยนตามเครื่องของคุณ

---
