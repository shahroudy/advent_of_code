from lark import Lark, UnexpectedInput


def count_matching_inputs(grammar, start, expressions):
    parser = Lark(grammar, start=start)
    match_count = 0
    for txt in expressions:
        try:
            parser.parse(txt)
            match_count += 1
        except UnexpectedInput:
            pass
    return match_count
