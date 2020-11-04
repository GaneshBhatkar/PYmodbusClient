from pymodbus.client.sync import ModbusSerialClient as Modbusclient
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
#from pymodbus.client.sync import ModbusUdpClient as ModbusClient

from pymodbus.register_read_message import ReadInputRegistersResponse
#from pymodbus.transaction import ModbusRtuFramer
import struct
from utils import FloatData



# For reading Descrete inputs
def Read_Discrete_Inputs(Address,Registers,Slave_Id):
    
    discrete_inputs_value = client.read_discrete_inputs(Address,Registers,unit=Slave_Id)
    #bits to read discrete input
    for i in range(0,8):
        print(discrete_inputs_value.bits[i])
        if i==(Number_Of_Registers-1): 
            break

while 1:
    Modbus_Protocol= input('TCP or RTU ')

    if Modbus_Protocol.upper()=='RTU':
        client=Modbusclient(method='rtu',port='COM4',stopbits=1,bytesize=8,baudrate=9600,timeout=0.3)
        connection=client.connect()
        print(connection)

    if Modbus_Protocol.upper()=='TCP':
        client = ModbusClient('192.168.1.65', port=8000)
        connection=client.connect()
        print(connection)

    while 1:
        Starting_Address=int(input('Enter starting register '))-1
        Number_Of_Registers=int(input('Enter no of register '))
        Slave_Id=int(input('Enter Slave id '))

        Read_Discrete_Inputs(Starting_Address,Number_Of_Registers,Slave_Id)

        Exit=input('Exit  y/n ')

        if Exit.upper()=='Y':
            print('Exit')
            break
    
