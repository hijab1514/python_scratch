# for and while are two kind of loops
# Range function is used to create the lists of the numbers

for x in range(0,5):
 print("salam")

 # We can use list and range together 
 print(list(range(10,20)))

 for x in range(0,5):
 print("salam %s" %x)

 wizard_list = [ 'spider', 'lion' , 'hunger','tiger' ]
for i in wizard_list : # i represent the whole wizard_list
    print(i)

# while loop
x = 45
y = 50

while x < 50 and y < 100:
    x = x +1
    y = y+1
    print(x,y)
