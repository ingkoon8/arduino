# GUI 로 모든 기능 제어

import tkinter as tk
from tkinter import ttk
import serial
import serial.tools.list_ports
import threading
import time


root = tk.Tk()

# GUI의 크기를 지정합니다.
root.geometry('700x500')

def ps3(): # 센서3 인식 동작
    ser.write(b"LAMP_RED=OFF\n")
    button_lamp_red.configure(text='OFF',bg='red')
    ser.write(b"LAMP_GREEN=ON\n")
    button_lamp_red.configure(text='ON',bg='green')
    sendData = f"CV_MOTOR={130}\n"
    ser.write( sendData.encode() )

def ps2(): # 센서2 인식 동작
    ser.write(b"LAMP_YELLOW=ON\n")
    button_lamp_red.configure(text='ON',bg='yellow')
    ser.write(b"LAMP_GREEN=OFF\n")
    button_lamp_red.configure(text='OFF',bg='green')
    time.sleep(2)
    ser.write(b"LAMP_RED=ON\n")
    button_lamp_red.configure(text='ON',bg='red')
    ser.write(b"LAMP_YELLOW=OFF\n")
    button_lamp_red.configure(text='OFF',bg='yellow')
    sendData = f"CV_MOTOR={0}\n"
    ser.write( sendData.encode() )
    time.sleep(3)
    ser.write(b"LAMP_RED=OFF\n")
    button_lamp_red.configure(text='OFF',bg='red')
    ser.write(b"LAMP_GREEN=ON\n")
    button_lamp_red.configure(text='ON',bg='green')
    sendData = f"CV_MOTOR={130}\n"
    ser.write( sendData.encode() )

def ps1(): # 센서1 인식 동작
    ser.write(b"LAMP_GREEN=OFF\n")
    button_lamp_red.configure(text='OFF',bg='green')
    ser.write(b"LAMP_YELLOW=ON\n")
    button_lamp_red.configure(text='ON',bg='yellow')
    time.sleep(1.5)
    ser.write(b"LAMP_RED=ON\n")
    button_lamp_red.configure(text='ON',bg='red')
    ser.write(b"LAMP_YELLOW=OFF\n")
    button_lamp_red.configure(text='OFF',bg='yellow')
    sendData = f"CV_MOTOR={0}\n"
    ser.write( sendData.encode() )
    sendData = f"SERVO_1={97}\n"
    ser.write( sendData.encode() )
    sendData = f"SERVO_3={110}\n"
    ser.write( sendData.encode() )
    time.sleep(1)
    ser.write(b"CATCH=ON\n")
    button_air_catch.configure(text='ON',bg='red')
    time.sleep(1)
    sendData = f"SERVO_1={80}\n"
    ser.write( sendData.encode() )
    time.sleep(2)
    sendData = f"SERVO_2={90}\n"
    ser.write( sendData.encode() )
    time.sleep(2)
    ser.write(b"CATCH=OFF\n")
    button_air_catch.configure(text='OFF',bg='gray')
    sendData = f"SERVO_2={180}\n"
    ser.write( sendData.encode() )

# ----------타워램프----------------
# 초기값을 설정합니다.
lamp_red_value = True
lamp_yellow_value = False
lamp_green_value = False

# 값을 반전시키는 함수를 정의합니다.
def lamp_red_button_toggle():
    global lamp_red_value
    lamp_red_value = not lamp_red_value
    if lamp_red_value:
        ser.write(b"LAMP_RED=ON\n")
        button_lamp_red.configure(text='ON',bg='red')
    else:
        ser.write(b"LAMP_RED=OFF\n")
        button_lamp_red.configure(text='OFF',bg='gray')

# 값을 반전시키는 함수를 정의합니다.
def lamp_yellow_button_toggle():
    global lamp_yellow_value
    lamp_yellow_value = not lamp_yellow_value
    if lamp_yellow_value:
        ser.write(b"LAMP_YELLOW=ON\n")
        button_lamp_yellow.configure(text='ON',bg='yellow')
    else:
        ser.write(b"LAMP_YELLOW=OFF\n")
        button_lamp_yellow.configure(text='OFF',bg='gray')

