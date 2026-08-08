#include <iostream>
#include <time.h>
using namespace std;


int main()
{
	srand(time(0));
	setlocale(LC_ALL, "RU");

	int level, a, b, health, number, user_variant, help, points, quit, round = 1;
	bool win_round;

	cout << "Приветствуем в игре!" << endl

	a = 1;
	b = 10;
	health = 10 / 2;
	points = 0;


    cout << "Добро пожаловать на 1-ый уровень." << endl << endl;

	for (int i = 1; i < 4; i++) {
		cout << "Раунд " << i << "" << endl;
		cout << "Компьютер загадывает число..." << endl;
		Sleep(1000);
		number = rand() % b + a;
		while (true) {
			cout << "Введите число:";
			cin >> user_variant;
			if (user_variant == number) {
				cout << "Ты угадал!" << endl;
				health *= 5;
				break;
			}
			else {
				cout << "Неправильно!" << endl;
				--health;
			}

			if (health <= 0) {
				win_round = false;
				break;
			}

			else {
				cout << "Хотите подсказку? Стоимость подсказки - 1 жизнь" << endl
					 << "Введите 1 если да и 2 если нет" << endl;
				cin >> help;
				if (help == 1) {
					if (user_variant > number) {
						cout << "Ваше число больше чем загаданное." << endl;
					}
					else {
						cout << "Ваше число меньше чем загаданное." << endl;
					}
					--health;
				}

			}
		}
		if (!win_round) {
			cout << "Ты проиграл уровень!" << endl;
			break;
		}
		else {
			cout << "Раунд пройден, молодец!" << endl;
		}
	}

		
}











	if (level == 1) {
		a = 1;
		b = 10;
		health = b / 2;
		number = rand() % b + a;
	}
	else if (level == 2) {
		a = 10;
		b = 100;
		health = (b - a + 1) / 4;
		number = rand() % b + a;
	}
	else {
		cout << "проверьте вводимые данные." << endl;
	}
	while (true)
	{
		cout << "Введите число: ";
		cin >> user_variant;
		if (user_variant == number) {
			cout << "Молодец, ты победил!" << endl
				<< " У тебя " << (level == 1 ? health * 5 : health * 10) << " очков.";
			break;
		}
		else {
			cout << "Неправильно." << endl;
			--health;
		}
		if (health <= 0) {
			cout << "У вас не осталось жизней, вы умерли(" << endl;
			break;
		}
		else {
			cout << "Хотите подсказку? Стоимость подсказки - 1 жизнь" << endl
				<< "Введите 1 если да и 2 если нет" << endl;
			cin >> help;
			if (help == 1) {
				if (user_variant > number) {
					cout << "Ваше число больше чем загаданное." << endl;
				}
				else {
					cout << "Ваше число меньше чем загаданное." << endl;
				}
				--health;
			}
		}

	}

}