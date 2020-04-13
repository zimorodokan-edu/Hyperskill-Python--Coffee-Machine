class CM:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.operate_state = None

    def print_state(self):
        print()
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'${self.money} of money')
        print()

    def get_user_input(self, action):
        if action == 'remaining':
            self.print_state()
            self.wait_for_action()
        elif action == 'take':
            print(f'I gave you ${self.money}')
            self.money = 0
            print()
            self.wait_for_action()
        elif action == 'fill':
            self.operate_state = 'fill_water'
            print()
            print('Write how many ml of water do you want to add:')
        elif action == 'buy':
            self.operate_state = 'buy'
            print()
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        elif action == 'back':
            self.wait_for_action()
        elif action.isdecimal():
            if self.operate_state == 'buy':
                if self.cups < 1:
                    print('Sorry, not enough disposable cups!')
                    print()
                    self.wait_for_action()
                elif action == '1':
                    if self.water >= 250:
                        if self.beans >= 16:
                            self.water -= 250
                            self.beans -= 16
                            self.money += 4
                            self.cups -= 1
                            print('I have enough resources, making you a coffee!')
                            print()
                            self.wait_for_action()
                        else:
                            print('Sorry, not enough coffee beans!')
                            print()
                            self.wait_for_action()
                    else:
                        print('Sorry, not enough water!')
                        print()
                        self.wait_for_action()
                elif action == '2':
                    if self.water >= 350:
                        if self.beans >= 20:
                            if self.milk >= 75:
                                self.water -= 350
                                self.beans -= 20
                                self.milk -= 75
                                self.money += 7
                                self.cups -= 1
                                print('I have enough resources, making you a coffee!')
                                print()
                                self.wait_for_action()
                            else:
                                print('Sorry, not enough milk!')
                                print()
                                self.wait_for_action()
                        else:
                            print('Sorry, not enough coffee beans!')
                            print()
                            self.wait_for_action()
                    else:
                        print('Sorry, not enough water!')
                        print()
                        self.wait_for_action()
                elif action == '3':
                    if self.water >= 200:
                        if self.beans >= 12:
                            if self.milk >= 100:
                                self.water -= 200
                                self.beans -= 12
                                self.milk -= 100
                                self.money += 6
                                self.cups -= 1
                                print('I have enough resources, making you a coffee!')
                                print()
                                self.wait_for_action()
                            else:
                                print('Sorry, not enough milk!')
                                print()
                                self.wait_for_action()
                        else:
                            print('Sorry, not enough coffee beans!')
                            print()
                            self.wait_for_action()
                    else:
                        print('Sorry, not enough water!')
                        print()
                        self.wait_for_action()
            elif self.operate_state == 'fill_water':
                self.water += abs(int(action))
                self.operate_state = 'fill_milk'
                print('Write how many ml of milk do you want to add:')
            elif self.operate_state == 'fill_milk':
                self.milk += abs(int(action))
                self.operate_state = 'fill_beans'
                print('Write how many grams of coffee beans do you want to add:')
            elif self.operate_state == 'fill_beans':
                self.beans += abs(int(action))
                self.operate_state = 'fill_cups'
                print('Write how many disposable cups of coffee do you want to add:')
            elif self.operate_state == 'fill_cups':
                self.cups += abs(int(action))
                self.operate_state = None
                print('')
                self.wait_for_action()

    def wait_for_action(self):
        print('Write action (buy, fill, take, remaining, exit):')


cm = CM()
cm.wait_for_action()

while True:
    action = input()

    if action == 'exit':
        break

    cm.get_user_input(action)
