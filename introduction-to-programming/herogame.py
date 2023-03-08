print("Welcome to Hero’s 5 Labors!")
foot=20
pegasus=50
hero_hp_loss_for_hour=10
pegasus_hp_loss_for_hour=15
hero_hp=3000
pegasus_hp=550
hour_total=0
travel_types=["foot","pegasus"]
task_list=[["Task1",-1,400,50],["Task2",-1,500,100],["Task3",600,500,75],["Task4",1000,500,50],["Task5",900,700,80]]

while task_list!=[]:
  print("Remaining HP for Hero :",hero_hp)
  print("Remaining HP for Pegasus:",pegasus_hp)
  print("Here are the tasks left that hero needs to complete:")
  print("TaskName  ","ByFootDistance   ","ByPegasus    ","HPNeeded   ")
  #here, we print the tasks recursively
  def print_remaining_tasks(task_list):
    if task_list==[]:
      return "" 
    else:
      print(task_list[0][0] , "     " , task_list[0][1] ,"               " , task_list[0][2] , "          ",task_list[0][3])
      return print_remaining_tasks(task_list[1:])

  print_remaining_tasks(task_list)

  tasks=[]
  for i in task_list:
    tasks.append(i[0])
  for i in range(len(tasks)):
    tasks[i]=tasks[i].lower()  
  mission=input("Where should Hero go next?")
  mission=mission.lower()  
  while mission not in tasks:
    print("Invalid input")
    mission=input("Where should Hero go next?")
    mission=mission.lower()
  travel_type=input("How do you want to travel?(Foot/Pegasus)​")
  travel_type=travel_type.lower()
  for i in task_list:
    if i[0].lower()==mission:
      index_of_mission=task_list.index(i)
      selected_mission_requirements=i
  #checking if we can achieve the mission with pegasus
  hour_pegasus = selected_mission_requirements[2]/pegasus
  pegasus_hp_test = pegasus_hp - hour_pegasus * pegasus_hp_loss_for_hour
  hero_hp_test_pegasus = hero_hp - hour_pegasus * hero_hp_loss_for_hour - selected_mission_requirements[3]

  #checking if we can achieve the mission on foot 
  hour_foot = selected_mission_requirements[1]/foot
  hero_hp_test_foot = hero_hp - hour_foot * hero_hp_loss_for_hour - selected_mission_requirements[3]
  
  #we check if hero's and pegasus's hp will be enough for the task or not
  if hero_hp_test_pegasus <= 0 and hero_hp_test_foot <= 0:
    print("Game over")
    break    
  elif pegasus_hp_test<=0 and selected_mission_requirements[1]==-1:
    print("Game over")
    break
  while travel_type=="pegasus" and (pegasus_hp_test)<=0:
      print("Pegasus does not have enough HP.")
      travel_type=input("How do you want to travel?(Foot/Pegasus)")
      travel_type=travel_type.lower()
  while travel_type not in travel_types:
    print("Invalid input")
    travel_type=input("How do you want to travel?(Foot/Pegasus)​")
    travel_type=travel_type.lower()
    while travel_type=="pegasus" and (pegasus_hp_test)<=0:
      print("Pegasus does not have enough HP.")
      travel_type=input("How do you want to travel?(Foot/Pegasus)")
      travel_type=travel_type.lower()
  while travel_type=="foot" and selected_mission_requirements[1]==-1:
    print("You cannot go there by foot.")
    travel_type=input("How do you want to travel?(Foot/Pegasus)​")
    travel_type=travel_type.lower()
    while travel_type not in travel_types:
      print("Invalid input")
      travel_type=input("How do you want to travel?(Foot/Pegasus)​")
      travel_type=travel_type.lower()
  #here, we calculate how much time will pass and how much hp of hero or pegasus's gone  #when the mission is achieved
  if travel_type=="foot" and selected_mission_requirements[1]!=-1:
    hour=int(selected_mission_requirements[1]/foot) 
    hero_hp=hero_hp-hour*hero_hp_loss_for_hour-selected_mission_requirements[3]
  if travel_type=="pegasus":
    hour=int(selected_mission_requirements[2]/pegasus)
    hero_hp=hero_hp-selected_mission_requirements[3]
    pegasus_hp=pegasus_hp- hour*pegasus_hp_loss_for_hour
  hour_total+=hour  
  print("Hero defeated the monster")
  print("Time passed :",hour_total,"hour","\n" )  
  travel_type=input("How do you get back to home?")
  travel_type=travel_type.lower()
  #checking if we can return home with pegasus
  hour_pegasus = selected_mission_requirements[2]/pegasus
  pegasus_hp_test = pegasus_hp - hour_pegasus * pegasus_hp_loss_for_hour
  hero_hp_test_pegasus = hero_hp - hour_pegasus * hero_hp_loss_for_hour - selected_mission_requirements[3]

  #checking if we can return home on foot 
  hour_foot = selected_mission_requirements[1]/foot
  hero_hp_test_foot = hero_hp - hour_foot * hero_hp_loss_for_hour - selected_mission_requirements[3]
  
  #we check if hero's and pegasus's hp will be enough for the returning home or not 
  if hero_hp_test_pegasus <= 0 and hero_hp_test_foot <= 0:
    print("Game over")
    break    
  elif pegasus_hp_test<=0 and selected_mission_requirements[1]==-1:
    print("Game over")
    break
  while travel_type=="pegasus" and (pegasus_hp_test)<=0:
      print("Pegasus does not have enough HP.")
      travel_type=input("How do you want to travel?(Foot/Pegasus)")
      travel_type=travel_type.lower()
  while travel_type not in travel_types:
    print("Invalid input")
    travel_type=input("How do you want to travel?(Foot/Pegasus)​")
    travel_type=travel_type.lower()
    while travel_type=="pegasus" and (pegasus_hp_test)<=0:
      print("Pegasus does not have enough HP.")
      travel_type=input("How do you want to travel?(Foot/Pegasus)")
      travel_type=travel_type.lower()
  while travel_type=="foot" and selected_mission_requirements[1]==-1:
    print("You cannot go there by foot.")
    travel_type=input("How do you want to travel?(Foot/Pegasus)​")
    travel_type=travel_type.lower()
    while travel_type not in travel_types:
      print("Invalid input")
      travel_type=input("How do you want to travel?(Foot/Pegasus)​")
      travel_type=travel_type.lower()
  #here, we calculate how much time will pass and how much hp of hero or pegasus's gone #when hero arrives home  
  if travel_type=="foot" and selected_mission_requirements[1]!=-1:
    hour=int(selected_mission_requirements[1]/foot) 
    hero_hp=hero_hp-hour*hero_hp_loss_for_hour
  if travel_type=="pegasus":
    hour=int(selected_mission_requirements[2]/pegasus)
    pegasus_hp=pegasus_hp- hour*pegasus_hp_loss_for_hour
  hour_total+=hour   
  print("Hero arrived home")
  print("Time passed :",hour_total,"hour","\n")
  #in here, we remove the task that hero completed recursively
  length=len(task_list) 
  def remove_task(length_task_list,task_list_):
    if task_list_==[]:
      return []
    elif task_list_[length_task_list-1]==selected_mission_requirements:
      return remove_task(length_task_list-1,task_list_[:-1]) 
    else:
      return remove_task(length_task_list-1,task_list_[:-1]) + [task_list_[length_task_list-1]]
  task_list=remove_task(length,task_list)

