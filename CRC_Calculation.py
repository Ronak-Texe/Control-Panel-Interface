
def UpdateCRC8(crc,data):
    crc^=data
    for i in range(8):# Why 8 times loop thats why it gets multiplied by number of times
        
        if(crc & 0x80):
            crc=(crc<<1)^(0x85)
           # print(crc)
            #print("\nYou have reached here\n")
        else:
            crc=crc<<1
    return (crc)
    
def CalcRC8(data,byte):
    crc=0xff
    for i in range(byte):
        crc=UpdateCRC8(crc,data[i])
    return(hex(crc & 0xff))# Masking of data to make sure that it remains within the 32 bit number

def CompareCRC(initial_data, final_crc):
    if(int(initial_data,16)==int(final_crc,16)):
        print("CRC Matched")
    else:
        print("CRC Fail to Match")