# 값을 반전시키는 함수를 정의합니다.
def lamp_green_button_toggle():
    global lamp_green_value
    lamp_green_value = not lamp_green_value
    if lamp_green_value:
        ser.write(b"LAMP_GREEN=ON\n")
        button_lamp_green.configure(text='ON',bg='green')
    else:
        ser.write(b"LAMP_GREEN=OFF\n")
        button_lamp_green.configure(text='OFF',bg='gray')

# 빨간색 램프 생성
# 버튼을 생성합니다.
button_lamp_red = tk.Button(root, text='OFF', bg='gray',width=5, height=1,command=lamp_red_button_toggle)
button_lamp_red.grid(row=0, column=0, padx=10, pady=5)
# 라벨을 생성합니다.
label_lamp_red = tk.Label(root, text='타워램프 빨간색')
label_lamp_red.grid(row=0, column=1, padx=10, pady=5)

# 노란색 램프
# 버튼을 생성합니다.
button_lamp_yellow = tk.Button(root, text='OFF', bg='gray',width=5, height=1,command=lamp_yellow_button_toggle)
button_lamp_yellow.grid(row=1, column=0, padx=10, pady=5)
# 라벨을 생성합니다.
label_lamp_yellow = tk.Label(root, text='타워램프 노란색')
label_lamp_yellow.grid(row=1, column=1, padx=10, pady=5)

# 녹색 램프
# 버튼을 생성합니다.
button_lamp_green = tk.Button(root, text='OFF', bg='gray',width=5, height=1,command=lamp_green_button_toggle)
button_lamp_green.grid(row=2, column=0, padx=10, pady=5)
# 라벨을 생성합니다.
label_lamp_green = tk.Label(root, text='타워램프 녹색')
label_lamp_green.grid(row=2, column=1, padx=10, pady=5)


# ----------서보모터-----------------
# 슬라이더에서 손을 놓았을 때 실행되는 함수를 정의합니다.
def slider_servo_1_released(event):
    value = slider_servo_1.get()
    print('slider_servo_1:', value)
    sendData = f"SERVO_1={value}\n"
    ser.write( sendData.encode() )

def slider_servo_2_released(event):
    value = slider_servo_2.get()
    print('slider_servo_2:', value)
    sendData = f"SERVO_2={value}\n"
    ser.write( sendData.encode() )

def slider_servo_3_released(event):
    value = slider_servo_3.get()
    print('slider_servo_3:', value)
    sendData = f"SERVO_3={value}\n"
    ser.write( sendData.encode() )


# 슬라이더 값을 저장하기 위한 변수를 생성합니다.
slider_value_1 = tk.DoubleVar()
slider_value_1.set(80)

slider_value_2 = tk.DoubleVar()
slider_value_2.set(180)

slider_value_3 = tk.DoubleVar()
slider_value_3.set(100)

# 슬라이더를 생성합니다.
slider_servo_1 = tk.Scale(root, from_=60, to=130, orient='horizontal', variable=slider_value_1, length=200, width=20,label='         서보모터1(60~130)')
slider_servo_1.grid(row=0, column=4, padx=20, pady=5)

slider_servo_2 = tk.Scale(root, from_=0, to=180, orient='horizontal', variable=slider_value_2, length=200, width=20,label='         서보모터2(0~180)')
slider_servo_2.grid(row=1, column=4, padx=20, pady=5)


slider_servo_3 = tk.Scale(root, from_=30, to=120, orient='horizontal', variable=slider_value_3, length=200, width=20,label='         서보모터3(30~120)')
slider_servo_3.grid(row=2, column=4, padx=20, pady=5)

# 슬라이더에서 손을 놓았을 때 실행될 함수를 지정합니다.
slider_servo_1.bind('<ButtonRelease-1>', slider_servo_1_released)
slider_servo_2.bind('<ButtonRelease-1>', slider_servo_2_released)
slider_servo_3.bind('<ButtonRelease-1>', slider_servo_3_released)


