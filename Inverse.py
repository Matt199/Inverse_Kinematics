


import math 

# Defining the model value 

# Defining the model value 

Sb = 567.0		# Base equilateral triangle side 

Sp = 76.0			#Platform equilateral triangle side 

L = 524.0			#Upper legs length

l = 1244.0		#Lower legs parallelogram length 

h = 131.0			#lower legs parallelogram width 

Wb = 164.0		#planar distance from {0} to near base side

Ub = 327.0		#planar distance from {0} to a base vertex

Wp = 22.0			#planar distance from {P} to near platform side

Up = 44.0			#planar distance from {P} to a platform vertex

# Where: 

a = Wb - Up

b = Sp/2.0 - (math.sqrt(3) / 2.0) * Wb

c = Wp - (1.0/2.0) * Wb 

print "Podaj wartosci wsp:"
x1 = raw_input("wartosc X1 ")
y1 = raw_input("wartosc Y1 ")
z1 = raw_input("wartosc Z1 ")

x1 = float(x1)
y1 = float(y1)
z1 = float(z1)


# Equation Ei * cos(xi) + Fi * sin(xi) + Gi where: i = {1,2,3}


def inverse_kinematic(x0, y0, z0):
	
	E1 = 2.0 * L * (y0 + a)
	F1 = 2.0 * z0 * L
	G1 = math.pow(x0,2) + math.pow(y0,2) + math.pow(z0,2) + math.pow(a,2) + math.pow(L,2) + 2.0 * y0 * a - math.pow(l,2)
	
	E2 = -L * (math.sqrt(3) * (x0 + b) + y0 + c)
	F2 = 2.0 * z0 * L
	G2 = math.pow(x0,2) + math.pow(y0,2) + math.pow(z0,2) + math.pow(b,2) + math.pow(c,2) + math.pow(L,2) + 2 * (x0 * b + y0 * c) - math.pow(l,2)
	
	E3 = L * (math.sqrt(3) * (x0 - b) - y0 - c)
	F3 = 2.0 * z0 * L
	G3 = math.pow(x0,2) + math.pow(y0,2) + math.pow(z0,2) + math.pow(b,2) + math.pow(c,2) + math.pow(L,2) + 2.0 * (-x0 * b + y0 * c) - math.pow(l,2)
	
	
	st1 = abs(math.pow(E1,2) + math.pow(F1,2) - math.pow(G1,2))
	st2 = abs(math.pow(E2,2) + math.pow(F2,2) - math.pow(G2,2))
	st3 = abs(math.pow(E3,2) + math.pow(F3,2) - math.pow(G3,2))
	
	
	t11 = (-F1 + math.sqrt(st1)) / (G1 - E1)
	t12 = (-F1 - math.sqrt(st1)) / (G1 - E1)
	
	t21 = (-F2 + math.sqrt(st2)) / (G2 - E2)
	t22 = (-F2 - math.sqrt(st2)) / (G2 - E2)
	
	t31 = (-F3 + math.sqrt(st3)) / (G3 - E3)
	t32 = (-F3 - math.sqrt(st3)) / (G3 - E3)
	
	thetha11 = math.degrees(2*math.atan(t11))
	thetha12 = math.degrees(2*math.atan(t12))
	thetha21 = math.degrees(2*math.atan(t21))
	thetha22 = math.degrees(2*math.atan(t22))
	thetha31 = math.degrees(2*math.atan(t31))
	thetha32 = math.degrees(2*math.atan(t32))
	
	
	return[thetha11, thetha12, thetha21, thetha22, thetha31, thetha32]
	
	
print inverse_kinematic(x1, y1, z1)
	
	
	
	
	