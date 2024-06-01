import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("select Port: COM")

for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])
    else:
        print("COM" + str(val) + " is not listed in port list.")

serialInst.baudrate = 115200
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
            packet = serialInst.readline().decode('utf8')
            print(packet)