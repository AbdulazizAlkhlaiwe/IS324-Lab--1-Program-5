size= float(input('Enter the size of data in MBs : '))
dig = int(input('How many digits to show after the decimal point? '))
GB = size/1024
f= format(GB, '.'+ str(dig) + 'f')
print('Size in GB : ',f )