import socket
import threading
import time
import zlib

data="%s" %'?{"infoType":10,"clientID":123,"infoDesc":"问询报文","source":"wms","destination":"wcs","serial":1235,"content":{"objectID":"50","objectDesc":"InitAll"}}$';

def UnPackJson(str):
     return str[1:len(str)-1]

def Compress(str):
    try:
        print('%d' %len(str))
        r=zlib.compress(str.encode(encoding='utf-8'))

        #d=zlib.decompress(r)
        #print(u'%s' %d.decode('utf-8'))
        return r;
    except OSError:
        pass
        print(r'error')

def DeCompress(r):
    try:
        d=zlib.decompress(r)
        print(u'%s' %d.decode('utf-8'))
        return r;
    except OSError:
        pass
        print(r'error')

def ClientRec():
     sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM);
     try:
          sock.connect(('115.29.251.85', 9000));
          sock.sendall(data.encode(encoding='utf_8'));
     except:
          print('error connect\n')
          return
          
     while True:
          try:
               
               szBuf=sock.recv(10024);
               if not len(szBuf):
                    print('not szBuf ')
               byt = 'recv:\n' + UnPackJson(szBuf.decode('utf8'))
               
               print('rec %s \n' %(byt),end='')
               #sock.close()
          except Exception:
               print('error recv %r \n')
               return
          
                    
     print('end of the connecct',end='')
     
def TestServer():
     for i in range(1,40):
          time.sleep(1);
          t=threading.Thread(target=ClientRec);
          t.start();


if '__main__'==__name__:
    for i in range(1,2):
        t=threading.Thread(target=TestServer);
        time.sleep(1);
        t.start();
    #print('over',end='')
        
    
    
