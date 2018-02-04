import sys
import  os,subprocess

def rm(image):
    print image
    docker=subprocess.Popen(["docker","rmi", image,"--force"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output,errors=docker.communicate()
    print output,errors
    
def image_name():
    #t,errors=[]
    p=subprocess.Popen(["docker","images","-aq"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    t,errors=p.communicate()
    return  [ x for x in t.split('\n') if x != '' ] 

if __name__=="__main__":
  
    
#    print image_name() 
    map(rm,image_name())
