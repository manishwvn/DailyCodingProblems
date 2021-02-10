import time

def f():
	pass
	
def job_scheduler(n):
	time.sleep(n/1000)
	f()
	
	
job_scheduler(1000)
