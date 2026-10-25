def number_pattern(n):  

    
    if not isinstance(n, int) or isinstance(n, bool):
        return "Argument must be an integer value."
        

    if n < 1:
        return "Argument must be an integer greater than 0."
        
    pattern = ""
    

    for number in range(1, n + 1):
        if number == 1:
            pattern += str(number)
        else:
            pattern += " " + str(number)
            
    
    return pattern
