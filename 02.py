details="""I am Dheeraj Tiwari
 i a'/m from Kushinagr 
 i did my graduation from Ghaziabad"""

print(details)

myArr = [1,2,3,4]
print(myArr)

# looping through array

myName='saumya'
for i in myName:
    print(i)


#String Length
print(len(myName))

var1='a' in myName 
print((var1)) #True

var1='D' in myName 
print((var1)) #False


MyName1="Dheeraj Tiwari"
#slicing
print(MyName1[0:7]) #Dheeraj
print(MyName1[0:]) #Dheeraj Tiwari
print(MyName1[:]) #Dheeraj Tiwari
print(MyName1[:12]) #Dheeraj Tiwari
print(MyName1[8:]) #Dheeraj Tiwari


# convert into lower and Upper case
sisName='ShilPi'
print(sisName.upper()) # SHILPI
print(sisName.lower()) # SHILPI


#remove White spaces
ExmpName="  Rahul"
print(ExmpName)
print(ExmpName.strip())