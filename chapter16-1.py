# 1. Modify this function to return a list of strings as defined above

def list_benefits():
    """returns list of strings from list1"""
    list1 = ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
    return (list1)


# 2. Modify this function to concatenate to each benefit - " is a benefit of functions!"

def build_sentence(benefit):
    """returns argument and "is a benefit of functions!" sentence"""
    sentence = benefit + " is a benefit of functions!"
    return sentence


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()

    print(build_sentence(list_of_benefits[0]))

    print(build_sentence(list_of_benefits[1]))

    print(build_sentence(list_of_benefits[2]))

    print(build_sentence(list_of_benefits[3]))


name_the_benefits_of_functions()
