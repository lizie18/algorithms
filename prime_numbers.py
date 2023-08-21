def number_is_prime():
  """
  The function checks if a given number is prime or not.
  :return: a boolean value. It returns True if the entered number is prime, and False if it is not
  prime.
  """
  entered_number = None
  try:
    entered_number = int(input("Enter a positive number: "))
  except:
    raise ValueError("It's not a valid number")
  else:
    if entered_number  <= 1:
      return False
    if entered_number  <= 3:
      return True
    if entered_number % 2 == 0 or entered_number % 3 == 0:
      return False
    loop_limit = 5 * 5 - 1
    for num in range(5, loop_limit, 6):
      loop_limit = num * num - 1
      if entered_number % num == 0 or entered_number % (num+2) == 0:
        return False
      return True


  
print(number_is_prime())