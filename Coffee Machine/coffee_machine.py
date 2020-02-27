class CoffeeMachine:

    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.action = ''

    def machine_has(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee_beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')
        print()

    def use_resource(self, water1, milk1, coffee_beans1, cup):
        self.water
        self.milk
        self.coffee_beans
        self.cups
        self.money
        if water1 > self.water:
            print('Sorry, not enough water!')
        elif milk1 > self.milk:
            print('Sorry, not enough milk!')
        elif coffee_beans1 > self.coffee_beans:
            print('Sorry, not enough Coffee Beans!')
        elif cup > self.cups:
            print('Sorry, not enough cup!')
        else:
            self.water -= water1
            self.milk -= milk1
            self.coffee_beans -= coffee_beans1
            self.cups -= cup
            print('I have enough resources, making you a coffee!')

    def buy(self):
        # self.money
        action = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        if action == '1':
            self.use_resource(250, 0, 16, 1)
            self.money += 4
        elif action == '2':
            self.use_resource(350, 75, 20, 1)
            self.money += 7
        elif action == '3':
            self.use_resource(200, 100, 12, 1)
            self.money += 6
        elif action.lower() == 'back':
            self.machine_action("")
        print()

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add: '))
        self.milk += int(input('Write how many ml of milk do you want to add: '))
        self.coffee_beans += int(input('Write how many grams of coffee beans do you want to add: '))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add: '))
        print()

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0
        print()

    def machine_action(self, entrada):
        self.action
        while self.action.lower() != 'exit':
            self.action = input('Write action (buy, fill, take, remaining, exit): ')
            if self.action.lower() == 'exit':
                break
            elif self.action.lower() == 'fill':
                self.fill()
            elif self.action.lower() == 'take':
                self.take()
            elif self.action.lower() == 'remaining':
                print()
                self.machine_has()
                self.machine_action('')
            elif self.action.lower() == 'buy':
                self.buy()
        print()


cafe = CoffeeMachine()
cafe.machine_action(input)
