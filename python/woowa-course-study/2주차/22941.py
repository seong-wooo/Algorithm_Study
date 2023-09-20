import math

hp_y, atk_y, hp_m, atk_m = map(int, input().split())
p, s = map(int, input().split())

if hp_m % atk_y == 0 and atk_y <= p:
    hit_y = math.ceil((hp_m + s) / atk_y)

elif hp_m % atk_y != 0 and hp_m % atk_y <= p:
    hit_y = math.ceil((hp_m + s) / atk_y)
else:
    hit_y = math.ceil(hp_m / atk_y)

hit_m = math.ceil(hp_y / atk_m)

print("Victory!") if hit_y <= hit_m else print("gg")