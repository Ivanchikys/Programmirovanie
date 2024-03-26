bool a = true;
while (a)
{
    move moveCode = (move)Convert.ToInt32(Console.ReadKey().Key);

    switch (moveCode)
    {
        case move.W:
            Console.WriteLine("—Вперёд");
                break;

        case move.A:
            Console.WriteLine("—Влево");
                break;

        case move.S:
            Console.WriteLine("—Назад");
                break;

        case move.D:
            Console.WriteLine("—Вправо");
                break;

        case move.Esc:
            a = false;
                break;

    }
    Console.WriteLine();
    
} 


enum move
{
    W = 87,
    A = 65,
    S = 83,
    D = 68,
    Esc = 27
}


