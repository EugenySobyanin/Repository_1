#include <iostream>


int main()
{
	using namespace std;
	setlocale(LC_ALL, "RU");
	srand(time(0));

	const int len = 3;
	int numbers[len][len], number;
	for (int i = 0; i < len; i++)
	{
		for (int j = 0; j < len; j++) 
		{
			if (j == 0)
			{
				cout << "Введите число: ";
				cin >> number;
				numbers[i][j] = number;
			}
			else
			{
				number *= 2;
				numbers[i][j] = number;
			}
		}
	}

	for (int i = 0; i < len; i++)
	{
		for (int j = 0; j < len; j++)
		{
			cout << numbers[i][j] << " ";
		}
		cout << endl;
	}


}