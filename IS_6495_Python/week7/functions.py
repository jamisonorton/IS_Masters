def yesNoBooleanConverter(val):
    val = str(val).upper()
    if val == "Y" or val == "YES":
        return True
    else:
        return False


def booleanYesNoConverter(val):
    if val:
        return "Yes"

    return "No"


def nullToBooleanConverter(value):
    return value is not None


def moveQueueValueConverter(val):
    # R, H, D, P
    val = str(val).upper()
    if val == "R":
        return "Released"
    elif val == "H":
        return "Hold"
    elif val == "D":
        return "Deleted"
    elif val == "P":
        return "Pending"
    else:
        return None


def fahrenheit_To_Celsius(val):
    celsius = (val - 32) * (5 / 9)

    return celsius


def celsius_To_Fahrenheit(val):
    fahrenheit = (val * 9 / 5) + 32

    return fahrenheit


def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very doubtful"
