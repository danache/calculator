from sup import evaluate
if __name__ == '__main__':
    while True:
        s = input()
        res = ''.join(s.split())
        print(evaluate(res))
