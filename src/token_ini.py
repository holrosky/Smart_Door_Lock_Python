with open('/home/pi/Smart_Door_Lock/token.txt') as token:
  lines = token.read().split()
  for line in lines:
    print(line)