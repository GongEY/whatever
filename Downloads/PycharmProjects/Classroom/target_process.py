import sys
import time

if __name__ == "__main__":
    print('{} process...'.format(sys.argv[1])) #n번째 프로세스인지 표시
    time.sleep(5)
    print('Hello {} subprocess'.format(sys.argv[1])) #목표메시지 출력