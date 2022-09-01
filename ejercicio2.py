import pandas as pd

def main():
	#retrieve data
	data = pd.read_excel("Data_For_Test_2022_08_31.xlsx")
	# 1. filter report before 20h
	data = data[data['Ciudad']=='Bogotá']
	print(data.value_counts(data['Ciudad']=='Bogotá'))


if __name__ == '__main__':
	main()