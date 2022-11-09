#Note code is not fully finctional, at the moment the code will only accurately return numbers form 0 to 9999. 

def get_twenties(num, tens, ones):
        """
        If the second digit is zero, return the tens digit, otherwise return the tens digit and the ones
        digit.
        
        :param num: The number to be converted
        :param tens: ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        :param ones: ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        :return: the tens and ones place of the number.
        """
        n = int(num[0])
        if num[1] == "0":
                return f'{tens[n - 2]}'
        else:
                n1 = int(num[1])
                return f'{tens[n - 2]} {ones[n1]}'

def get_hundreds(num, ones, hun, tens):
        """
        If the number is less than 100, return the number in words, otherwise return the number in words
        with the word "hundred" appended to it.
        
        :param num: the number to be converted
        :param ones: a list of the words for the numbers 1-9
        :param hun: "hundred"
        :param tens: a list of the tens words
        :return: The hundreds place of the number, and the tens and ones place of the number.
        """
        nh = int(num[0])
        if num[1:] == "00":
                return f"{ones[nh] }{hun[0]}" 
        else:
                twenties = get_twenties(num[1:], tens,ones)
                return f"{ones[nh]} {hun[0]} and {twenties}"
        
def get_thousands(num, thou, ones, hun, tens):
        """
        If the number is 1000, return "one thousand". 
        
        If the number is not 1000, then call the get_hundreds function on the last three digits of the
        number, and return "one thousand, " followed by the result of that function
        
        :param num: the number to be converted
        :param thou: the word for thousand
        :param ones: a list of the words for the numbers 1-9
        :param hun: "hundred"
        :param tens: a list of the tens words
        :return: the number in words.
        """
        nh = int(num[0])
        if num[1:] == "000":
                return f"{ones[nh]} {thou[0]}" 
        else:
                hund = get_hundreds(num[1:], ones, hun, tens)
                return f"{ones[nh]} {thou[0]}, {hund}"
        
        
def number (num):
        """
        It takes a number, converts it to a string, and then uses the length of the string to determine
        which function to call. 
        
        The functions are: 
        
        get_twenties() - for numbers between 20 and 99
        
        get_hundreds() - for numbers between 100 and 999
        
        get_thousands() - for numbers between 1000 and 9999
        
        The last function is a bit more complicated because it has to handle numbers between 10000 and
        99999. 
        
        The function number() is called in the main() function.
        
        :param num: the number you want to convert to words
        :return: The number in words.
        """
    
        ones = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
             'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
            'seventeen', 'eighteen', 'nineteen']
    
        tens = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        hun = ['hundred']
        thousand = ['thousand']
        new_num = str(num)
        
        if num < 20:
            return ones[num]
    
        elif len(new_num) == 2:
                return f'{get_twenties(new_num, tens,ones)}'
        
        elif len(new_num) == 3:
                return f'{get_hundreds(new_num, ones, hun, tens)}'
               
        elif len(new_num) == 4:
                return f'{get_thousands(new_num, thousand, ones, hun, tens)}'
               
        elif len(new_num) == 5:
                nh = int(new_num[:2])
        
                if new_num[2:] == "000":
                        return f"{ones[nh]} {thousand[0]}" 
                # elif new_num[1:] == "0000":
                #         nh = int(new_num[0])
                #         return f"{tens[nh-2]} {thousand[0]}" 
                        
                else:
                        sand = get_thousands(new_num[1:], thousand, ones, hun, tens)
                        return f"{tens[nh-2]} {thousand[0]}, {sand}"
                
                



    
# Asking the user to enter a number, and then it is calling the function number() on that number.
num = int(input('Enter a number: '))

print (number(num))
    