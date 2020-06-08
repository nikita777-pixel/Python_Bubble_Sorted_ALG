# Import library here:

import random # Import rundom here.

class BubbleSorted:
    # Realization Bubble Sorted here:

    mas = [] # Created massive .
    max_num = 99 # max num to massive.
    min_num = 1 # min num to massive.
    len_mas = len(mas) # Check len to mas (variable).

    def __init__(self):
        # Construct here:

        print("Don't Sorted Massive: ")

        for i in range(10): # Craeted Rundom Number to massive here:
            x1 = random.randint(self.min_num, self.max_num) # Variable x1 == random number.
            self.mas.append(x1) # Crated mas[] rundom number.

        lens_mas = len(self.mas) # Variable read how many lines here.

    def Check_Rundom_Numbers_To_Massive(self):
        # Check Rundom Number to massive here:

        for i in range(10):
            print(self.mas[i])

    def Realization_Bubble_Sorted(self):
        # Realization Bubble Sorted here

        self.len_mas = len(self.mas) # Created Variable (len_mas) Check len to (len_mas) variable.

        for i in range(self.len_mas):
            for j in range(self.len_mas - 1):
                # Realization Swap Numbers if : mas[1] > mas[2] here:

                if self.mas[j] > self.mas[j + 1]:

                    # Swap number to mas:

                    self.mas[j], self.mas[j + 1] = self.mas[j + 1], self.mas[j]

        # Realization Check Sorted massive here:

        print("Sorted massive: ")

        for i in range(10):
            print(self.mas[i])

def main():
    # write code here:

    bub = BubbleSorted() # Crated Object (bub) here:
    bub.Check_Rundom_Numbers_To_Massive()
    bub.Realization_Bubble_Sorted()

main() # Created main (function) here.

