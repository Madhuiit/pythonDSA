import time
def pseudo_random(seed=1) -> int:
    seed =(seed*9303 + 49297)%233280
    return seed/233280.0
print(int(pseudo_random(int(time.time()))*10))