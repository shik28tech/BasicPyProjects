import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Please Drink Water",
            message = "15.5 cups for men and 12.5 cups for women",
            timeout = 10
        )
        time.sleep(10)