# ----------근접센서-----------------
# 근접센서1
# 라벨을 생성합니다.
label_ps_1 = tk.Label(root, text='근접센서1')
label_ps_1.grid(row=3, column=0, padx=10, pady=5)
# 버튼을 생성합니다.
button_ps_1 = tk.Button(root, text='OFF', bg='gray',width=5, height=1, state='disabled', disabledforeground='black')
button_ps_1.grid(row=4, column=0, padx=10, pady=5)

# 근접센서2
# 라벨을 생성합니다.
label_ps_2 = tk.Label(root, text='근접센서2')
label_ps_2.grid(row=3, column=1, padx=10, pady=5)
# 버튼을 생성합니다.
button_ps_2 = tk.Button(root, text='OFF', bg='gray',width=5, height=1, state='disabled', disabledforeground='black')
button_ps_2.grid(row=4, column=1, padx=10, pady=5)

# 근접센서3
# 라벨을 생성합니다.
label_ps_3 = tk.Label(root, text='근접센서3')
label_ps_3.grid(row=3, column=2, padx=10, pady=5)
# 버튼을 생성합니다.
button_ps_3 = tk.Button(root, text='OFF', bg='gray',width=5, height=1, state='disabled', disabledforeground='black')
button_ps_3.grid(row=4, column=2, padx=10, pady=5)


# ----------컨베이어 모터-----------------
# 슬라이더에서 손을 놓았을 때 실행되는 함수를 정의합니다.
def slider_convayor_released(event):
    value = slider_convayor.get()
    print('Slider convayor value:', value)
    sendData = f"CV_MOTOR={value}\n"
    ser.write( sendData.encode() )

#모터
slider_convayor_value = tk.DoubleVar()
slider_convayor_value.set(0)

# 슬라이더를 생성합니다.
slider_convayor = tk.Scale(root, from_=0, to=255, orient='horizontal', 
                           variable=slider_convayor_value, length=200, 
                           width=20, label='컨베이어 모터제어(0~255)')
slider_convayor.grid(row=4, column=4, padx=20, pady=5)

# 슬라이더에서 손을 놓았을 때 실행될 함수를 지정합니다.
slider_convayor.bind('<ButtonRelease-1>', slider_convayor_released)


# ----------가변저항 표시-----------------
# 프로그래스바를 생성합니다.
progressbar_vr_1 = ttk.Progressbar(root,orient='horizontal', mode='determinate', length=200, maximum=1023)
progressbar_vr_1.grid(row=6, column=0, columnspan=3, padx=20, pady=5)
# 프로그레스바 오른쪽에 값을 표시하는 라벨을 생성합니다.
progressbar_vr_1_label = ttk.Label(root, text='가변저항1: 0')
progressbar_vr_1_label.grid(row=6, column=3, padx=10)

# 프로그래스바를 생성합니다.
progressbar_vr_2 = ttk.Progressbar(root,orient='horizontal', mode='determinate', length=200, maximum=1023)
progressbar_vr_2.grid(row=7, column=0, columnspan=3, padx=20, pady=5)
# 프로그레스바 오른쪽에 값을 표시하는 라벨을 생성합니다.
progressbar_vr_2_label = ttk.Label(root, text='가변저항2: 0')
progressbar_vr_2_label.grid(row=7, column=3, padx=10)

# 프로그래스바를 생성합니다.
progressbar_vr_3 = ttk.Progressbar(root,orient='horizontal', mode='determinate', length=200, maximum=1023)
progressbar_vr_3.grid(row=8, column=0, columnspan=3, padx=20, pady=5)
# 프로그레스바 오른쪽에 값을 표시하는 라벨을 생성합니다.
progressbar_vr_3_label = ttk.Label(root, text='가변저항3: 0')
progressbar_vr_3_label.grid(row=8, column=3, padx=10)

# ----------공기흡입-----------------
air_catch_value = False

