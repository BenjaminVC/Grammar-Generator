#python program that reads an input file's grammar in BNF
import random

"dictionary=dict() #key/value=non-terminal/rules which are split on either side of ::="

#start program, user input selects the file that builds a grammar dictionary
def program_start():
	grammar_file=input('What is the name of the grammar file? ') 
	contents=open(grammar_file, 'r') #open grammar_file as read-only
	
	for line in contents:
		dictionary[line.split("::=", 1)[0]]=line.split("::=", 1)[1] 
		
	contents.close() #close input stream
	print()
	program_main()

#main loop of grammar generator, continues until user passes empty string to token
def program_main():
	print("Available symbols to generate are:")
	print(sorted(dictionary.keys()))
	token=input("What do you want to generate (Enter to quit)? ")
	
	if(token==""):
		exit(0) #user exited program 
	generations=int(input("How many do you want me to generate? "))
	x=0 
	final_sentence=[]
	
	while (x<generations):
		final_sentence.clear()
		final_sentence.append(grammar_gen(token))
		print(final_sentence)
		x+=1 
	program_main()

#recursively build a sentence based on passed token 
def grammar_gen(instance_token):	
	#if rule does not contain non-terminal, choose random terminal 
	if(instance_token not in dictionary.keys()):
		return instance_token #base case, passed token is terminal symbol
	result=[]
	val=list()
	val=(dictionary[instance_token].split("|")) #store current grammar rules
	val[-1]=val[-1].strip() #remove \n character from val
	random_val=random.choice(val) #pseudo-randomly select from value list 
	
	#append to result for the number of elements in the randomly selected rule
	for element in random_val.split():
		result.append(grammar_gen(element)) #recursively append 
		
	return " ".join(result) #return words, inserting whitespace between each one			
#starting point of grammargenerator.py
program_start()