from threading import Thread
import time, random

def queuing_thread(inputs):
    for i in inputs:
        thr = Thread(target=computational_thread, args=[i]).start()
        threads.append(thr)

    # exit thread
    return

def sequencial_thread(inputs):
    for i in inputs:
        computational_thread(i)
        print(f'info: {i} done')
    
    return


def computational_thread(t_queue_i):
    ret = thread_artificial_load(5)

    # Submit result
    t_output.append(t_queue_i)


def declare_vars():
    # thread queue, 
    # scheduler iteration index, 
    # thread output
    global t_queue, s_iter
    global t_output, threads

    t_queue, s_iter  = 0, 0
    t_output, threads = [], []


def scheduler():
    declare_vars()

    inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    queuing_thread(inputs)
    queue_thr = Thread(target=queuing_thread, args=[inputs]).start()
    # sequencial_thread(inputs)

    s_iter = 0

    while True:
        # Guard if statment
        if s_iter > max(inputs):
            break

        computated, index = False, 0
        for i, t_o in enumerate(t_output):
            if s_iter == t_o:
                computated, index = True, i

        # Guard if statment
        if not computated:
            continue

        print(t_output[index], index)
        s_iter += 1

        





def thread_artificial_load(t_ref_sec:float):
    rand = random.random()
    time.sleep(t_ref_sec * rand)

    # return success
    return t_ref_sec * rand
