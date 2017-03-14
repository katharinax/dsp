[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

>> The class that implements resampling is defined as follows:  
>>   
>> ```python  
>> class DiffMeansResample(h0.DiffMeansPermute):
>>     def RunModel (self):
>>         """
>>         Goal: Use resampling to simulate test data
>>         Output: Simulated data
>>         """
>>         group1 = np.random.choice(self.pool, self.n, replace = True)
>>         group2 = np.random.choice(self.pool, self.m, replace = True)
>>         data = group1, group2
>>         return data
>> ```  
>>       
>> Pregnancy length:   
>> p-value using permutation = 0.164  
>> p-value using resampling = 0.158  
>>   
>> Birth weight:   
>> p-value using permutation < 0.001
>> p-value using resampling < 0.001  
>>   
>> There are no noticeable differences in the results by the two methods.
