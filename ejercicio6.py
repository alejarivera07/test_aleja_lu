import pandas as pd


def main():
	#retrieve data
	data = pd.read_excel("Data_For_Test_2022_08_31.xlsx")
	# 1. filter report before 20h
	data = data[data['Hora']<20]
	# 2. filter drivers from BOG
	data = data[data['Ciudad']=='Bogotá']
	# 3. filter drivers with Carry vh
	data = data[data['vehiculo']=='Carry']
	# 4. filter drivers with status available
	data = data[data['status'] == 'AVAILABLE']
	# 5. filter drivers with score > 5
	data = data[data['puntos'] > 5]
	#6. filter drivers with debt between 300 and 1300
	data = data[(data['deuda'] >=300) & (data['deuda']<= 1300)]
	print(data.value_counts(data['deuda']))


if __name__ == '__main__':
	main()