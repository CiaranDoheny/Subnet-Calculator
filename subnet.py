# Ask for an IP address, split it into the 4 octets and change them to an int from a string
# Then confirm that it is a valid IP address, print out any errors in an octet

ipaddress = input("What is the IP address?:")
ipadd = ipaddress.split(".")

ipoct1 = ipadd[0]
ipoct1 = int(ipoct1)
ipoct2 = ipadd[1]
ipoct2 = int(ipoct2)
ipoct3 = ipadd[2]
ipoct3 = int(ipoct3)
ipoct4 = ipadd[3]
ipoct4 = int(ipoct4)

if ipoct1 > 255:
    print(f"{ipoct1} is not a valid number in the 1st octet, up to 255 only")
elif ipoct2 > 255:
    print(f"{ipoct2} is not a valid number in the 2nd octet, up to 255 only")	
elif ipoct3 > 255:
    print(f"{ipoct3} is not a valid number in the 3rd octet, up to 255 only")
elif ipoct4 > 255:
    print(f"{ipoct4} is not a valid number in the 4th octet, up to 255 only")
else:
    print (f"{ipaddress} is a valid IP address")


# Ask for a subnet mask, turn the string into a int
# Calculate and print out the number of useable hosts in that range
# Print bespoke outputs for /31 and /32 (maths functions don't work for these) 

submask = input("What is the subnet mask?:")
submask = int(submask)

hosts = 32 - submask
hosts = 2**hosts - 2

if submask > 32:
    print(f"{submask} is not a valid subnet mask, up to 32 bits only.")
elif submask == 31:
    print("/31 can be used as a point-to-point address only")
elif submask == 32:
    print("/32 has no usable host addresses and is typically used as a loopback address")
else:
    print (f"There are {hosts} host addresses in {ipaddress}/{submask}")



# Below this is test code, works only for a /26 - I'm sure that this could be done better

if submask == 26 and ipoct4 >= 0 and ipoct4 < 64:
    print(F"The Network is:\t\t{ipoct1}.{ipoct2}.{ipoct3}.0/{submask}\nFirst available IP is:\t {ipoct1}.{ipoct2}.{ipoct3}.1\nLast available IP is:\t {ipoct1}.{ipoct2}.{ipoct3}.62\nBroadcast Address is:\t {ipoct1}.{ipoct2}.{ipoct3}.63")
elif submask == 26 and ipoct4 >= 64 and ipoct4 < 128: 
    print(F"The Network is:\t\t{ipoct1}.{ipoct2}.{ipoct3}.64/{submask}\nFirst available IP is:\t {ipoct1}.{ipoct2}.{ipoct3}.65\nLast available IP is:\t {ipoct1}.{ipoct2}.{ipoct3}.126\nBroadcast Address is:\t {ipoct1}.{ipoct2}.{ipoct3}.127")
elif submask == 26 and ipoct4 >= 128 and ipoct4 < 192:
    print(F"The Network is:\t\t{ipoct1}.{ipoct2}.{ipoct3}.128/{submask}\nFirst available IP is:\t {ipoct1}.{ipoct2}.{ipoct3}.129\nLast available IP is:\t {ipoct1}.{ipoct2}.{ipoct3}.190\nBroadcast Address is:\t {ipoct1}.{ipoct2}.{ipoct3}.191")
elif submask == 26 and ipoct4 >= 192 and ipoct4 < 255: 
    print(F"The Network is:\t\t{ipoct1}.{ipoct2}.{ipoct3}.192/{submask}\nFirst available IP is:\t {ipoct1}.{ipoct2}.{ipoct3}.193\nLast available IP is:\t {ipoct1}.{ipoct2}.{ipoct3}.254\nBroadcast Address is:\t {ipoct1}.{ipoct2}.{ipoct3}.255")
