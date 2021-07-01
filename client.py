import socket
#determine IP and PORT number of the Server to connect
port = 5112
host= 'localhost'

if __name__ == '__main__':
        cSocket = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
        address = (host, port)
        cSocket.connect( address )
        data =cSocket.recv(2048)
        print(data.decode('ascii'))
        message=input()
        cSocket.send(message.encode('ascii'))
        data =cSocket.recv(2048)
        print(data.decode('ascii'))
        message=input()
        cSocket.send(message.encode('ascii'))

        while True :
                #recieve the questions and answer them 
                data =cSocket.recv(2048)
                
                # if we recieve "NO",we don't have a validity to do the exam
                if data.decode('ascii')=='NO':
                        print("you do not have the validity to do the exam\n")
                        cSocket.close()
                        break
                #if we recieve "OK" ,this meaning that questions are ended
                if data.decode('ascii')=='OK':
                        break
                #split method convert th recevied string to a list
                #where every element in the list is the string that acscced "  "
                dataList=data.decode('ascii').split("  ")
                for i in range(len(dataList)) :
                        print(dataList[i])
                message=input("YOUR ANSWER:  ")
                print("\n\n")
                cSocket.send(message.encode('ascii'))
        while True :
                #recieve the exam informations after finish
                for i in range(8):
                        data= cSocket.recv(2048).decode('ascii')
                        print(data)
                #finish the exam after recieve the informations
                a=input('Press (OK) to EXIT:    ')
                if a=='OK':
                        break
        cSocket.close()
