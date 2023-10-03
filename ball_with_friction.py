import math

def degree(t: float, a: float, r: float, v: float = 0) -> float|str:
    if r != 0:
        if v != 0:
            if a != 0:
                s = v * t - (a * t ** 2) / 2

                if s <= 0:
                    return 'Invalid values.'
                
                circ_len = 2 * math.pi * r

                alpha = s % circ_len

                return alpha
            else:
                return 'It is impossible to calculate the final angle of rotation of the ball, \
                        because the friction force does not act on the movable ball.'
        
        else:
            return 0
    else:
        return 'The radius of the ball cannot be zero.'