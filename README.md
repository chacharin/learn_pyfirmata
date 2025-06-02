# Arduino Control with PyFirmata

โปรเจกต์นี้สาธิตการควบคุม Arduino ด้วย Python โดยใช้ไลบรารี **pyFirmata** ซึ่งสามารถใช้งานร่วมกับ Arduino ที่อัปโหลด **StandardFirmata** ผ่าน Arduino IDE ได้

---

## Requirements

ติดตั้งไลบรารีที่จำเป็นก่อนเริ่มต้น:
```bash
pip install pyfirmata2
```

Arduino ของคุณต้องอัปโหลด **StandardFirmata** ผ่าน Arduino IDE:
1. ไปที่ **File > Examples > Firmata > StandardFirmata**
2. อัปโหลดลงบอร์ด

---

## โครงสร้างโปรแกรม

| ไฟล์              | บทบาท                         | ขาที่ใช้  |
|------------------|-------------------------------|-----------|
| `digital_output.py` | เปิด/ปิด LED ด้วยขา Digital      | D13       |
| `sensor_read.py`    | อ่านค่าจากเซ็นเซอร์ Digital + Analog | D2 (ปุ่ม), A0 (potentiometer) |
| `servo_control.py`  | ควบคุม Servo Motor           | D9 (PWM)  |

---

## อธิบายทีละไฟล์

### 3.1 `digital_output.py`
กระพริบ LED บนขา D13 ทุก 1 วินาที

### 3.2 `sensor_read.py`
ใช้ **callback** เพื่ออ่านสวิตช์ D2 และโพเทนชิฯ A0  
ตั้ง `samplingOn(30)` → ประมาณ 33 Hz

### 3.3 `servo_control.py`
สั่งเซอร์โวที่ D9 หมุน 0 → 180° → 0 ขั้นละ 30°

---

##  วิธีรันเดโม

```bash
# 1. กระพริบ LED
python digital_output.py

# 2. ปุ่ม + โพเทนชิฯ (กด Ctrl‑C เพื่อหยุด)
python sensor_read.py

# 3. หมุนเซอร์โว (กด Ctrl‑C เพื่อหยุด)
python servo_control.py
```

หากบอร์ดของคุณไม่ใช่ `COM11` ให้แก้สตริงพอร์ตในแต่ละสคริปต์  
(เช่น `COM7` หรือ `/dev/ttyACM0`)

---

## ปัญหาที่พบบ่อย

| อาการ | วิธีแก้ |
|-------|--------|
| `SerialException: could not open port` | พอร์ตผิด / ถูกโปรแกรมอื่นจับ / ไดรเวอร์ CH340/FTDI ไม่ครบ |
| ไม่มีข้อความจาก callback | ลืม `enable_reporting()` หรือ sampling interval ยาวเกิน |
| เซอร์โวสั่น / แรงไม่พอ | จ่ายไฟ 5 V แยกให้เซอร์โวและต่อกราวด์ร่วม |
| เรียก `.read()` แล้ว `IOError` | pyfirmata2 ปิดการ polling → ใช้ callback แทน |

---

