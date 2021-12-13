# Taylor Martin
# CS-210 Final Exam
# Counting Sort
# counting_sort.py
import numpy as np
from time import perf_counter

def counting_sort(list):
    """counting sort function"""
    size = len(list)
    #output and count list init
    output = [0] * size
    count = [0] * size
    #storing count of each element in
    for i in range(0,size):
        count[list[i]] +=1
    #storing the cumulative count of each element
    for i in range(0,size):
        count[i] += count[i-1]
    
    #place the elements in output list after finding the index of each element in the original
    # list in count list
    n = size - 1
    while n >= 0:
        output[count[list[n]] -1 ] = list[n]
        count[list[n]] -= 1
        n-=1
    
    for n in range(0,size):
        list[n] = output[n]
def main():
    """main"""

    #list comprehension to generate a list of 1000000 random integers ranging from 0-100
    list_comp_time_start = perf_counter()
    rand_list1 = (np.random.randint(low=0,high=100,size=1000000))
    list_comp_time_stop = perf_counter()
    list_comp_total_time = list_comp_time_stop - list_comp_time_start
    print("list_comp_time: ",list_comp_total_time, ' sec')
    #print random_list1 length and contents to make sure the generation was successful
    print('List comprehension random list: ',rand_list1)
    print('list 1 length: ',len(rand_list1))

    #for loop to generate a list of 1000000 random integers ranging from 0-100
    rand_list2 = []
    loop_gen_time_start= perf_counter()
    for _ in range(1000000):
        rand_list2.append(np.random.randint(0,100))
    loop_gen_time_stop = perf_counter()
    loop_gen_total_time = loop_gen_time_stop - loop_gen_time_start
    print('loop_gen_total_time: ',loop_gen_total_time, ' sec')
    print('Iterative for loop generation',rand_list2[0:3],'...',rand_list2[999997:1000000])
    print('list 2 length: ',len(rand_list2))

    #compare list generation results
    if(list_comp_total_time < loop_gen_total_time):
        print('list comprehension was faster by: ', loop_gen_total_time - list_comp_total_time,' sec')
    elif(loop_gen_total_time < list_comp_total_time):
        print('loop generation was faster by: ', list_comp_total_time - loop_gen_total_time,' sec')
    elif(loop_gen_total_time == list_comp_total_time):
        print('the two list generation processes were equally efficient')
    
    #sort rand_list1 and time the duration of the process 
    t1_start= perf_counter()
    rand_list1.sort()
    t1_stop= perf_counter()
    print('Built in python sort on list 1: ',rand_list1)
    t1_total_time = t1_stop - t1_start
    print('Python built in sort elapsed time:',t1_total_time, ' sec')

    #sort rand_list2 and time the duration of the process 
    t2_start= perf_counter()
    counting_sort(rand_list2)
    t2_stop= perf_counter()
    print('list 2 sorted with defined counting sort: ',rand_list2[0:3],'...',rand_list2[999997:1000000])
    t2_total_time = t2_stop - t2_start
    print('Programmed Counting Sort elapsed time:',t2_total_time, ' sec')

    #compare algorithm time results
    if(t1_total_time < t2_total_time):
        print('Python built in sort algorithm was more efficient by: ',t2_total_time-t1_total_time,' sec')
    elif(t2_total_time < t1_total_time):
        print('Programmer defined counting sort algorithm was more efficient by: ',t1_total_time-t2_total_time, ' sec')
    elif(t1_total_time == t2_total_time):
        print('The two used sorting algorithms were equally efficient')



if __name__ == '__main__':
    """run main function"""
    main()