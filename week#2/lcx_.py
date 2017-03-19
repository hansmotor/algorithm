#!/usr/bin/env python

class loop_problem(object):
	def __init__(self):
		self.arr=[2,-1,1,2,2]
	#	self.arr=[-1,2]
		self.loop_time=2
		self.length=len(self.arr)
		self.aaa(self.arr)
	def aaa(self,array):
		loop_list=[]
		a=0
		b=0
		c=0
		for i in array:
		   if i ==0:
			print "the array could not contain the 0 "
			return 0
		print 'raw_list',array
	
		next_list=self.next_address(array)
		for i in xrange(self.length):
		   b=a=next_list[i]
		   c=next_list[b]
#		   print "before while",a,b
		   loop_list=[i,a]
		   while next_list[a]!=i:
			a=next_list[a]
			loop_list.append(a)
		#	if a==b or self.loop_time==100:
			self.loop_time+=1
			if a==b or c==a:
			   break
		   if next_list[a]==i:
			loop_list.append(i)
#			loop_result='->'join(map(str))
			print "the object arr[%s]=%s need loop %s times "%(i,array[i],self.loop_time)
			print "loop_list",'->'.join(map(str,loop_list))
		   else:
			print "the object arr[%s]=%s cannot loop"%(i,array[i])
		   self.loop_time=2 

	def next_address(self,array):
		#length of the array
		next_station=[0]*self.length
		for i in xrange(self.length):
		#s is the next index of array[i]
		   s=i+array[i]
#		   print 'first-step,s',s
		#if array[i]>0.foward
		   if array[i]>0:
			if s>(self.length-1):#if s exceed the length,come back to the first of array
			   s=s-self.length
			next_station[i]=s
		#if array[i]<0,back
		   else:
			if s<0:
			   s=s+self.length
			next_station[i]=s
		print 'next_station',next_station
		return next_station
			
if __name__=="__main__":
	loop_problem()
