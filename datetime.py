import datetime
# today's date

Todays_date_and_time  = datetime.datetime.now()
print("today's date  " , Todays_date_and_time)
# formated date and time
formated_date_and_time = Todays_date_and_time.strftime("%D %M %Y  %H:%M:%S")
print("Formated date and time ",formated_date_and_time )