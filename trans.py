from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate

def converthindi(data):
	answer = transliterate(data.lower(), sanscript.OPTITRANS, sanscript.DEVANAGARI)
	return answer

def convertenglish(data):
	answer = transliterate(data, sanscript.DEVANAGARI, sanscript.OPTITRANS)
	return answer.lower()
  
