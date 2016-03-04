
if __name__=='__main__':
        f=open('akkaDict.txt','a')
        while(True):
                a=input()
                if(a=='over'):
                        break
                print(a,file=f)

        f.close()
        
