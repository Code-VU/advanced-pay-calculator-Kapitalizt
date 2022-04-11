def calculatePay():
    
    # This first line is provided for you
    hrs = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    if hrs > 40:
        pay = (40*rate)+(hrs-40)*rate*1.5
    else:
        pay = hrs*rate

    print('Pay: ' + str(pay))
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()