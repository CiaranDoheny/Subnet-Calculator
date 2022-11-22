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

submask = input("What is the subnet mask?:")
submask = int(submask)

if submask > 32:
    print(f"{submask} is not a valid subnet mask, up to 32 bits only.")
	
hosts = 32 - submask
hosts = 2**hosts - 2

print (f"There are {hosts} host addresses in that range")
