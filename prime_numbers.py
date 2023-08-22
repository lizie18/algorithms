def number_is_prime(entered_number):
  """
  The function checks if a given number is prime or not.
  :return: a boolean value. It returns True if the entered number is prime, and False if it is not
  prime.
  """
  # print(type(entered_number))
  if type(entered_number) != int:
    raise ValueError("Value is not a number")

  if entered_number  == 2 or entered_number  == 3:
    return True
  if entered_number  <= 1 or entered_number % 2 == 0 or entered_number % 3 == 0:
    return False

  loop_limit = int(entered_number**(1/2)) + 1
  for num in range(5, loop_limit, 6):
    loop_limit = num * num - 1
    if entered_number % num == 0 or entered_number % (num+2) == 0:
      return False
  return True

print(number_is_prime(10**122))
