
def DeviceStatus(status):
    device_status=[]
    for i in range(8):
        if(int(status,16) & (1<<i)):
            if(i==0):
                device_status.append('Front Tamper')
            if(i==1):
                device_status.append('Rear Tamper')
            if(i==2):
                device_status.append('Mask')
            if(i==3):
                device_status.append('Device Fault')
            if(i==4):
                device_status.append('Power Failure')
                
        if(device_status==[]):
            device_status.append('Normal')
            
    return(device_status)
    