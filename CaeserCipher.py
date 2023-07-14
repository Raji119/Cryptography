try:
 key=int(input("Enter a Number:"))
 str=input("Enter Value:")
 ns=""

 for i in range(0,len(str)):
  if(str[i].isalpha()):
   pos=ord(str[i])+key%26
   if(pos>122):
    pos=pos-26
   elif(pos>90 and (not str[i].lower())):
    pos=pos-26
   ns+=chr(pos)
  else:
   ns+=str[i]

 print("The Encrypted Value is:",ns)
except KeyboardInterrupt:
 print("Invalid Input...");

