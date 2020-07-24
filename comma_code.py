def comma_code(spam):
    for i in range(len(spam) - 2):
        print(spam[i], end=', ')
    print(spam[-2] + ' and ' + spam[-1])


spams = ['apples', 'bananas', 'tofu', 'hello', 'cats']
comma_code(spams)
