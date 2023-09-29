try:
    arr = [1]
    l_3 = arr[3]
    result = 10 / 2
except ZeroDivisionError as e:
    print("Specific Error:Number cannot be divided by zero.")
except Exception as e:
    print("Catches all Errors", e)
else:
    print("Only runs if there is no error in try block.")
finally:
    print("Runs Every time Whether error occurs or not.")
