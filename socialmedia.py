menu=0
logged_in_name=""
user=dict()
a=open("users.txt")
for line in a.readlines():
  for _ in line:
    username=line[:line.index(";")]
    line=line[line.index(";")+1:]
    password=line[:line.index(";")]
    line=line[line.index(";")+1:]
    friends=line[:len(line)-1]
    user[username]=[password,friends]
    break

def menu1(x,y,logged_in_name):
  if x in user.keys() and user[x][0]==y:
    print("Logged in\n")
    logged_in_name=logged_in_name.append(x)
    return logged_in_name
  else:
    print("Wrong password or username\n")
def menu2(z,n):
  def password_condition(z,pass_cond):
    length=0
    letter=0
    number=0
    if len(z)<8 and len(z)>=4:
      length=1
    for i in z:
      if i.isnumeric()==True:
        number=1
      else:
        continue
    for i in z:
      if i.isnumeric()==False:
        letter=1
    if letter==1 and number==1 and length==1:
      pass_cond.append(1)
    else:
      print(letter,number,length)
      pass_cond=list()
    if pass_cond==list():
      print("Password not valid\n")
    return pass_cond

  def username_condition(n,user_cond):
    number=0
    letter=0
    lower=0
    punc=0
    contains=0
    punctuations='''!()-[]{};“:”'"\,<>./?@#$%^&*_~'''
    if n not in user.keys():
      contains=1
    for i in n:
      if i.isnumeric()==True:
        number=1
    for i in n:
      if i.isnumeric()==False:
        letter=1
    if n.lower()==n:
      lower=1
    for i in punctuations:
      if i in n:
        punc=1
    if number==1 or letter==1:
      user_cond.append(1)
      if lower==1 and punc==0 and contains==1:
        user_cond.append(2)
    else:
      user_cond=list()
      print("Username not valid\n")
    return user_cond

  pass_cond=list()
  user_cond=list()
  password_condition(z,pass_cond)
  username_condition(n,user_cond)
  
  if pass_cond==[1] and user_cond==[1, 2]:
    user[n]=[z,""]

def menu3(logged_in_name):
  if logged_in_name=="":
    print("You need to log in first\n")
  elif logged_in_name!="":
    logged_in_name=logged_in_name[0]
    friend_name=input("Please enter the name of your new friend:\n")
    if friend_name!=logged_in_name and friend_name in user.keys():
      if len(user[logged_in_name][1])>0:
        user[logged_in_name][1]=user[logged_in_name][1]+","+friend_name+","
        user[logged_in_name][1]=user[logged_in_name][1][:len(user[logged_in_name][1])-1]
      if len(user[logged_in_name][1])==0:
        user[logged_in_name][1]=user[logged_in_name][1]+friend_name
    elif friend_name!=logged_in_name and friend_name not in user.keys():
      print("Friend not found\n")

def menu4(logged_in_name):
  if logged_in_name=="":
    print("You need to log in first\n")
  elif logged_in_name!="":
    logged_in_name=logged_in_name[0]
    print(user[logged_in_name][1]) 

def menu5():
  save=open("users.txt","w")
  for i in user.keys():
    save.write(i+";"+user[i][0]+";"+user[i][1]+"\n")
  save.close()
while menu!=5:
  menu=int(input("1. Log in / change user\n2. Create new user\n3. Add friend\n4. Show my friends\n5. Exit\n"))

  while menu>5 or menu<1:
    print("Invalid option\n") 
    menu=int(input("1. Log in / change user\n2. Create new user\n3. Add friend\n4. Show my friends\n5. Exit\n"))
  if menu==1:
    username_requested=input("Please enter username:\n")
    password_requested=input("Please enter password:\n")
    logged_in_name=list()
    menu1(username_requested,password_requested,logged_in_name)
  if menu==2:
    username_requested_=input("Please enter username:\n")
    password_requested_=input("Please enter password:\n")
    menu2(password_requested_,username_requested_)
  if menu==3:
    menu3(logged_in_name)
  if menu==4:
    menu4(logged_in_name)
  if menu==5:
    menu5()
