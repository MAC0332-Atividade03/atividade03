import argparse
from solucoes import sao_anagramas

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="atv4.py",
        description="Identify Anagrams"
    )

    parser.add_argument("str1", type=str)
    parser.add_argument("str2", type=str)

    args = parser.parse_args()

    string1 = args.str1
    string2 = args.str2

    print(sao_anagramas(string1, string2))