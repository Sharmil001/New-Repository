
from threading import*
import time

#'d' is the dictionary in which we store data
d={} 

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout
def create(key,value,timeout=0):
    if key in d:
        print("error: This key already exists") #error message1
    else:
        if(key.isalpha()):  

            #constraints for file size less than 1GB and Jasonobject value less than 16KB 
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]

                #constraints for input key_name capped at 32chars
                if len(key)<=32: 
                    d[key]=l

            #error message2
            else:
                print("error: Memory limit exceeded!! ")
                
        #error message3
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")



#for read operation
#use syntax "read(key_name)"            
def read(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=d[key]
        if b[1]!=0:
            #comparing the present time with expiry time
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                #error message5
                print("error: time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri



#for delete operation
#use syntax "delete(key_name)"
def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del d[key]
            print("key is successfully deleted")
