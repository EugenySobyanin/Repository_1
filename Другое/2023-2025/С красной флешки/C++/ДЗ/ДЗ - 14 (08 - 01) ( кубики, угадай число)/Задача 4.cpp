#include <iostream>
#include <ctime>
#include <windows.h>



int main()
{
	using namespace std;
	setlocale(LC_ALL, "RU");
	srand(time(0));

	int level, a, b, health, number, user_variant, help, points, quit, round = 1;
	bool win_round;

	cout << "Приветствуем в игре!" << endl << endl;


	points = 0;


	cout << "1-ый уровень." << endl
		<< "Ты должен угадать число от 1 до 10 три раза подряд." << endl << endl;

	for (int i = 1; i < 4; i++)
	{
		a = 1;
		b = 10;
		health = 10 / 2;
		win_round = true;

		cout << "Раунд " << i << "" << endl;
		cout << "Количество жизней: " << health << endl;
		cout << "Компьютер загадывает число..." << endl;
		Sleep(1000);
		cout << "Загадал." << endl;
		Sleep(1000);
		number = rand() % b + a;

		while (true)
		{
			cout << "Введите число:";
			cin >> user_variant;
			cout << endl;
			if (user_variant == number)
			{
				cout << "Ты угадал!" << endl;
				break;
			}
			else
			{
				cout << "Неправильно." << endl;
				--health;
				cout << "Количество жизней: " << health << endl;
			}

			if (health <= 0)
			{
				win_round = false;
				break;
			}

			else if(health != 1)
			{
				cout << "Хотите подсказку? Стоимость подсказки - 1 жизнь" << endl
					<< "Введите 1 если да и 2 если нет" << endl;
				cin >> help;
				if (help == 1)
				{
					if (user_variant > number)
					{
						cout << "Ваше число больше чем загаданное." << endl;
					}
					else
					{
						cout << "Ваше число меньше чем загаданное." << endl;
					}
					--health;
					cout << "Количество жизней: " << health << endl;
				}

			}
		}
		if (!win_round)
		{
			cout << "Ты проиграл уровень!" << endl << endl;
			break;
		}
		else
		{
			points += health * 5;
			cout << "Раунд пройден, молодец!" << endl
				<< "Очки: " << points << endl << endl;
		}
	}
	if (win_round)
	{
		cout << "Поздравляем, вы перешли на второй уровень!" << endl
			 << "Ты должен угадать число от 10 до 100 два раза подряд" << endl << endl;

		for (int i = 1; i < 3; i++)
		{
			a = 10;
			b = 100;
			health = (100 - 10) / 8;
			win_round = true;
			cout << "Раунд " << i << "" << endl
				 << "Количество жизней: " << health << endl
		         << "Компьютер загадывает число..." << endl;
			Sleep(1000);
			number = rand() % b + a;
			cout << "Загадал." << endl;
			Sleep(1000);

			while (true)
			{
				cout << "Введите число:";
				cin >> user_variant;
				cout << endl;
				if (user_variant == number)
				{
					cout << "Ты угадал!" << endl;
					break;
				}
				else
				{
					cout << "Неправильно." << endl;
					--health;
					cout << "Количество жизней: " << health << endl;

				}

				if (health <= 0)
				{
					win_round = false;
					break;
				}

				else if(health != 1)
				{
					cout << "Хотите подсказку? Стоимость подсказки - 1 жизнь" << endl
						<< "Введите 1 если да и 2 если нет" << endl;
					cin >> help;
					if (help == 1)
					{
						if (user_variant > number)
						{
							cout << "Ваше число больше чем загаданное." << endl;
						}
						else
						{
							cout << "Ваше число меньше чем загаданное." << endl;
						}
						--health;
						cout << "Количество жизней: " << health << endl;
					}

				}
			}
			if(!win_round)
			{
				cout << "Ты проиграл раунд." << endl;
				break;
			}
			else
			{
				points += health * 10;
				cout << "Раунд пройден, молодец!" << endl
					 << "Очки: " << points << endl << endl;
			}
		}
		if (win_round)
		{
			cout << "Поздравляю, ты прошел игру!";
		}
	}
}