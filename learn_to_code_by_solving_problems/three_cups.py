# https://dmoj.ca/problem/coci06c5p1 coci06c5p1
# swap A => 1 goes to 2, swap B => 2 goes to 3, swap C => 1 goes to 3
swaps = str(input())
ball_location = 1
for swap_type in swaps:
    if swap_type == 'A' and ball_location == 1:
        ball_location = 2
    elif swap_type == 'A' and ball_location == 2:
        ball_location = 1
    elif swap_type == 'B' and ball_location == 2:
        ball_location = 3
    elif swap_type == 'B' and ball_location == 3:
        ball_location = 2
    elif swap_type == 'C' and ball_location == 1:
        ball_location = 3
    elif swap_type == 'C' and ball_location == 3:
        ball_location = 1

print(ball_location)


