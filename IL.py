def FindIt():
     path='''IL.txt''';
     f=open(path, 'r');
     allLine=f.readlines()
     f.close()
     print(len(allLine))
     while True:
          inputStr=input();
          #print('input %s' %inputStr)
          if(isinstance(inputStr, str)==False):
               print('must be str')
               continue
          if(inputStr=='n'):
               return
          if(inputStr=="all"):
               for line in allLine:
                    print(line,end='')
               print('all show',end='')
               
          for line in allLine:
               if(line.find(inputStr,0,len(inputStr))!=-1):
                    print(line)
                    break
                  
     

if '__main__'==__name__:
   FindIt()

     
     
        
    
    
