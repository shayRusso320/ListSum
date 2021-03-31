def recv_numbers():
  lst = list()
  print("enter list")
  user_input = input().split(',')
  
  for item in user_input:
    lst.append(ord(item) - ord('0'))
    
  return lst

lst = recv_numbers()
print(lst)
print("sum = " + str(sum(lst)))
