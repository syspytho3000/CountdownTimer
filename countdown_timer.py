import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')  # Overwrite the previous line
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
if __name__ == "__main__":
    countdown_timer(10)  # Countdown from 10 seconds
