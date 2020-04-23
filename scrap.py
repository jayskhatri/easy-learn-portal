import wikipedia

def get_summary(topic):
    summary = wikipedia.summary(topic, sentences = 50).encode('utf-8')
    return summary