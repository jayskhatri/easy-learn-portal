import wikipedia

# user_input = str(input('Enter the user query: '))
# no_sent = int(input('Enter the number of sentences: '))

# page = wikipedia.page(user_input)
# #print page.content.encode('utf-8')
# summary = wikipedia.summary(user_input, sentences = no_sent).encode('utf-8')

# print(summary)

def star(topic):
    summary = wikipedia.summary(topic, sentences = 50).encode('utf-8')
    return summary