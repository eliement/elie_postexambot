print("Title of program: post exam bot")
print()
while True:
  description = input("Could you describe how you feel?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("keep smiling, happiness is the key to a blissful life ")
      counter += 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("im bored too haha, well i guess you could find something fun to do that you find joy in!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("go sleep because sleep is what gives us energy to have fun in the day!")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! I hope you feel better :)"

  print()
  print(output)
  print()
