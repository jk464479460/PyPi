
if __name__=='__main__':
        f=open('akkaDict.txt','a')
        while(True):
                a=input()
                b=input()
                if(a=='over'):
                        break
                if(b=='exit'):
                        print('cacel text')
                        continue;
                print(a,file=f)
                print('go on',end='')

        f.close()
        
