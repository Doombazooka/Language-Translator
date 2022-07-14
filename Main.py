from googletrans import Translator
translate = Translator()
text = str(input("Please enter the text you want to convert : "))
detectedLang=(translate.detect(text))
print("\nThe Langauge That you entred is ", detectedLang.lang)
out = translate.translate(text, dest='en')
print("\nThe Translation is ", out.text)
