def main():

    while True:
        name = (input("Which Sanrio charater are you? Please enter your name! "))
        if name[0].isalpha() == 1:
            print("Welcome " + name +"! Let's Begin.")
            break
        else:
            print("!!Invaild input!! \nplease enter your name")

        

    #sanrioChar = ["Hello Kitty","My Melody","Kuromi","Cinnamorll","PompomPurin"]
    qOne = " \n A) Cheerful B) Grumpy C) Sleepy D) Sweet"
    qTwo = "\n A) Red apples B) Meat C) Cinnamon rolls D) pudding"
    answers =[]

    while True:
        question_One = (input("How would your friends describe you? " + qOne + " "))
        if question_One.find("A, B, C, D") != 0:
            answers.append(question_One)
            print(question_One)
            break
        else:
            print("Invaild input \npick A, B, C, or D")

    while True:
        question_Two = (input("Which food would you enjoy the most?" + qTwo +" "))
        if question_Two.find("A, B, C, D") != 0:
            answers.append(question_Two)
            print(question_Two)
            break
        else:
            print("Invaild input \npick A, B, C, or D")
   
    if "A" and "B" in answers:
        print("Hello Kitty")

    
        


if __name__ == '__main__':
    main()