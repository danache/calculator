from data import t, spri
def readNum(S, opnd):
    res = []
    i = 0
    for i in range(len(S)):
        if S[i] in'12304567890.':
            res.append(S[i])
        else:
            break
    tmp = ''
    for j in res:
        tmp += j
    opnd.append(tmp)
    return (S[i:], opnd) if i != len(S) - 1 else ([], opnd)




def orderBetween(s1, s2):
    if s1 in ('+-*/()^!?') and s2 in ('+-*/()^!?'):
        return (spri[t[s1]])[t[s2]]
    else:
        return -1


def evaluate(S):
    for item in S:
        if item not in '1234567890.+-*/^!':
            return 'INPUT ERROR'
    opnd = []
    optr = []
    optr.append('?')
    while len(optr) != 0:
        if len(S) != 0 and S[0] in '1234567890':
            (S, opnd) = readNum(S, opnd)
        else:
            if len(S) >= 2:
                if S[0] in '+-*/^' and S[1] in '+-*/^':
                    return 'FORMAT ERROR'
                if S[0] in '()' and S[1] in '()':
                    return 'FORMAT ERROR'
            if len(S) == 0:
                S += '?'
            if orderBetween(optr[len(optr) - 1], S[0]) == '<':
                optr.append(S[0])
                S = S[1:]
            elif orderBetween(optr[len(optr) - 1], S[0]) == '=':
                optr.pop()
                S = S[1:]
            elif orderBetween(optr[len(optr) - 1], S[0]) == '>':
                op = optr.pop()
                if op == '!':
                    pass
                else:
                    popnd2 = opnd.pop()
                    popnd1 = opnd.pop()
                    opnd.append(cal(op, popnd1, popnd2))

    res = opnd.pop()
    if type(res) == type(1.0):
        return  "%.10f" % (res)
    else:
        return res


def cal(op, popnd1, popnd2):
    if op != '^':
        if op == '/' and popnd2 == '0':
            return 'VALUE ERROR'
        return eval('%s%s%s' % (popnd1, op, popnd2))
    else:
        res = 1
        for i in range(int(popnd2)):
            res *= int(popnd1)
        return res

