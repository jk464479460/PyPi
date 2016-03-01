import socket;
import threading;
import time;

data="%s" %'?{"infoType":10,"clientID":123,"infoDesc":"问询报文","source":"wms","destination":"wcs","serial":1235,"content":{"objectID":"0","objectDesc":"InitAll"}}$';


def ClientRec():
     sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM);
     try:
          sock.connect(('192.168.1.157', 9000));
          sock.sendall(data.encode(encoding='utf_8'));
     except:
          print('error connect\n')
          return
          
     while True:
          try:
               
               szBuf=sock.recv(10024);
               if not len(szBuf):
                    print('not szBuf ')
               byt = 'recv:\n' + szBuf.decode('utf8')
               
               print('jj %d \n' %len(szBuf),end='')
               #sock.close()
          except Exception:
               print('error recv %r \n')
               return
          
                    
     print('end of the connecct',end='')
     
def TestServer():
     for i in range(1,5):
          time.sleep(2);
          t=threading.Thread(target=ClientRec);
          t.start();

if '__main__'==__name__:
    for i in range(1,2):
        t=threading.Thread(target=TestServer);
        time.sleep(1);
        t.start();
    #print('over',end='')
        
    
    
