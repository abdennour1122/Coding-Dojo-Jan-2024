# 1. TASK: print "Hello World"
print( "hello world" )
# 2. print "Hello Noelle!" with the name in a variable
name = "abdennour"
print( f"hello " +  name)	# with a comma
print( "hello " + "abdennour" )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print( f"hello " +  str(42) )	# with a comma
print("hello"  + "42")	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( f"i love to eat " +  fave_food1 +"and"+ fave_food2 ) # with .format()
print( "i love to eat " +  "suchi and pizza" ) # with an f string
