#!/usr/bin/env python
# coding: utf-8

# # 2020 카카오 인턴십
# 
# ## 1. 키패드 누르기

# 스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.
# 
# 이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.맨 처음 왼손 엄지손가락은 `*` 키패드에 오른손 엄지손가락은 `#` 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.
# 
# 1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
# 2. 왼쪽 열의 3개의 숫자 `1`, `4`, `7`을 입력할 때는 왼손 엄지손가락을 사용합니다.
# 3. 오른쪽 열의 3개의 숫자 `3`, `6`, `9`를 입력할 때는 오른손 엄지손가락을 사용합니다.
# 4. 가운데 열의 4개의 숫자 `2`, `5`, `8`, `0`을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
# 
# 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.
# 
# [제한사항]
# 
# - numbers 배열의 크기는 1 이상 1,000 이하입니다.
# - numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
# - hand는 `"left"` 또는 `"right"` 입니다.
#     - `"left"`는 왼손잡이, `"right"`는 오른손잡이를 의미합니다.
# - 왼손 엄지손가락을 사용한 경우는 `L`, 오른손 엄지손가락을 사용한 경우는 `R`을 순서대로 이어붙여 문자열 형태로 return 해주세요.
# 

# In[5]:


def get_distance(hand_number, press_number):
    location = {'1':[0,0], '2':[0,1], '3':[0,2],
                '4':[1,0], '5':[1,1], '6':[1,2],
                '7':[2,0], '8':[2,1], '9':[2,2],
                '*':[3,0], '0':[3,1], '#':[3,2]}
    press_number = str(press_number)
    x_hand_number, y_hand_number = location[hand_number]
    x_press_number, y_press_number = location[press_number]
    distance = abs(x_hand_number-x_press_number) + abs(y_hand_number-y_press_number)
    return distance

def solution(numbers, hand):
    left_side = [1,4,7]
    right_side = [3,6,9]
    mid_side = [2,5,8,0]

    left_hand = '*'
    right_hand = '#'
    answer = ''

    for i in range(len(numbers)):
        if numbers[i] in left_side:
            answer += 'L'
            left_hand = str(numbers[i])
        elif numbers[i] in right_side:
            answer += 'R'
            right_hand = str(numbers[i])
        else: 
            if get_distance(left_hand, numbers[i]) < get_distance(right_hand, numbers[i]):
                answer += 'L'
                left_hand = str(numbers[i])
            elif  get_distance(left_hand, numbers[i]) > get_distance(right_hand, numbers[i]):
                answer += 'R'
                right_hand = str(numbers[i])
            else:
                if hand == 'left':
                    answer += 'L'
                    left_hand = str(numbers[i])
                else:
                    answer += 'R'
                    right_hand = str(numbers[i])
    return answer


# In[8]:


# test case 
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
# 기대값: "LRLLLRLLRRL"
solution(numbers, hand)

