'''import libraries'''
import schedule
import time

'''print the working progress'''
def job():
    print("I'm working...")

'''time sheduling'''
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("15:05").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

'''run the sheduled items'''
while True:
    schedule.run_pending()
    time.sleep(1)
