import sys

#get N from stdin, and format it properly
for line in sys.stdin:
    input_num = line.split()
    curr_num = int(input_num[0])
    N_val = str(curr_num)
    N_val = N_val.rstrip('\n')
    if (N_val == '0'):
        print ""
    else:
        #calculate sum of numbers in N
        get_sum = []
        for i in range(0, len(N_val)):
            get_sum.append(int(N_val[i]))
        N_num = int(N_val)
        N_sum = sum(get_sum)

        cont = True
        #find p value
        #only accept p values larger than 10
        p_num = 10
        Np_sum = 0
        cont = True
        while (cont == True):
            p_num += 1
            #check if sum of digits in N*p is the same as in N
            Np_num = N_num * p_num
            Np_val = str(Np_num)
            get_Np_sum = []
            for i in range(0, len(Np_val)):
                get_Np_sum.append(int(Np_val[i]))
            Np_sum = sum(get_Np_sum)
            if (N_sum == Np_sum):
                cont = False
        print p_num


