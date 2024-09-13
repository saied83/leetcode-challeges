#integer adding approach

def addBinary( a, b):
    s = ""
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
      if i >= 0:
        carry += int(a[i])
        i -= 1
      if j >= 0:
        carry += int(b[j])
        j -= 1
      s = str(carry % 2) + s
      carry //= 2

    return s
addBinary("11","1")


#manual approach
def addBinary(self, a: str, b: str) -> str:
        
        num1, num2 = [], []
        for i in a:
            num1.append(int(i))
        for i in b:
            num2.append(int(i))

        result = []
        carry = 0
        while len(num1) != 0 and len(num2) != 0:
            last = num1.pop()
            last2 = num2.pop()

            if last == 1 and last2 == 1 and carry == 0:
                result.insert(0, 0)
                carry = 1
            elif last == 1 and last2 == 1 and carry == 1:
                result.insert(0, 1)
                carry = 1
            elif last == 0 and last2 == 0 and carry == 1:
                result.insert(0, 1)
                carry = 0
            elif last == 0 and last2 == 0 and carry == 0:
                result.insert(0, 0)
                carry = 0
            elif (last == 0 and last2 == 1 and carry == 0) or (last==1 and last2 == 0 and carry == 0):
                result.insert(0, 1)
                carry = 0
            elif (last == 0 and last2 == 1 and carry == 1) or (last==1 and last2 == 0 and carry == 1):
                result.insert(0, 0)
                carry = 1

        while len(num1) != 0:
            num = num1.pop()
            if carry == 1 and num == 1:
                result.insert(0, 0)
                carry = 1
            elif carry == 1 and num == 0:
                result.insert(0, 1)
                carry = 0
            elif carry == 0 and num == 1:
                result.insert(0, 1)
                carry = 0
            elif carry == 0 and num == 0:
                result.insert(0, 0)
                carry = 0

        while len(num2) != 0:
            num = num2.pop()
            if carry == 1 and num == 1:
                result.insert(0, 0)
                carry = 1
            elif carry == 1 and num == 0:
                result.insert(0, 1)
                carry = 0
            elif carry == 0 and num == 1:
                result.insert(0, 1)
                carry = 0
            elif carry == 0 and num == 0:
                result.insert(0, 0)
                carry = 0
        if carry == 1:
            result.insert(0, 1)
        res = ''
        for i in result:
            res += str(i)
        return res