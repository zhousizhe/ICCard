import time
from operator import xor

import serial as serial
import serial.tools.list_ports
import binascii

def getDate(comArr):
    # 遍历所有串口发送机器复位指令，如成功返回说明读卡器连接成功
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) <= 0:
        print('找不到串口')
        return False
    else:
        for i in range(0, len(port_list)):
            prot_list_i = list(port_list[i])
            port_serial = prot_list_i[0]
            serial_1 = serial.Serial(port_serial, 9600, timeout=20)
            # cmd_send = bytes([0x00, 0x02, 0x00, 0x02, 0x31, 0x30, 0x03, 0x02, 0x01]) 测试数据,卡机状态
            cmd_send = bytes(comArr)
            # print(cmd_send)
            # 发送数据
            serial_1.write(cmd_send)
            time.sleep(1)
            # 读取返回值
            data = serial_1.read_all()
            # print(bytes.decode(data, encoding="utf-8"))
            # 将数据转成十六进制的形式
            datas = ''.join(map(lambda serial_1: ('/x' if len(hex(serial_1)) >= 4 else '/x0') + hex(serial_1)[2:], data))
            # 将字符串分割
            new_datas = datas.split("/x")
            # 清除空白数据
            new_datas.remove("")
            # 如果返回值为空则设备未响应指令
            if len(new_datas) <= 0:
                serial_1.close()
                continue
            # need是拼接出来的数据，比如：001a
            # need = new_datas[4] + new_datas[5];
            # print(new_datas)
    # 必须关闭链接
    serial_1.close()
    return new_datas

def inputToHex(test):
    cStr = str(test)
    dateBytes = bytes(cStr, encoding="utf-8")
    if len(dateBytes) <= 16:
        zeroBytes = bytes(16 - len(dateBytes))
        dateBytes = zeroBytes.__add__(dateBytes)
    else:
        dateBytes = bytes(16)
    datas = ''.join(
        map(lambda serial_1: ('/x' if len(hex(serial_1)) >= 4 else '/x0') + hex(serial_1)[2:], dateBytes))
    # 将字符串分割
    new_datas = datas.split("/x")
    # 清除空白数据
    new_datas.remove("")
    tenArr = [(int(ten_arr, 16)) for ten_arr in new_datas]
    tenArr.append(0x03)
    return tenArr

def BCCCheck(cmdArr):
    xorData = 0x00
    tempLen = 1
    while tempLen < len(cmdArr):
        if tempLen == 1:
            xorData = xor(cmdArr[0], cmdArr[1])
        else:
            xorData = xor(xorData, cmdArr[tempLen])
        tempLen = tempLen + 1
    # print(xorData)
    cmdArr.append(xorData)
    return cmdArr

def writeDisk(addCmdTitle,dateHex ):
    addCmdTitle.extend(dateHex)
    cmd = BCCCheck(addCmdTitle)
    result = getDate(cmd)
    return result

def cmdResultResolve(hexStr):
    try:
        hexStr = replaceZero(hexStr)
        byteStr = bytes.fromhex(hexStr)
        resultResolve = str(byteStr, encoding="utf-8")
        return resultResolve
    except BaseException:
        return hexStr

# def cmdResultResolveInt(hexInt):
#     try:
#         resultResolve = ""
#         byteInt = bytes.fromhex(hexInt)
#         for i in byteInt:
#             resultResolve = resultResolve + str(i)
#         return resultResolve
#     except BaseException:
#         return hexInt

def replaceZero(hexStr):
    i = 0
    while i < len(hexStr)-1:
        if hexStr[i] == "0" and hexStr[i+1] == "0":
            i = i+2
        else:
            return hexStr[i:]

# bytes.decode(data, encoding='utf-8')
