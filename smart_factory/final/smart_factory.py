import time
import serial
import serial.tools.list_ports
import threading

# File path
file_path = r'/Users/yujaemin/Desktop/python/received_ids.txt'

# Function to check if a string is numeric
def is_numeric(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# ----------타워램프----------------
# 초기값을 설정합니다.
lamp_red_value = True
lamp_yellow_value = False
lamp_green_value = False

global int_ID
global serial_receive_data

# 값을 반전시키는 함수를 정의합니다.
def lamp_red_button_toggle():
    global lamp_red_value
    lamp_red_value = not lamp_red_value
    if lamp_red_value:
        ser.write(b"LAMP_RED=ON\n")
    else:
        ser.write(b"LAMP_RED=OFF\n")

# 값을 반전시키는 함수를 정의합니다.
def lamp_yellow_button_toggle():
    global lamp_yellow_value
    lamp_yellow_value = not lamp_yellow_value
    if lamp_yellow_value:
        ser.write(b"LAMP_YELLOW=ON\n")
    else:
        ser.write(b"LAMP_YELLOW=OFF\n")

# 값을 반전시키는 함수를 정의합니다.
def lamp_green_button_toggle():
    global lamp_green_value
    lamp_green_value = not lamp_green_value
    if lamp_green_value:
        ser.write(b"LAMP_GREEN=ON\n")
    else:
        ser.write(b"LAMP_GREEN=OFF\n")

def ps1(): # 센서1 인식 동작
    ser.write(b"LAMP_RED=OFF\n")
    ser.write(b"LAMP_GREEN=ON\n")
    sendData = f"CV_MOTOR={130}\n"
    ser.write(sendData.encode())

def ps2(): # 센서2 인식 동작
    ser.write(b"LAMP_YELLOW=ON\n")
    ser.write(b"LAMP_GREEN=OFF\n")
    time.sleep(2)
    ser.write(b"LAMP_RED=ON\n")
    ser.write(b"LAMP_YELLOW=OFF\n")
    
    sendData = f"CV_MOTOR={0}\n"
    ser.write(sendData.encode())
    time.sleep(2)
    sendData = f"CV_MOTOR={130}\n"
    ser.write(sendData.encode())
    ser.write(b"LAMP_RED=OFF\n")
    ser.write(b"LAMP_GREEN=ON\n")


def ps3(angle1,angle2,angle3): # 센서3 인식 동작
    ser.write(b"LAMP_GREEN=OFF\n")
    ser.write(b"LAMP_YELLOW=ON\n")
    time.sleep(1.5)
    ser.write(b"LAMP_RED=ON\n")
    ser.write(b"LAMP_YELLOW=OFF\n")
    sendData = f"CV_MOTOR={0}\n"
    ser.write(sendData.encode())
    sendData = f"SERVO_1={97}\n"
    ser.write(sendData.encode())
    sendData = f"SERVO_3={110}\n"
    ser.write(sendData.encode()) #박스 내려 꽃는 동작
    time.sleep(1)
    ser.write(b"CATCH=ON\n")
    time.sleep(1)

    sendData = f"SERVO_1={80}\n"
    ser.write(sendData.encode())
    time.sleep(0.5)
    sendData = f"SERVO_2={180}\n"
    ser.write(sendData.encode())
    time.sleep(0.5) #박스 들어올리는 동작
    
    
    
    sendData = f"SERVO_2={angle2}\n"#angle2 숫자 클수록 고개 조금 돌림
    ser.write(sendData.encode())
    time.sleep(0.5)
    sendData = f"SERVO_3={angle3}\n"# angle1 숫자 낮아지면 고개 위로 올림
    ser.write(sendData.encode())
    time.sleep(0.5)
    sendData = f"SERVO_1={angle1}\n"# angle1 숫자 낮아지면 고개 위로 올림
    ser.write(sendData.encode())
    
    




  
    time.sleep(1)

    ser.write(b"CATCH=OFF\n")
    time.sleep(2)
    sendData = f"SERVO_1={80}\n"
    ser.write(sendData.encode())
    sendData = f"SERVO_2={180}\n"
    ser.write(sendData.encode())
    sendData = f"SERVO_3={180}\n"# angle1 숫자 낮아지면 고개 위로 올림
    ser.write(sendData.encode())
    
    


    

# Serial receive thread
serial_receive_data = ""
def serial_read_thread():
    global int_ID
    global serial_receive_data
    angles = [80, 70, 180]
    while True:
        if ser.in_waiting > 0:
            read_data = ser.readline()
            serial_receive_data = read_data.decode()
            print(serial_receive_data)

            if ("PS_3=ON" in serial_receive_data):
                ps1()
                serial_receive_data =""
            elif ("PS_3=OFF" in serial_receive_data):
                serial_receive_data =""
            elif ("PS_2=ON" in serial_receive_data):
                ps2()
                serial_receive_data =""
            elif ("PS_2=OFF" in serial_receive_data):
                serial_receive_data =""
            elif ("PS_1=ON" in serial_receive_data):
                
                if (int_ID == 1):
                    angles = [130, 130, 80]
                    print("1")
                elif(int_ID == 2):
                    angles = [130, 90, 100]
                    print("2")
                elif(int_ID == 3):
                    angles = [130,40, 85]
                    print("3")
                ps3(angles[0],angles[1],angles[2])
                time.sleep(5)
                serial_receive_data =""
            elif ("PS_1=OFF" in serial_receive_data):
                serial_receive_data =""    


def main():
    global int_ID  # Declare int_ID as a global variable
    try:
        while True:
            # Read the file for new numeric IDs
            with open(file_path, 'r') as file:
                lines = file.readlines()

            for line in lines:
                line = line.strip()
                if is_numeric(line):
                    # Process the numeric ID
                    print(f"Numeric ID: {line}")
                    print(type(line))
                    int_ID = int(line)

            # Clear the file contents
            with open(file_path, 'w') as file:
                file.write("")

            time.sleep(0.1)

    except KeyboardInterrupt:
        # Clear the file contents
        with open(file_path, 'w') as file:
            file.write("")


if __name__ == '__main__':
    # Search for connected ports
    ports = list(serial.tools.list_ports.comports())

    # Search for the connected Arduino port
    for p in ports:
        if 'IOUSBHostDevice' in p.description:
            ser = serial.Serial(p.device, 9600)  # Connect to Arduino via serial communication
            print(f"Connected to port: {p.device}")
            break
    else:
        print("Arduino not found.")
    
    t1 = threading.Thread(target=serial_read_thread)
    t1.daemon = True
    t1.start()

    main()
    ser.close()



