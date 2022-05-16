#========================================
#
# this module is for the validation codes only
# written by matt upton-cashmore
# last checked 9/05/22
# known bugs: none
#=============================================


# use try to write own error message for errors so it doesnt crash
# this function is for checking the length of our data
# data is what we want to chack, length is our value for our max/min length
# option is for later when decide what length im checking
def lengthCheck(data,length,option):
    if option ==1:
        if len(data) == length:
            return True
        else:
            return False
    elif option == 2:
            if len(data) >= length:
                return True
            else:
                return False

    elif option == 3:
        if len(data) <= length:
            return True

        else:
            return False






# this function checks the data is within the correct length parameters
# data is what we want to to validate, high and low are our max/min values

def rangeCheck(data,hi,low):
    if (int(len(data)) > low) and (int(len(data)) < hi):
        return True
    else:
        return False
    #return true or false



if __name__ == "__main__":
    pass



