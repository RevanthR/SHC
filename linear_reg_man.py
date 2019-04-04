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

	



print(type(x))
