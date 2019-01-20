s = {
     1:'One',
     2:'Two',
     3:'Three',
     4:'Four',
     5:'Five',
     6:'Six',
     7:'Seven',
     8:'Eight',
     9:'Nine',
     10:'Ten',
     11:'eleven',
     12:'twelve',
     13:'thirteen',
     14:'fourteen',
     15:'fifteen',
     16:'sixteen',
     17:'seventeen',
     18:'eighteen',
     19:'nineteen',
     20:'twenty',
     30:'thirty',
     40:'forty',
     50:'fifty',
     60:'sixty',
     70:'seventy',
     80:'eighty',
     90:'ninety'
     }


def numbertoletter(n) :
    if n == 0 :
        return 'Zero'
    if n in s :
        n = int(n)
        return s[n].capitalize()
    n = str(n)
    if len(n) == 2 :
        n = int(n)
        return s[n//10*10].capitalize()+' '+s[n%10].capitalize()
    if len(n) == 3 :
        n = int(n)
        if n%100 == 0 :
            return s[n//100]+' ' +"Hundred"
        return s[n//100]+' '+"Hundred"+' '+numbertoletter(n%100)
    if len(n) == 4 :
        n = int(n)
        if n%1000 == 0 :
            return s[n//1000]+' '+"Thousand"
        return s[n//1000]+' '+"Thousand"+ ' '+numbertoletter(n%1000)
    if len(n) == 5 :
        n = int(n)
        if n%10000 == 0 :
            return numbertoletter(n//1000)+ ' '+"Thousand"
        return numbertoletter(n//1000)+ ' ' + "Thousand" + ' ' + numbertoletter(n%1000)
    if len(n) == 6 :
        n = int(n)
        if n%100000 == 0 :
            return s[n//100000]+' ' + "Hundred Thousand" 
        return s[n//100000]+' ' + "Hundred" + ' ' + numbertoletter(n%100000)
    if len(n) == 7 :
        n = int(n)
        if n%1000000 == 0 :
            return s[n//1000000]+' ' + "Million"
        return s[n//1000000]+' ' + "Million" + ' ' +numbertoletter(n%1000000)
    if len(n) == 8 :
        n = int(n)
        if n%10000000 == 0 :
            return numbertoletter(n//1000000)+ ' '+"Million"
        return numbertoletter(n//1000000)+ ' '+"Million" + ' ' +numbertoletter(n%1000000)
    if len(n) == 9 :
        n = int(n)
        if n%100000000 == 0 :
            return s[n//100000000]+' ' + "Hundred Million" 
        return s[n//100000000]+' ' + "Hundred" + ' ' +numbertoletter(n%100000000)
    if len(n) >= 10 and len(n) <13:
        n = int(n)
        if n%1000000000 == 0 :
            return numbertoletter(n//1000000000)+ ' '+"Billion"
        return numbertoletter(n//1000000000)+ ' '+"Billion" + ' ' + numbertoletter(n%1000000000)
    
    if len(n) >= 13 :
        n = int(n)
        if n%1000000000000 == 0 :
            return numbertoletter(n//1000000000000)+ ' '+"Trillion"
        return numbertoletter(n//1000000000000)+ ' '+"Trillion" + ' ' + numbertoletter(n%1000000000000)

    
t = int(input())
for _ in range(t) :
    n = int(input())
    print(numbertoletter(n).strip())