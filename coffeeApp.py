class CoffeMaker:
	water=400
	milk=540
	beans=120
	disposables=9
	cash=550
	def __init__(self,name,coffee_shop):
		self.name = name
		self.coffee_shop = coffee_shop

	def do(self):
		self.action=input('Write action (buy, fill, take, remaining, exit): ')
		while True:
			if self.action == 'buy':
				self.coffee_type=input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')

				if self.coffee_type == 'back':
					self.action=input('Write action (buy, fill, take, remaining, exit): ')

				elif self.coffee_type == '1':
					if self.water >= 250:
						print('I have enough resources, making you a coffee!\n')
						print('done, enjoy!')
						self.water-=250
						self.beans-=16
						self.cash+=4
						self.disposables-=1
						

					else:
						print('Sorry, not enough water!')
					self.action=input('Write action (buy, fill, take, remaining, exit): ')

				elif self.coffee_type == '2':
					if self.water >= 350:
						print('I have enough resources, making you a coffee!\n')
						print('done, enjoy!')
						self.water-=350
						self.milk-=75
						self.beans-=20
						self.cash+=7
						self.disposables-=1

					else:
						print('Sorry, not enough water!')
					self.action=input('Write action (buy, fill, take, remaining, exit): ')

				elif self.coffee_type == '3':
					if self.water >= 200:
						print('I have enough resources, making you a coffee!\n')
						print('done, enjoy!')
						self.water-=200
						self.milk-=100
						self.beans-=12
						self.cash+=6
						self.disposables-=1

					else:
						print('Sorry, not enough water!')

					self.action=input('Write action (buy, fill, take, remaining, exit): ')

			elif self.action == 'fill':
				self.water+=int(input('Write how many ml of water do you want to add: '))
				self.milk+=int(input('Write how many ml of milk do you want to add: '))
				self.beans+=int(input('Write how many grams of coffee beans do you want to add: '))
				self.disposables+=int(input('Write how many disposable cups of coffee do you want to add: '))
				print('Done! ready')
				self.action=input('Write action (buy, fill, take, remaining, exit): ')

			elif self.action == 'remaining':
				print('The coffee machine has: ')
				print(self.water,'of water')
				print(self.milk,'of milk')
				print(self.beans,'of coffee beans')
				print(self.disposables,'of disposable cups')
				print('${} of money'.format(self.cash))
				self.action=input('Write action (buy, fill, take, remaining, exit): ')

			elif self.action == 'take':
				print('I gave you ${}'.format(self.cash))
				self.cash = 0
				self.action=input('Write action (buy, fill, take, remaining, exit): ')

			elif self.action == 'exit':
				break

myCoffee = CoffeMaker('ballsy','starbucks')
myCoffee.do()