if task_list==[]:
  print("Congratulations, you have completed the task.")
  hall_of_fame=open('hall_of_fame.txt','a')
  name=input("What is your name : ")
  hall_of_fame.write(str(hour_total))
  hall_of_fame.write(":")
  hall_of_fame.write(name)
  hall_of_fame.write("\n")
  hall_of_fame.close()
  hall_of_fame_read=open('hall_of_fame.txt','r')
  line_counter=0
  heroes_and_hours=dict()
  for line in hall_of_fame_read.readlines():
    hour_of_hero=line[:line.index(":")]
    name_of_hero=line[line.index(":")+1:line.index("\n")]
    heroes_and_hours[name_of_hero]=hour_of_hero

  #we sort hours here 
  sorted_heroes_and_hours = sorted(heroes_and_hours.values()) 
  sorted_hours = {}
  for i in sorted_heroes_and_hours:
      for n in heroes_and_hours.keys():
          if heroes_and_hours[n] == i:
            sorted_hours[n] = heroes_and_hours[n]
            heroes_and_hours.pop(n)
            break
  #and here
  hall_of_fame=list()
  counter=0
  for i in sorted_hours.keys():
    hall_of_fame.append(i)
    counter+=1
    if counter==3:
      break
  print("Hall of Fame\n","Name           ","Finish time")
  for i in hall_of_fame:
    print(i,"               ",sorted_hours[i],"\n")