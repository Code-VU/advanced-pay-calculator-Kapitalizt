def calculatePay():
    
    try:
        hours = int(input('Enter Hours: '))
        rate = float(input('Enter Rate: '))
    except:
        print('Error, please enter numeric input')
        quit()
        
    if hours > 40:
        extra_time = int(hours - 40) * 1.5 * 10
        gross_pay = (hours * rate) + extra_time
    else :
        gross_pay = hours * rate

    print(gross_pay)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()