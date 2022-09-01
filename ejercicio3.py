import pandas as pd

def main():
	#retrieve data
	data = pd.read_excel("Data_For_Test_2022_08_31.xlsx")
	# 1. filter report before 20h
	print(data.value_counts(data['Hora']=='Carry'))


if __name__ == '__main__':
	main()