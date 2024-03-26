using System.ComponentModel.Design;
using System.Threading.Channels;
//Есть логин/пароль для входа в систему:
//Запросить у пользователя логин и пароль.
//На введение верного пароля есть только три попытки.
//Если пользователь авторизовался успешно вывести "Xui", 
//если ошибся трижды - "Go naxui pls" и прекратить запрос пары логин/пароль.
Console.WriteLine("Регистрация\n\n");

Console.WriteLine("Введите логин");
string Login = Console.ReadLine();

Console.WriteLine("Введите пароль");
string Password = Console.ReadLine();

Console.Clear();



Console.WriteLine("Авторизация\n\n");

bool tl = true;
int countl = 0;

Console.WriteLine("Введите логин");
while (tl)
{
    if (countl < 3)
    {
        if (Console.ReadLine() != Login)
        {
            Console.WriteLine("Не верно указан логин\n");
            countl++;
        }

        else
        {
            tl = false;
        }
    }
    else
    {
        Console.WriteLine("Poshel Naxuj");
        tl = false;
    }
}


bool tp = true;
int countp = 0;

Console.WriteLine("Введите пароль");
while (tp)
{

    if (countp < 3)
    {
        if (Console.ReadLine() != Password)
        {
            Console.WriteLine("Не верно указан Пароль\n");
            countp++;
        }
        else
        {
            Console.WriteLine(" ВЫ АВТОРИЗОВАНЫ");
            tp = false;
        }
    }
    else
    {
        Console.WriteLine("Poshel Naxuj");
        tp = false;
    }

}

 


