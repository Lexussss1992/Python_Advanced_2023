from collections import deque

eggs = deque([int(i) for i in input().split(', ')])
papers = deque([int(i) for i in input().split(', ')])
box_filled = 0

while eggs and papers:
    first_egg = eggs.popleft()
    last_paper = papers.pop()
    size = first_egg + last_paper

    if first_egg <= 0:
        papers.append(last_paper)
        continue

    if first_egg == 13:
        first_paper = papers.popleft()
        papers.append(first_paper)
        papers.appendleft(last_paper)
        continue

    if size <= 50:
        box_filled += 1

if box_filled >= 1:
    print(f'Great! You filled {box_filled} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: ', end='')
    print(*eggs, sep=', ')

if papers:
    print(f'Pieces of paper left: ', end='')
    print(*papers, sep=', ')



# 20, 13, -7, 7
# 10, 5, 20, 15, 7, 9

# 2, 4, 7, 8, 0
# 5, 6, 2

# 12, 23
# 28, 40