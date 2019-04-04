import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

x=np.random.rand(100,1)
y=2+3*x+np.random.rand(100,1)


def error_compute(b,m,points):
	total_Error=0
	for i in range(0,len(points)):
		x=points[i,0]
		y=points[i,1]

		total_Error+=(y-((m*x)+b))**2
	return total_Error/float(len(points))

def gradient_man(b_cur,m_cur,points,learningRate):
	b_gradient=0
	m_gradient=0
	N=float(len(points))

	for i in range(0,len(points)):
		x=points[i,0]
		y=points[i,1]
		b_gradient+= -(2/N)*(y-((m_cur*x)+b_cur))
		m_gradient+= -(2/N)*(y-((m_cur*x)+b_cur))*x
	new_b=b_cur-(learningRate*b_gradient)
	new_m=m_cur-(learningRate*m_gradient)

	return [new_b,new_m]

def grad_descent_runner(points,start_b,start_m,learning_rate,num_iter):
	b=start_b
	m=start_m
	for i in range(num_iter):
		b,m=gradient_man(b,m,array(points),learning_rate)
	return [b,m]	

def run():
	points = genfromtxt("data.csv", delimiter=",")
    learning_rate = 0.0001
    initial_b = 0 # initial y-intercept guess
    initial_m = 0 # initial slope guess
    num_iterations = 1000
    print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points))
    print "Running..."
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print "After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points))

if __name__ == '__main__':
    run()