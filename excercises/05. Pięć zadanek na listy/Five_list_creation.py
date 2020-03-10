numbers = [0, 5, 10, 15, 20, 25, 30]

for num in [0, 1, 5, 6]:
    print(numbers[num])



print(numbers[0], numbers[1], numbers[5], numbers[6])
print(numbers[-7], numbers[-6], numbers[-2], numbers[-1])
print(numbers[2:6:2])



names = ["JULIA", "ZUZANNA", "MAJA", "ZOFIA", "LENA", "ANTONI", "JAKUB", "JAN", "SZYMON", "FRANCISZEK"]

print("Najbardziej popularne imiona: ", names[0], names[-1])



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)



numbers1 = [
951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165,
141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418,
907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918,
237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892,
894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685,
93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527
]

#numbers2 = []

for i in numbers1:
    if i%2 == 0:
        #numbers2.append(i)
        print(i, end="-") #tu zamiast i miałem drugą listę -> numbers2

