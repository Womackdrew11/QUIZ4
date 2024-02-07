import argparse

def main():
    parser = argparse.ArgumentParser(description='Argument Parser Example')
    
    parser.add_argument('input_string', type=str, help='A string input')
    parser.add_argument('input_int', type=int, help='An integer input')
    parser.add_argument('input_float', type=float, help='A float input')

    args = parser.parse_args()

    print(f'String: {args.input_string}')
    print(f'Integer: {args.input_int}')
    print(f'Float: {args.input_float}')

if __name__ == "__main__":
    main()
