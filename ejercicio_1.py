import pandas as pd

def main():
	#retrieve data
	data = pd.read_excel("Data_For_Test_2022_08_31.csv")
	# 1. filter report before 20h
	data = data[data['Hora']<20]
	print(data.value_counts(data['Hora']<20))


if __name__ == '__main__':
	main()