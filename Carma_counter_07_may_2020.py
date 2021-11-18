class Carma_evaluation:
    def __init__(self,
                 sex,
                 meat,
                 gambling,
                 poisons
                 ): #constructor

        self.sex = str(input(f'Enter the "yes" if have illegal sex: ')).lower()
        self.meat = str(input(f'Enter the "yes" if eat meat: ')).lower()
        self.gambling = str(input(f'Enter the "yes" if have gambling: ')).lower()
        self.poisons = str(input(f'Enter the "yes" if smoke, drink, consume drugs: ')).lower()

    def carma_sex(self):
        if 'yes' in self.sex:
            print('\nYour carma is bad-get married!')
        else:
            print('\nYou are good in sex aspect:-)')

    def carma_meat(self):
        if 'yes' in self.meat:
            print('Your carma is bad-do not participate in killing!')
        else:
            print('You are good, not killing and not eating killing products:-)')

    def carma_gambling(self):
        if 'yes' in self.gambling:
            print('Your carma is bad-do not play games!')
        else:
            print('You are good not gambling:-)')

    def carma_poisons(self):
        if 'yes' in self.poisons:
            print('Your carma is bad-do not smoke, drink, consume drugs!\n')
        else:
            print('You are good not poisoning yourself:-)\n')

carma_1 = Carma_evaluation('', '', '', '')
carma_1.carma_sex()
carma_1.carma_meat()
carma_1.carma_gambling()
carma_1.carma_poisons()

carma_2 = Carma_evaluation('', '', '', '')
carma_2.carma_sex()
carma_2.carma_meat()
carma_2.carma_gambling()
carma_2.carma_poisons()

exit()
