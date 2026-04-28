age = int(input(f"Can you enter your Age: "))

if age < 18:
    print("You are a Child. You can't vote")
else:
    print("You are old enough to vote.")
    print("Whom do you want to vote among these.")
    print("1. Paul Kagame")
    print("2. Edouard TUYUBAHE")
    print("3. NKURUNZIZA Everest")
    president= int(input("Enter Number: "))

    if president == 1:
        print("You chose well")
    elif president == 2:
        print("You planned well the future of your country!")
    else:
        print("You are crazy man")    
