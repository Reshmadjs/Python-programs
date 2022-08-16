import multiprocessing
result=[]
def square_no(list):
	global result
	for i in list:
		result.append(i*i)
		
	print("result:{}".format(result))	

  	
if __name__ == '__main__':
	list=[2,7,3]
	p1=multiprocessing.Process(target=square_no,args=(list,))
	p1.start()
	p1.join()
	print("result in main is {}".format(result))
  				 			

	