# 값을 반전시키는 함수를 정의합니다.
def air_catch_button_toggle():
    global air_catch_value
    air_catch_value = not air_catch_value
    if air_catch_value:
        ser.write(b"CATCH=ON\n")
        button_air_catch.configure(text='ON',bg='red')
    else:
        ser.write(b"CATCH=OFF\n")
        button_air_catch.configure(text='OFF',bg='gray')

# 라벨을 생성합니다.
label_air_catch = tk.Label(root, text='에어펌프')
label_air_catch.grid(row=6, column=4, padx=10, pady=5)
# 버튼을 생성합니다.
button_air_catch = tk.Button(root, text='OFF', bg='gray',width=5, height=1,command=air_catch_button_toggle)
button_air_catch.grid(row=7, column=4, padx=10, pady=5)


#시리얼 수신 쓰레드
def serial_read_thread():
    while True:
        if ser.in_waiting > 0:
            read_data = ser.readline()
            serial_receive_data = read_data.decode()
            print("수신:",serial_receive_data)
            if "PS_1=ON" in serial_receive_data:
                button_ps_1.configure(text='ON',bg='red')
                print(serial_receive_data)
                ps1()
                serial_receive_data =""
                continue
            elif "PS_1=OFF" in serial_receive_data:
                button_ps_1.configure(text='OFF',bg='gray')
                print(serial_receive_data)
                serial_receive_data =""
            elif "PS_2=ON" in serial_receive_data:
                button_ps_2.configure(text='ON',bg='red')
                print(serial_receive_data)
                ps2()
                serial_receive_data =""
            elif "PS_2=OFF" in serial_receive_data:
                button_ps_2.configure(text='OFF',bg='gray')
                print(serial_receive_data)
                serial_receive_data =""
            elif "PS_3=ON" in serial_receive_data:
                button_ps_3.configure(text='ON',bg='red')
                print(serial_receive_data)
                ps3()
                serial_receive_data =""
            elif "PS_3=OFF" in serial_receive_data:
                button_ps_3.configure(text='OFF',bg='gray')
                print(serial_receive_data)
                serial_receive_data =""
            elif "OK_VR_1=" in serial_receive_data:
                #print("vr1:",serial_receive_data.split("=")[1])
                vr1_value = serial_receive_data.split("=")[1]
                progressbar_vr_1['value'] = vr1_value
                progressbar_vr_1.update()
                progressbar_vr_1_label.configure(text='가변저항1: {}'.format(vr1_value))
            elif "OK_VR_2=" in serial_receive_data:
                #print("vr2:",serial_receive_data.split("=")[1])
                vr2_value = serial_receive_data.split("=")[1]
                progressbar_vr_2['value'] = vr2_value
                progressbar_vr_2.update()
                progressbar_vr_2_label.configure(text='가변저항2: {}'.format(vr2_value))
            elif "OK_VR_3=" in serial_receive_data:
                #print("vr3:",serial_receive_data.split("=")[1])
                vr3_value = serial_receive_data.split("=")[1]
                progressbar_vr_3['value'] = vr3_value
                progressbar_vr_3.update()
                progressbar_vr_3_label.configure(text='가변저항3: {}'.format(vr3_value))
            

def update_vr():
    ser.write(b"VR_1=?\n")
    ser.write(b"VR_2=?\n")
    ser.write(b"VR_3=?\n")
    root.after(1000, update_vr)

# 연결된 포트 검색
ports = list(serial.tools.list_ports.comports())

# 연결된 아두이노 포트 검색
for p in ports:
    if 'IOUSBHostDevice' in p.description:
        ser = serial.Serial(p.device, 9600)  # 아두이노와 시리얼 통신 연결
        print(f"{p.device} 포트에 자동으로 연결하였습니다.")
        break
else:
    print("아두이노를 찾을 수 없습니다.")

t1 = threading.Thread(target=serial_read_thread)
t1.daemon = True
t1.start()

update_vr()

root.mainloop()
