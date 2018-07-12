ori_num_bac = int(input("How many B bacterias are there?"))

num_time_wait = int(input("How much time in minutes will we wait?"))

num_time = num_time_wait//2

num_bac = ori_num_bac * (2** num_time)


print("After {0} minutes, we would have {1} bacterias".format(num_time_wait,num_bac))