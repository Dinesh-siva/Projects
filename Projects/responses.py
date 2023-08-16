from datetime import datetime

def sample(input_text):
    user_message = str(input_text).lower()

    if user_message in("hello","hi","hey"):
        "Hey!How its going"
    if user_message in("time","time?"):
        now = datetime.now()
        data_time = now.strftime("%d/%m/%y","%H:%M:%S")
        return str(date_time)

    return "I don't understand You."