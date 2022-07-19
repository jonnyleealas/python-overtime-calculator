from asyncore import write


def computePay(hours, rate):
    regularPay = rate * 40
    overTimeHours = hours - 40
    timeAndAHalf = rate * 1.5
    print(timeAndAHalf, 'i am time and a half')
    overTime = overTimeHours * timeAndAHalf
    # format is used to add 2 decimal places to our float
    overTimePay = format(float(overTime + regularPay), '.2f')
    nonOverTimePay = format(float(hours * rate), '.2f')
    if hours > 40:
        print(overTimePay)
        return '${}'.format(overTimePay)
    else:
        print(nonOverTimePay)
        return '${}'.format(nonOverTimePay)

# this is a comment for alan to test gituhub
# save our compute function for later use
# compute = computePay(41, 10)
# open the file with append option 'a'
f = open('/Users/jonnylee/pythonTextFile.txt', 'a')
# use writelines to write to our file and convert to a string because the function only writes strings
with open('/Users/jonnylee/pythonTextFile.txt', 'a') as f:
    f.writelines(str(computePay(20, 10)))
    f.write('\n')
