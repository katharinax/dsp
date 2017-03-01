# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both tuples and lists are ordered and iterable. Lists are mutable while tuples are immutable, which makes tuples suitable as keys in dictionaries. The elements in a tuple and a list can each be of different data types, but conventionally people use lists to hold one single data type; in this case, a list can be easily converted to a NumPy array, which can only hold one single data type. Though some people prefer tuple's immutable property, it looks like lists are more popularly used.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both lists and sets are iterable and mutable, but sets cannot hold any duplicated elements. Sets are unordered while lists are ordered (note: ordered, not sorted).

>> An example of using lists and sets:
>> ```python
>> list1 = [1, 3, 2, 2, 2]
>> list2 = [2, 4, 3, 2, 2]
>> intersec = set()
>> for e in list1:
>>     if e in list2:
>>         intersec.add(e)
>> print(intersec) # {2, 3}
>> ```

>> Set is much faster for finding an element thanks to its underlying hash table data structure, but list is faster to iterate over because it is simpler to walk down the array.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda's are anonymous functions. They are created at runtime and don't necessarily have to be assigned to a name. I think lambda's provide a quick and concise way to write out simple functions, especially for the map, filter, and reduce functions.

>> The example below compares using lambda and using a regular function to achieve the same result:

>> ```python
>> list1 = [2, 4, -5, -1, 7]
>>  
>> # use lambda
>> print(sorted(list1, key=lambda e: abs(e)))
>>        
>> # use regular function
>> def myAbs(i):
>>     return abs(i)
>> print(sorted(list1, key=myAbs))
>> ```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> Instead of explicitly listing elements, list comprehension utilizes the *for* expression to create lists. Both map/filter and list comprehension are capable of achieving the same results, but list comprehension provides concise and readable code which are often slightly faster in performance.

>> The example below compares using list comprehension and using map/filter to create the same lists:

>> ```python
>> tup = (1, "two", 2, 2, 3.4)
>> # list comprehension ex. 1
>> print([type(e) for e in tup])
>> # map() equivalent of ex. 1
>> print(list(map(type, tup)))
>> # list comprehension ex. 2
>> print([e for e in tup if type(e) == int])
>> # filter() equivalent of ex. 2
>> print(list(filter(lambda e: type(e) == int, tup)))
>> ```

>> The example below demonstrates set comprehension and dictionary comprehension:

>> ```python
>> tup = (1, "two", 2, 2, 3.4)
>> # set comprehension
>> print({type(e) for e in tup})
>> # dictionary comprehension
>> print({e * 2: type(e) for e in tup})
>> ```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days 

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)
