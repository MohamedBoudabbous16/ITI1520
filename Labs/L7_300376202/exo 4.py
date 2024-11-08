#Mohamed Boudabbous
#300376202
#exo4
def move_zeros_v1(x):
    
    global y
    y=[]
    for i in range (len(x)-1):
        if x[i]!= 0:
            y.append(x[i])
    for i in range (len(x)-1):
        if x[i]==0:
            y.append(x[i])
    return y


# move_zeros_v2 
def move_zeros_v2(x):
  n_z = []
  for i in x:
    if i != 0:
      n_z.append(i)

  for i in range(len(x)):
    if x[i] == 0:
      n_z.append(x[i])
     
  x[:] = n_z
    


# move_zeros_v3
def move_zeros_v3(x):
  m= 0
  for i in range(len(x)):
    if x[i] != 0:
      x[m], x[i] = x[i], x[m]
      m += 1
#Programme principal
#fonction 1
x = [1, 0, 3, 0, 0, 5, 7]
y=move_zeros_v1(x)
print(x, y)
#fonction 2
x = [1, 0, 3, 0, 0, 5, 7]
z=move_zeros_v2(x)
print(x,z)
#fonction 3
x = [1, 0, 3, 0, 0, 5, 7]
t=move_zeros_v3(x)
print(x, t)
