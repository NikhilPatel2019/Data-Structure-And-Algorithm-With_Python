#1. Simple Class
class dog:
  print("Inside Class\n")
  pass

#2. Class
class Customer:
  """
  Class to create customer 
  """
  #Constructor👇
  def __init__(self, name, membership_type):
    self.name = name
    self.membership_type = membership_type
    print("Customer Created")

#2(A) - Creating Objects👇
c1 = Customer('Chandragupta', 'Premium')
#2(B) - Accessing Values of created Object👇
print("Customer Name: ", c1.name, "\nMembership Type: ",c1.membership_type)
print("\n")

c2 = Customer("Bindusara", "VIP")
print("Customer Name: ", c2.name, "\nMembership Type: ",c2.membership_type)

#2(C) - Another Way of creating an object👇
customers = [Customer('Ashoka', 'Premium+'),
             Customer('Shushima', 'Gold')]

for index,c in enumerate(customers):
  print("No.:", index)
  print("Customer Name:", c.name)
  print("Membership Type: ", c.membership_type)