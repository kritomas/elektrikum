import math

def calcResistance(U, I):
	if U < 0:
		raise ValueError("Voltage cannot be negative.")
	if I < 0:
		raise ValueError("Current cannot be negative.")
	if I == 0:
		return math.inf
	return U / I
def calcVoltage(I, R):
	if I < 0:
		raise ValueError("Current cannot be negative.")
	if R < 0:
		raise ValueError("Resistance cannot be negative.")
	return I * R
def calcCurrent(U, R):
	if U < 0:
		raise ValueError("Voltage cannot be negative.")
	if R < 0:
		raise ValueError("Resistance cannot be negative.")
	if (R == 0):
		return math.inf
	return U / R

def calcForce(q1, q2, r, relative_permitivity=1):
	return relative_permitivity*q1*q2/r**2