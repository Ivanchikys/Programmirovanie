var
n, sum, number: Integer;

procedure SumNumbers(n: Integer; var sum: Integer);

begin
  while n > 0 do begin
    number := n mod 10;
    sum := sum + number;
    n := n div 10;
  end;

end;

begin
  Write('Введите число: ');
  readln(n);

  sum := 0;
  SumNumbers(n, sum);

  Writeln('Сумма цифр числа: ', sum);
  readln;
end.

