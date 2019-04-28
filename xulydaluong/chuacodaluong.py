import time
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
    binh_phuong(5)
    lap_phuong(5)
    print('Thực hiện trong: ', time.time()-t)