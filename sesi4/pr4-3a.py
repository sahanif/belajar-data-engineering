def fungsi (input1, input2, operasi):
    if operasi =='plus1' :
        series = [i for i in range (input1,input2+1)]

    elif operasi =='kuadrat':
        #series = [input1**i for i in range (input1, input2+1)]
        n1 = input1
        series = []
        for i in range (input1, input2+1):
            series.append(n1)
            n1 = input1**i
            if n1 > input2:
                break

    elif operasi =='fibonaci':
        count =0
        n1 = input1
        n2 = input1+1
        series =[]
        #while count < input2:
        for count in range (input2):
            series.append(n1)
            bilangan_akhir = n1+n2
            n1=n2
            n2 = bilangan_akhir
            if n1 > input2:
                break
            count +=1

    return series


hasil_plus1 = fungsi (2,10,'plus1')
hasil_kuadrat = fungsi (2,10,'kuadrat')
hasil_fibonaci = fungsi (2,10,'fibonaci')

print (hasil_plus1)
print (hasil_kuadrat)
print (hasil_fibonaci)




