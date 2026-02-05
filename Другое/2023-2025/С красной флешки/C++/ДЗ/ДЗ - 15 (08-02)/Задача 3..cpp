#include <iostream>


int main()
{
	using namespace std;
	setlocale(LC_ALL, "RU");
	float month_profit[13]{ 0 }, min_profit, max_profit;
	int left, right, min, min_index, max_index;

	for (int i = 0; i <= 12; i++)
	{
		switch (i)
		{
		case 0:
			continue;
		case 1:
			cout << "Введите прибыль за январь: ";
			cin >> month_profit[i];
			break;
		case 2:
			cout << "Введите прибыль за февралт: ";
			cin >> month_profit[i];
			break;
		case 3:
			cout << "Введите прибыль за март: ";
			cin >> month_profit[i];
			break;
		case 4:
			cout << "Введите прибыль за апрель: ";
			cin >> month_profit[i];
			break;
		case 5:
			cout << "Введите прибыль за май: ";
			cin >> month_profit[i];
			break;
		case 6:
			cout << "Введите прибыль за июнь: ";
			cin >> month_profit[i];
			break;
		case 7:
			cout << "Введите прибыль за июль: ";
			cin >> month_profit[i];
			break;
		case 8:
			cout << "Введите прибыль за август: ";
			cin >> month_profit[i];
			break;
		case 9:
			cout << "Введите прибыль за сентябрь: ";
			cin >> month_profit[i];
			break;
		case 10:
			cout << "Введите прибыль за октябрь: ";
			cin >> month_profit[i];
			break;
		case 11:
			cout << "Введите прибыль за ноябрь: ";
			cin >> month_profit[i];
			break;
		case 12:
			cout << "Введите прибыль за декабрь: ";
			cin >> month_profit[i];
			break;
		default:
			cout << "Проверьте вводимые данные.";
			break;
		}
	}

	cout << endl;
	cout << "Введите границы диапазона: ";
	cin >> left >> right;

	if (left > right)
	{
		swap(left, right);
	}

	min_profit = month_profit[left];
	max_profit = month_profit[right];

	for (int j = left; j <= right; j++)
	{
		if (month_profit[j] < min_profit)
		{
			min_profit = month_profit[j];
			min_index = j;
		}
		if (month_profit[j] > max_profit)
		{
			max_profit = month_profit[j];
			max_index = j;
		}

		cout << "Прибыль за " << j << " месяц: " << month_profit[j] << endl;
	}

	cout << endl;
	cout << "Минимальная прибыль: " << min_profit << endl;
	cout << "Максимальная прибыль: " << max_profit << endl;
}