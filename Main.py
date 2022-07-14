from googletrans import Translator

translate = Translator()
text = str(input("Please enter the text you want to convert : "))
detectedLang = (translate.detect(text))
lang: str = "en"
if detectedLang.lang == "hi":
    detectedLang = "Hindi"
elif detectedLang.lang == "bn":
    detectedLang = "Bengali"
elif detectedLang.lang == "mr":
    detectedLang = "Marathi"
elif detectedLang.lang == "mr":
    detectedLang = "Marathi"
elif detectedLang.lang == "te":
    detectedLang = "Telugu"
elif detectedLang.lang == "ta":
    detectedLang = "Tamil"
elif detectedLang.lang == "ur":
    detectedLang = "Urdu"
elif detectedLang.lang == "gu":
    detectedLang = "Gujarati"
print("\nThe Langauge That you entered is ", detectedLang)
print("Do you want to translate other language rather than english types yes")
choice = str(input())
if choice == "yes" or choice == "Yes" or choice == "YES":
    print('\n Please Enter the langauge you want to translate')
    print(
        "For Hindi type hi\nFor english type en \nFor Urdu type ur \nFor Tamil type ta\nFor Telugu type te\nFor "
        "Matathi "
        "type mr\nFor gangling type bn")
    lang = str(input())
out = translate.translate(text, dest=lang)
detectedLang = out.dest
if detectedLang == "hi":
    detectedLang = "Hindi"
elif detectedLang == "bn":
    detectedLang = "Bengali"
elif detectedLang == "mr":
    detectedLang = "Marathi"
elif detectedLang == "mr":
    detectedLang = "Marathi"
elif detectedLang == "te":
    detectedLang = "Telugu"
elif detectedLang == "ta":
    detectedLang = "Tamil"
elif detectedLang == "ur":
    detectedLang = "Urdu"
elif detectedLang == "gu":
    detectedLang = "Gujarati"
elif detectedLang == "en":
    detectedLang = "English"
print("Your Text in ", detectedLang, "is")
print("\nThe Translation is ", out.text)
