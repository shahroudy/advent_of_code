def trick_shot(x0, x1, y0, y1):
    maxy = -100
    count = 0

    for dx_s in range(0, x1 + 1):
        if dx_s * (dx_s + 1) / 2 < x0:
            continue
        for dy_s in range(-100, 100):
            x, y = 0, 0
            dx, dy = dx_s, dy_s
            current_max_y = -100
            for _ in range(1000):
                if dy < 0 and y < y0:
                    break
                if dx == 0 and (x < x0 or x > x1):
                    break
                x += dx
                y += dy
                if dx > 0:
                    dx -= 1
                elif dx < 0:
                    dx += 1
                dy -= 1
                current_max_y = max(current_max_y, y)
                if x0 <= x <= x1 and y0 <= y <= y1:
                    maxy = max(maxy, current_max_y)
                    count += 1
                    break
    return maxy, count


if __name__ == "__main__":
    assert trick_shot(20, 30, -10, -5) == (45, 112)
    print(trick_shot(192, 251, -89, -59))
