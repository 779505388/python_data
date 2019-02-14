import time
def coreLoop():
    limit = 10**8
    while limit>0:
        limit-= 1
def otherLoop1():
    time.sleep(0.2)
def otherLoop2():
    time.sleep(0.4)
    
def main():
    start_time =time.localtime()
    print('程序开始时间：',time.strftime('%Y-%m-%d %H:%M:%S',start_time))
    start_perf_count = time.perf_counter()
    otherLoop1()
    otherLoop1_pref_count=time.perf_counter()
    otherLoop1_pref= otherLoop1_pref_count-start_perf_count
    coreLoop()
    coreLoop_preef_count=time.perf_counter()
    coreLoop_pref=coreLoop_preef_count-otherLoop1_pref_count
    otherLoop2()
    otherLoop2_pref_count=time.perf_counter()
    otherLoop2_pref= otherLoop2_pref_count -coreLoop_preef_count
    end_pref_count=time.perf_counter()
    end_pref =end_pref_count-start_perf_count
    end_time=time.localtime()
    print(otherLoop1_pref,otherLoop2_pref,coreLoop_pref,end_pref)
    print('程序结束时间：',time.strftime('%Y-%m-%d %H:%M:%S',end_time))
main()