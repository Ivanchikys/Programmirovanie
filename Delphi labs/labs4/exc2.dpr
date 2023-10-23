//С клавиатуры вводятся числа (положительные и отрицательные)
//и последовательно суммируются их модули.
//Найти количество введенных чисел, когда их сумма превысила 100.
var
  a :integer;
  count, summa :integer;
begin

summa := 0;
count := 0;

while summa <= 100 do
  begin
    Writeln('Введите числА');
      readln(a);
        summa := summa + Abs(a);
        count := count + 1;
  end;
    writeln('Было введено такое кол-во чисел: ',count);
      readln;
  end.
