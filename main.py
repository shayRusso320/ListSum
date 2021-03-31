def recv_numbers():
  lst = list()
  print("enter value")
  user_input = input()

  while user_input != "stop":
    lst.append(ord(user_input) - ord('0'))
    print("enter value")
    user_input = input()

  return lst

lst = recv_numbers()
print("sum = " + str(sum(lst)))
