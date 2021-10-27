def even_filter(list):
    returnList=[]
    for i in list:
        if (i%2==0):
            returnList.append(i);

    return returnList

print(even_filter([1, 2, 4, 5, 8, 9, 10]))

def is_prime_number(num):
    if(num<2):
        return False
    elif(num==2):
        return True
    elif(num==3):
        return True

    for i in range(2,(num//2)+1):
        if(num%i==0):
            return False

    return True

print(is_prime_number(60))
print(is_prime_number(61))


def count_vowel(input):
    result = 0;
    vowels = "aeiou"
    for i in input:
        if(i in vowels):
            result = result +1
    return result;

print(count_vowel("pythonian"))
