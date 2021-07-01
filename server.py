import socket

if __name__ == '__main__':
#define Ip and PORT number of Server
    host = 'localhost'
    port = 5112
#define a socket with these IP and PORT number:
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    serv.bind( ( host , port ))
    print("Ready to work>>")
    serv.listen(1)
    c=0
    while True:
        #start to accept requests from clients
        (sc , sockname )= serv.accept()
        #print a sentence to tell that a student is examined 
        print(' A student is examing now..')
        #request the student to Enter his name
        sc.send( 'Enter your name'.encode('ascii') )
        name = sc.recv(1024)
        name = name.decode('ascii')
        #show the student that is examined
        print('Student  '+name+'  is examined now')

        #request the student to Enter his ID
        sc.send('Enter your ID'.encode('ascii'))
        sid = sc.recv(1024)
        sid = int(sid.decode('ascii'))
        if sid > 210  :
            sc.send('NO'.encode('ascii'))
            sc.close()
        elif sid < 101  :
            sc.send('NO'.encode('ascii'))
            sc.close()

        else:
            print('You are welcome ; good wishes for you\n\npress "OK" to continue: ')
            #take the Questions form depending on student ID (even=> fromA,odd=>formB)
            if (sid%2) == 0 :
                qFile = open("ExamQuestionsA.txt" , 'r')
            else :
                qFile = open("ExamQuestionsB.txt" , 'r')
            questionsList =list()
            #transfer the Questions to a list "questionsList"
            for i in qFile :
                questionsList.append( i )               
            qFile.close()
        
            #take the correction form depending on student ID (even=> fromA,odd=>formB)
            if (sid%2) == 0 :
                cFile = open("correctionA.txt" , 'r')
            else :
                cFile = open("correctionB.txt" , 'r')
            answerList=list()
            #transfer the Questions to a list "questionsList"
            for i in cFile :
                answerList.append( i )               
            cFile.close()
            answer=list()
        
            while True :
                    #start the exam that had 8 questions
                    for i in range(8):
                        reply = questionsList[i] +"\n"
                        sc.send(reply.encode('ascii'))
                        answer1 = sc.recv(1024).decode('ascii')
                        answer.append(answer1)
                    #take the answers and append them to a list "answerList"
                    for i in range(8):
                        if (answer[i]+'\n')==answerList[i]:
                            c=c+1
                
                    sc.send('OK'.encode('ascii'))
                    #calculate the percent grade
                    GP = (c*100)/8;
                    #determine the state of the student
                    if GP >= 50:
                        state="Succeeded"
                    else:
                        state="Failed"
                    #Copy student's informations to a text file ("Result.txt")
                    aFile = open('Result.txt' , 'w')
                    aFile.write("Student's Exam Informations :\n\n")
                    aFile.write("Student's names :  ")
                    aFile.write(name)
                    aFile.write("\n")
                    aFile.write("Student's ID:  ")
                    aFile.write(str(sid))
                    aFile.write("\n")
                    aFile.write("Number of true answers:  ")
                    aFile.write(str(c))
                    aFile.write("\n")
                    aFile.write("Number of false answers:  ")
                    aFile.write(str(8-c))
                    aFile.write("\n")
                    aFile.write("Grade percent:  ")
                    aFile.write(str(GP))
                    aFile.write(" %\n")
                    aFile.write("State is: ")
                    aFile.write(state)
                    aFile.close()
                    #--------------
                    #send the informations to the student(client) :
                
                    infor = open('Result.txt' , 'r')
                    inforList = list()
                    for i in infor :
                        inforList.append( i )               
                    infor.close()
                    for i in range(8):
                        reply = inforList[i] 
                        sc.send(reply.encode('ascii'))
                    sc.send('\nThank you,you have ended exam succesfuly \n'.encode('ascii'))
                    sc.close()
                    break
				
            serv.close()
