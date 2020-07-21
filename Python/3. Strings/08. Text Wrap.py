import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)  # with TextWap
    # return "".join([string[i:i+max_width] for i in range(0, len(string), max_width)]) # Without TextWrap


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
