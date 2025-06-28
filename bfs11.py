from collections import deque

def wordLadder(beginWord,endWord,wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    
    queue = deque([(beginWord,1)])

    while queue:
        word ,steps = queue.popleft()
        if word  == endWord :
            return steps
    

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                nextWord = word[:i] + c + word[i+1:]
                if nextWord in wordSet :
                    wordSet.remove(nextWord) 
                    queue.append((nextWord,steps+1))

    return 0









beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(wordLadder(beginWord,endWord,wordList))