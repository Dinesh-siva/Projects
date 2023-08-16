import pywhatkit as pwk
from openpyxl import load_workbook

wb = load_workboaok('datanum.xlsx')  # Replace 'data.xlsx' with the path to your Excel file
sheet = wb.active

for row in sheet.iter_rows(min_row=1,min_col=1,max_row=6,max_col=3, values_only=True):  # Assuming the data starts from the second row
    recipient = row[0]  # Assuming the recipient's number is in the first column of the Excel sheet
    message = row[1]  # Assuming the message is in the second column of the Excel sheet

    # Format the recipient number to include the country code (e.g., +1 for the US)
    recipient = '+' + recipient

    # Send the message using pywhatkit
    pwk.sendwhatmsg_instantly(recipient, message,)

    print(f"Message sent to {recipient}: {message}")