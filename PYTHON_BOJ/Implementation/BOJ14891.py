from copy import copy
import sys

first = list(sys.stdin.readline().rstrip())
second = list(sys.stdin.readline().rstrip())
third = list(sys.stdin.readline().rstrip())
fourth = list(sys.stdin.readline().rstrip())

K = int(sys.stdin.readline().rstrip())

def rotation_colock(gear):
    tmp = copy(gear)
    gear[0] = tmp[-1]
    gear[1] = tmp[0]
    gear[2] = tmp[1]
    gear[3] = tmp[2]
    gear[4] = tmp[3]
    gear[5] = tmp[4]
    gear[6] = tmp[5]
    gear[7] = tmp[6]

def rotation_not_colock(gear):
    tmp = copy(gear)
    gear[0] = tmp[1]
    gear[1] = tmp[2]
    gear[2] = tmp[3]
    gear[3] = tmp[4]
    gear[4] = tmp[5]
    gear[5] = tmp[6]
    gear[6] = tmp[7]
    gear[7] = tmp[0]
    

#맞닿아있는 부분의 idx는 오른쪽 2,왼쪽이 6이다.
for _ in range(K):
    num,direction = map(int,sys.stdin.readline().rstrip().split())
    
    check_first = False
    check_second = False
    check_third = False
    check_fourth = False

    if num == 1:
        check_first = True
        if first[2] != second[6]:
            check_second = True
            if second[2] != third[6]:
                check_third = True
                if third[2] != fourth[6]:
                    check_fourth = True
        
        if direction == 1:
            rotation_colock(first)
            if check_second:
                rotation_not_colock(second)
                if check_third:
                    rotation_colock(third)
                    if check_fourth:
                        rotation_not_colock(fourth)
        
        if direction == -1:
            rotation_not_colock(first)
            if check_second:
                rotation_colock(second)
                if check_third:
                    rotation_not_colock(third)
                    if check_fourth:
                        rotation_colock(fourth)

    if num == 2:
        
        check_second = True
        if first[2] != second[6]:
            check_first = True
        if second[2] != third[6]:
            check_third = True
            if third[2] != fourth[6]:
                check_fourth = True
        
        if direction == 1:
            if check_first:
                rotation_not_colock(first)
            if check_second:
                rotation_colock(second)
                if check_third:
                    rotation_not_colock(third)
                    if check_fourth:
                        rotation_colock(fourth)
        
        if direction == -1:
            if check_first:
                rotation_colock(first)
            if check_second:
                rotation_not_colock(second)
                if check_third:
                    rotation_colock(third)
                    if check_fourth:
                        rotation_not_colock(fourth)

    if num == 3:
        check_third = True
        if second[2] != third[6]:
            check_second = True
            if first[2] != second[6]:
                check_first = True
        if third[2] != fourth[6]:
            check_fourth = True
        
        if direction == 1:
            if check_second:
                rotation_not_colock(second)
                if check_first:
                    rotation_colock(first)
            if check_third:
                rotation_colock(third)
                if check_fourth:
                    rotation_not_colock(fourth)
        
        if direction == -1:
            if check_second:
                rotation_colock(second)
                if check_first:
                    rotation_not_colock(first)
            if check_third:
                rotation_not_colock(third)
                if check_fourth:
                    rotation_colock(fourth)

    if num == 4:
        check_fourth  = True
        if third[2] != fourth[6]:
            check_third  = True
            if second[2] != third[6]:
                check_second = True
                if first[2] != second[6]:
                    check_first = True
        
        if direction == 1:
            rotation_colock(fourth)
            if check_third:
                rotation_not_colock(third)
                if check_second:
                    rotation_colock(second)
                    if check_first:
                        rotation_not_colock(first)
        
        if direction == -1:
            rotation_not_colock(fourth)
            if check_third:
                rotation_colock(third)
                if check_second:
                    rotation_not_colock(second)
                    if check_first:
                        rotation_colock(first)
answer = 0
if first[0] == "1":
    answer += 1
if second[0] == "1":
    answer += 2
if third[0] == "1":
    answer += 4
if fourth[0] == "1":
    answer += 8

print(answer)