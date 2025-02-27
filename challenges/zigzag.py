def solution(numbers):
    zigzag = []
    for triplet in range(len(numbers)-2):
        zigzag.append(1) if numbers[triplet] < numbers[triplet+1] > numbers[triplet+2] or numbers[triplet] > numbers[triplet+1] < numbers[triplet+2] else zigzag.append(0)
    return zigzag
