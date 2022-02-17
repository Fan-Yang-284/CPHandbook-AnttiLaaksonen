#compress strings in binary digits
from collections import Counter
class Node:
    def __init__(self,val,letter,left=None,right=None):
        self.val = val
        self.letter = letter
        self.left = left
        self.right = right

def encode(str):
    def printTree(node, level=0):
        if node != None:
            printTree(node.left, level + 1)
            print(' ' * 4 * level + '->', node.val)
            printTree(node.right, level + 1)

    counter = Counter(str)

    counts = sorted(list(counter),key = lambda x:counter[x])

    #print(counts)

    if len(counts)>=2:
        l = Node(counter[counts[0]],counts[0])
        r = Node(counter[counts[1]],counts[1])
        head = Node(l.val+r.val,None,l,r)
        counts = counts[2:]

        while counts:
            curr = counts.pop(0)
            l = Node(counter[curr],curr)
            temp = head
            head = Node(temp.val+l.val,None,l,temp)

    #printTree(head)

    coded = ""

    memo = {}

    for s in str:
        if s in memo:
            coded+=memo[s]
            continue

        copy = head
        compressed = ""
        while copy!=None:
            if copy.left and copy.left.letter == s:
                compressed+="0"
                memo[s] = compressed
                break
            elif copy.right:
                copy = copy.right
                compressed+="1"
            else:
                break
        coded+=compressed

    return coded

def decode(str):
    res = ""
    i = 0
    while i<len(str):
        s = str[i]
        if s == "0":
            res+="A"
        else:
            if len(str[i:]) < 3:
                res+="C"
                i+=1
            else:
                substr = str[i:i+3]
                if substr == "111":
                    res+="D"
                    i+=2
                elif substr == "110":
                    res+="B"
                    i+=2
                else:
                    res+="C"
                    i+=1
        i+=1
    return res

print(encode("AABACDACA"))
print(decode("001100101110100"))