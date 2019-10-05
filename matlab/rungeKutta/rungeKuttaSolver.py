class RungeKutta4:
	"""
	RungeKutta4(x:number, y1:number, y2:number, y3:number)
		A class to solve third order diff equation uing rungeKutta 4th order
	
	x -> type:number
		this is the initial condition of the independent variable of the ODE

	y1 -> type:number
		this is the initial condition of base function f

	y2 -> type:number
		this is the initial condition of the differential of the function f, f_prime

	y3 -> type:number
		this is the initial condition of the second differential of the function f, f_prime_prime
	"""
	def __init__(self, x, y1, y2, y3, h):
		self.h = h
		self.x = x
		self.y1, self.y2, self.y3 = y1, y2, y3

	def __repr__(self):
		x = self.x if self.x - self.h < 0 else self.x - self.h
		return 'x = {:<.4f}, y1 = {:<.4f}, y2 = {:<.4f}, y3 = {:<.4f}'.format(x, self.y1, self.y2, self.y3)

	def getK(self, x, y1, y2, y3):
		"""
		getK(x:number, y1:number, y2:number, y3:number)
			solves for the Ks in the rungekutta method
		"""
		return self.f1(x, y1, y2, y3), self.f2(x, y1, y2, y3), self.f3(x, y1, y2, y3)

	def f1(self, x, y1, y2, y3):
		"""
		getK(x:number, y1:number, y2:number, y3:number)
			solves the first order ODE function
		"""
		return self.h * y2

	def f2(self, x, y1, y2, y3):
		"""
		getK(x:number, y1:number, y2:number, y3:number)
			solves the second order ODE function
		"""
		return self.h * y3

	def f3(self, x, y1, y2, y3):
		"""
		f3(x:number, y1:number, y2:number, y3:number)
			solves the third order ODE function
		"""
		return -.5 * self.h * y1 * y3

	def getSolution(self):
		"""
		getSolution()
			returns the final solution of the ODE using the rungekutta method
		"""
		if self.x == 0:
			self.x += self.h
			return self.x, self.y1, self.y2, self.y3

		# the old solutions
		x, y1, y2, y3 = self.x-self.h, self.y1, self.y2, self.y3

		# the ks
		k1 = self.getK(x, y1, y2, y3)
		k2 = self.getK(x+self.h/2, y1+k1[0]/2, y2+k1[1]/2, y3+k1[2]/2)
		k3 = self.getK(x+self.h/2, y1+k2[0]/2, y2+k2[1]/2, y3+k2[2]/2)
		k4 = self.getK(x+self.h, y1+k3[0], y2+k3[1], y3+k3[2])
		
		li = [y1, y2, y3]
		for i in range(3):
			li[i] += ((k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) / 6)

		# the new solutions
		self.y1, self.y2, self.y3 = li

		# the new step
		self.x += self.h
		x = self.x if self.x - self.h < 0 else self.x - self.h

		return x, self.y1, self.y2, self.y3

def fileWriter(filepath, contents):
	with open(filepath, 'w') as f:
		f.write(contents)

def main():
	# initial variable
	step = 0.2

	# set the initial conditions
	eta, f, f_prime, f_prime_prime = 0, 0, 0, 0.33206

	# the instance of the rk object for solving
	rungeKuttaSolver = RungeKutta4(eta, f, f_prime, f_prime_prime, step)

	# holds all the solutons
	solution_table = "{:<6s}  {:<6s}  {:<6s} {:<6s}\n".format("Eta", "F", "F_prime", "F_prime_prime")

	for i in range(50):
		# gets new solution after a step
		x, y1, y2, y3 = rungeKuttaSolver.getSolution()

		# shows the current solution
		print(rungeKuttaSolver)

		# the solution  table
		solution_table += "{:.4f}  {:.4f}  {:<0.4f}  {:.4f}\n".format(x, y1, y2, y3)

	# write the soluitons to a file
	fileWriter('rVelocityOutput.txt', solution_table)

if __name__ == '__main__':
	main()