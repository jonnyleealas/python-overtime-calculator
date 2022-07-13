def computePay(hours, rate):
    regularPay = rate * 40
    overTimeHours = hours - 40
    timeAndAHalf = rate * 1.5
    overTime = overTimeHours * timeAndAHalf
    # format is used to add 2 decimal places to our float
    overTimePay = format(float(overTime + regularPay),'.2f')
    nonOverTimePay = format(float(hours * rate), '.2f')
    if hours > 40:
        print(overTimePay)
        return '${}'.format(overTimePay)
    else:
        print(nonOverTimePay)
        return '${}'.format(nonOverTimePay)
# save our compute function for later use
compute = computePay(49.30, 10.23)
# open the file with append option 'a'
f = open('pythonTextFile.txt', 'a')
# use writelines to write to our file and convert to a string because the function only writes strings
with open('pythonTextFile.txt', 'a') as f:
    f.writelines(str(compute))
    f.write('\n')
