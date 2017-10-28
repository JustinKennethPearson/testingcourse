def toEnglish(n):
    """ Converts a number between 0 and 999 to English """
    numbers = ['zero','one','two','three','four','five','six',
               'seven','eight','nine','ten','eleven','twelve',
               'thirteen','fourteen','fifteen','sixteen',
               'seventeen','eighteen','nineteen']
    tens = ['','','twenty','thirty','forty','fifty','sixty',
            'seventy','eighty','ninety']
    numberOfHundreds = n // 100
    numberOfTens  = n // 10
    numberOfUnits = n % 10
#We always treat the numbers 0-19 as special numbers.
    return_string = ''
    if n in range(0,20):
        return(numbers[n])
    if numberOfHundreds in range(1,10):
        return_string = return_string + numbers[numberOfHundreds] + ' hundred'
        n = n - numberOfHundreds*100
        if n>0:
            return_string = return_string + ' and ' + toEnglish(n)
        return(return_string)
    if numberOfTens in range(1,10):
        return_string = return_string + tens[numberOfTens]
        if numberOfUnits > 0 :
            return_string = return_string + ' ' + numbers[numberOfUnits]
        return(return_string)

    

