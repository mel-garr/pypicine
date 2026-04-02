import sys

def calculate_letter(text:str):
    UpperCount = 0
    LowerCount = 0
    PunctCount = 0
    DigitCount = 0
    SpaceCount = 0
    for i in text:
        if i.isupper():
            UpperCount += 1
        elif i.islower():
            LowerCount += 1
        elif i.isdigit():
            DigitCount += 1
        elif i.isspace():
            SpaceCount += 1
        elif i in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            PunctCount += 1
    print(f"The text countains {len(text)} characters:\n{UpperCount} uppser letters\n{LowerCount} lower letters\n{PunctCount} punctuation marks\n{SpaceCount} spaces\n{DigitCount} digits")
    

def main():
    the_text = ""
    try:
        assert len(sys.argv) <= 2, "more than one argument provided"
        if len(sys.argv) < 2:
            while not the_text:
                the_text = input("What is the text to count?\n")
            
            the_text += "\n" #thecarriage
        else:
            the_text = sys.argv[1]
        calculate_letter(the_text)

    except AssertionError as e:
          print ("AssertionError:", e)
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()