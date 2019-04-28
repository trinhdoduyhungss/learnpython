import time
from threading import Thread, active_count
def binh_phuong(n):
    for i in range(n+1):
        time.sleep(0.2)
        print('Bình phương: %s'%(i*i))
def lap_phuong(n):
    for y in range(n+1):
        time.sleep(0.2)
        print('Lập phương: %s'%(y*y*y))
if __name__=='__main__':
    t = time.time()
    thread_a = Thread(target=binh_phuong, args=(5,))
    thread_b = Thread(target=lap_phuong, args=(5,))
    thread_a.start()
    thread_b.start()
    thread_a.join()
    thread_b.join()
    print('Thực hiện trong: ', time.time()-t)
    print('Số luồng thực hiện: ', active_count()) # Vì 2 thread trên đã chạy xong nên nó chỉ trả về 1 , 1 chính là thread main đang chạy ( console )