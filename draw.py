from display import plot
from math import floor

def draw_line(x0, y0, x1, y1, screen, color):
    if x0 == x1 or y0 == y1: return
    # draw_line(x1, y1, x0, y0, screen, color)
    print(x0, y0, x1, y1)
    if x0 == x1 or y0 == y1: return
    midX = floor((x1 + x0) / 2)
    midY = floor((y1 + y0) / 2)
    if midX == x1 or midY == y1: return
    if midX == x0 and midX != x1:
        x0 += 1
        midX += 1
    if midY == x0 and midY != x1:
        y0 += 1
        midY += 1
    plot(screen, color, midX, midY)
    draw_line(x0, y0, midX, midY, screen, color)
    draw_line(midX, midY, x1, y1, screen, color)

def draw_line_backup( x0, y0, x1, y1, screen, color ):
    if x0 == x1 and y0 == y1: return
    if x0 > x1: return draw_line(x1, y1, x0, y0, screen, color)
    if x1 - x0 == 0:
        if y1 > y0:
            plot(screen, color, y0 + 1, y1)
            return draw_line(x0, y0 + 1, x1, y1, screen, color)
        else:
            plot(screen, color, y0 - 1, y1)
            return draw_line(x0, y0 - 1, x1, y1, screen, color)
    slope = (y1 - y0) / (x1 - x0)
    if slope > 1:
        plot(screen, color, x0, y0 + 1)
        return draw_line_backup(x0, y0 + 1, x1, y1, screen, color)
    elif slope == 1:
        plot(screen, color, x0 + 1, y0 + 1)
        return draw_line_backup(x0 + 1, y0 + 1, x1, y1, screen, color)
    elif slope > 0:
        plot(screen, color, x0 + 1, y0)
        return draw_line_backup(x0 + 1, y0, x1, y1, screen, color)
    elif slope > -1:
        plot(screen, color, x0 + 1, y0)
        return draw_line_backup(x0 + 1, y0, x1, y1, screen, color)
