import serial

# Serial port information
port = 'COM17'  # Change it according to the port number
baudrate = 9600  # set the same baud rate as Arduino code

# File path
file_path = 'received_ids.txt'

# Create serial communication object
ser = serial.Serial(port, baudrate)

# Read existing contents of the file
file = open(file_path, 'r')
existing_ids = file.read().strip()
file.close()

# Read data
while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        
        # Check if the data contains '='
        if '=' in data:
            id = data.split('=')[1]
        else:
            id = data
            
        # Append new ID to existing contents
        updated_ids = existing_ids + '\n' + id

        # Write updated contents back to the file
        file = open(file_path, 'w')
        file.write(updated_ids)
        file.close()

        print(f'Received ID: {id}')

# Close the serial port
ser.close()
