def IP_to_Binary_code_32 (vroodi):
    """
    input your IP and this 
    function will procces on that 
    and will give you that IPs 
    binary. 

    Parameters
    ----------
    vroodi : str
        this function need to input string 
        to do some string methods .
    Returns:
        Binary of your IP
    -------
    output parameter:
        str
    """
    
    ip, prefix_str = vroodi.split("/")
    prefix = int(prefix_str) 
    tikeha = ip.split(".")
    binary_ha = [format(int(b), "08b")  for b in tikeha ]
    return"".join(binary_ha), prefix


def IP_to_Binary_code_dotted (vroodi):
    """
    input your IP and this 
    function will procces on that 
    and will give you that IPs 
    binary (splited with dot (.)).

    Parameters
    ----------
    vroodi : string
        this function need to input string 
        to do some string methods .

    return:
        binary they are splited with dot(.) .
    -------
    output parameter:
        str
    """
    
    ip, prefix_str = vroodi.split("/")
    prefix = int(prefix_str)
    tikeha = ip.split(".")
    binary_ha = [format(int(b), "08b")  for b in tikeha ]
    return".".join(binary_ha), prefix
    

def Find_Prefix_merg (bin1, prefix1, bin2, prefix2):
    """
    this function will work on your prefixs
    enumerate and zip your data of prefixs 
    and output your recommeded prefix for 
    that merge. 

    Parameters
    ----------
    ips1 : str
        IPto.. defs will automaticly 
        Separate prefix of IP.
    ips2 : str
        IPto.. defs will automaticly 
        Separate prefix of IP..

    Returns:
        your prefix for merge
    -------
    output parameter:
        str
    """
    
    net1 = bin1[:prefix1] + "0" * (32 - prefix1)
    net2 = bin2[:prefix2] + "0" * (32 - prefix2)
    for i, (b1, b2) in (enumerate(zip(net1, net2))):
        if b1 != b2 : 
            return i
    return prefix1
    
while True :

    vroodi = input("Enter your ip (IP/PREFIX) : ") 
    ips1 = IP_to_Binary_code_32(vroodi)
    print(f"IP to binary code 32(sprit) :      {IP_to_Binary_code_32(vroodi)}")
    print("\n")
    print(f"IP to binary code 32(dotted) :     {IP_to_Binary_code_dotted(vroodi)}\n\n")
    
    mergcon = input("\nWanna merge? n/y : ")
    if mergcon.lower() == "y":
        
        
        vroodi2 = input("\nEnter your second ip (IP/PREFIX) : ")  
    
    
        ips2 = IP_to_Binary_code_32(vroodi2)
    

        print(f"/nIP to binary code 32(sprit) :      {IP_to_Binary_code_32(vroodi2)}")
        print("\n")
        print(f"IP to binary code 32(dotted) :        {IP_to_Binary_code_dotted(vroodi2)}")
        
        print ("\n")
    
    
    
    
    
        print(f"Your Prefix for classless :           {Find_Prefix_merg (ips1[0], ips1[1], ips2[0], ips2[1] )}")

        edame = input("\n \nDo you wanna con ? n/y : ")  
        if edame.lower() == "n" :
            print ("byby")
            break 
        continue
    print("byby")
    break