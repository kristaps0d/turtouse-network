from threading import Thread
import time, random

def queuing_thread(inputs):
    for i in inputs:
        thr = Thread(target=computational_thread, args=[i])
        thr.run()
        threads.append(thr)


def computational_thread(t_queue_i):
    ret = thread_artificial_load(2)

    # submit result
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

    inputs = [1, 2, 3]
    queue_thr = Thread(target=queuing_thread, args=[inputs])
    queue_thr.run()

    while True:

        print(t_output)

        outputs, index = False, 0

        for i, t_o in enumerate(t_output):
            if s_iter == t_output:
                outputs, index = True, i

        if not outputs:
            continue

        print(t_output[i])






def thread_artificial_load(t_ref_sec:float):
    rand = random.random()
    time.sleep(t_ref_sec * rand)

    # return success
    return t_ref_sec * rand
