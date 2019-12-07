def main():
    groups = {"821": (
    "Egorov", "Bageev", "Abramson", "Adamson", "Adderiy", "Addington", "Adrian", "Bosworth", "Campbell", "Clifford",
    "Emerson", "Francis", "Gate", "Higgins"), "822": (
    "Egorov", "Bageev", "Abramson", "Adamson", "Adderiy", "Addington", "Adrian", "Bosworth", "Campbell", "Clifford"),
              "833": ("Egorov", "Bageev", "Abramson", "Adamson", "Adderiy"),
              "844": ("Egorov", "Bageev", "Abramson", "Adamson")}
    d1 = len(groups.get("821"))
    d2 = len(groups.get("822"))
    d3 = len(groups.get("833"))
    d4 = len(groups.get("844"))
    max = d1
    min = d1
    if d2 > max:
        max = d2
        if d3 > max:
            max = d3;
            if d4 > max:
                max = d4
    if d2 < min:
        min = d2
        if d3 < min:
            min = d3;
            if d4 < min:
                min = d4

    if max == d1:
        print(groups.get("821"))
    if max == d2:
        print(groups.get("822"))
    if max == d3:
        print(groups.get("833"))
    if max == d4:
        print(groups.get("844"))
    print()
    if min == d1:
        print(groups.get("821"))
    if min == d2:
        print(groups.get("822"))
    if min == d3:
        print(groups.get("833"))
    if min == d4:
        print(groups.get("844"))

if __name__ == '__main__':
    main()
