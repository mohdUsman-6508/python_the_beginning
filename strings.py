course_name="beginner's course of Python"

# multiline string ''' i am multiline string '''
course_description='''This is the one stop solution for
the beginner who want to become
master in the "python"'''
print(course_name)
print(course_description)
# square bracket format [0:] [1:5] [1:-2]
# array in python has negative index also

name="machine learning"
t_name=name
print(name[1:-1])  #achine learnin  exclude first and last character
#######################################################################################

# formatted string f'this is {i}'
name='osman'
power='programming and more hidden powers'
superhero=f'{name} have powers of {power}'
print(superhero)

########################################################################################

# methods--> these are the function specific to something e.g. String methods like find upper lower etc.
name1='osman'
print(name1.upper())
print(name1.capitalize())
print(name1.title())
print(name1.find('m'))
print('man' in name1)
print(name1.replace('o','u'))