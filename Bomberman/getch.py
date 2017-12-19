# Taken from Internet for input purpose only.
class _Getch:
    """Gets a single character from standard input.
    Does not echo to the screen. """

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix:
    def __init__(self, poll_period=1.5):
        import tty
        import sys
        self.poll_period = poll_period

    def __call__(self):
        import sys
        import tty
        import termios
        import select
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            [i, o, e] = select.select([sys.stdin.fileno()], [], [], self.poll_period)
            if i:
                ch = sys.stdin.read(1)
            else:
                ch = ''
                # ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

# i = 0
# while i <= 9:
#    key = getch()
#    print ("key: ", key)
#    i += 1
