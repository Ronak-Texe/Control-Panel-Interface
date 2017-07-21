# Doing the bitwsie operation with integer is same as doing with hexadecimal


def HexCombine(bitmap,byte,shift_bit):
    temp_hexa=0x00000000
    
    for i in range(byte):
        temp_int=int(bitmap[i],16)
        if(shift_bit>=0):
            temp_hexa=((temp_int<<shift_bit) | temp_hexa)
            # temp_hexa |= (temp_int << shift_bit)
            #print(temp_hexa)
            shift_bit -= 8
    return(temp_hexa)
    
def CalcDeviceNum(bitmap,byte,shift_bit):
    device_number=[]
    temp_hexa=HexCombine(bitmap,byte,shift_bit)
    for i in range(byte*8):
        if(temp_hexa & (1<<i)):
            device_number.append((i+1))
            
    if(device_number==[]): #If no device underwent change so it should store 0 and print that
        device_number=0
        
    return(device_number)
    


