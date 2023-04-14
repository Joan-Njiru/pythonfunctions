def hello(*names):
    for name in names:
        print(f"Hello {name}")

def addition(*numbers):
    answer=0
    for num in numbers:
        answer+=num

    return answer

#write a function that accepts any number of integers and returns 
#the result of multiplying all of them

def multiply(*nums):
    result=1
    for n in nums:
        result*=n

    return result
#function printing out student attributes
def student_attributes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

#default arguments
def my_country(country="Egypt"):
    print(f"Hello from {country}")




        

