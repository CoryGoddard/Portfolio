import random as rand

def gen(length):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    res = ""
    
    for i in range(length):
        res += alpha[rand.randrange(53)]
        
    return res

def score(goal, new):
    same = 0
    
    for i in range(len(goal)):
        if goal[i] == new[i]:
            same += 1
            
    return same

def main():
    goal = input("Goal: ")
    new = gen(len(goal))
    best = 0
    Score = score(goal, new)
    curr = Score / len(goal)
    index = 0
    tot = 0
    
    while curr < 1:
        if curr > best:
            print(f"\nBest: {new}\n"
                  f"Score: {Score}/{len(goal)}\n"
                  f"Time: {tot}")
            best = curr
        if index == 1000000:
            print(".",end="")
            index = 0
        new = gen(len(goal))
        Score = score(goal, new)
        curr = Score / len(goal)
        index += 1
        tot += 1
    print(f"\n{new}")
    print(tot)
main()
