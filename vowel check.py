def vowelcheck():
    word=input("enter a word:")
    vowels="aeiouAEIOU"
    flag=0
    for ch in word:
        if ch in vowels:
            print(ch)
            flag=1
    if flag==0:        
       print("no vowels in given word")        
