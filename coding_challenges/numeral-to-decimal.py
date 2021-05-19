class numeralSystemsToDecimals():

    def numSysToDecimals(self, number, numSysBase):
        number = str(number)
        decimalNum = 0
        position = len(number)
        while position > 0:
            position -= 1
            decimalNum += int(number[position])*(numSysBase**position)
        return decimalNum
