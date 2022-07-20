# creating message list from text file (message.txt)
with open('message.txt', 'r') as messages:
    messages = [[str(n) for n in line.split()] for line in messages] #Creating elements by splitting per line, then per word.

#creating profanity list from text file (prof.txt)
profList = [] 
profList = open("prof.txt").readlines()
profanity = [x[:-1] for x in profList]

#Checking the "messages" list for shared elements of the "profanity" list.
for i in reversed(messages):
            for j in list(profanity):
                if i.__contains__(j):
                    print("DETECTED")
                    messages.remove(i) #Removing the detected list inside the 2D list.

#Writing newly edited list to text file
processedMessage = open('processedMessage.txt', 'w')
for row in messages:
    processedMessage.write(' '.join([str(item) for item in row])) #Joining elements per list together, then writing them to text file.
    processedMessage.write('\n')