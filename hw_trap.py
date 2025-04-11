def trap(height):
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0
    
    while left < right:
        if left_max <= right_max:
            left += 1
            if height[left] > left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
        else:
            right -= 1
            if height[right] > right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
    
    return water

# 테스트 케이스 실행 및 결과 출력
test_cases = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([2, 0, 2], 2),
    ([3, 0, 0, 2, 0, 4], 10),
    ([4, 2, 0, 3, 2, 5], 9),
    ([5, 4, 3, 2, 1], 0),
    ([1, 0, 1], 1),
    ([0, 0, 0, 0], 0),
]

for i, (h, expected) in enumerate(test_cases, 1):
    result = trap(h)
    print(f"테스트 케이스 {i}:")
    print(f"입력: {h}")
    print(f"예상 출력: {expected}")
    print(f"실제 출력: {result}")
    print("통과" if result == expected else "실패")
    print("-" * 50)