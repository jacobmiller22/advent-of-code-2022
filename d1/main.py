import sys


def p1(lines):
    m = 0
    m_i = -1
    c = 0
    g = 0
    for i, line in enumerate(lines):
        if line.strip() == "":
            g += 1
            # New group
            if c > m:
                m_i = g
                m = c
            c = 0
        else:
            c += int(line.strip())

    print(f"Part 1: elf: {m_i}, cal: {m}")


def p2(lines):
    m_cal = [0, 0, 0]  # max calories
    g_cal = [0, 0, 0]  # group number for max calories
    c = 0  # Current calories
    g = 0  # Current group
    cals = [0]
    for i, line in enumerate(lines):
        if line.strip() == "":
            cals.append(0)
            g += 1
        else:
            cals[g] += int(line.strip())

    # Get the top 3 groups and their indices
    for i in range(3):
        max_cals = max(cals)
        max_cals_index = cals.index(max_cals)
        m_cal[i] = max_cals
        g_cal[i] = max_cals_index + 1
        cals[max_cals_index] = 0

    print(m_cal)

    # Sort the groups by calories, but they are connected

    # res = sum(m_cal)

    # Sum t

    print(f"Part 2: res: {sum(m_cal)}")


def main():

    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    # p1(lines)

    p2(lines)


if __name__ == '__main__':
    main()
