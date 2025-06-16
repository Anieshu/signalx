with open("D:\TeamOctane\\Para2.txt") as file:
    
    for line in file:
        wording = " "
        clean_line = line.strip()
        #print(clean_line)
        words = clean_line.split()
        for word in words:
            print(word)
            clean_word = word.strip(".,!?;:-()[]{}\"'")
            if clean_word.lower() == clean_word[::-1].lower():
                print("It's palindrome")
            else:
                print("It's not a palindrome")
        print(" ")