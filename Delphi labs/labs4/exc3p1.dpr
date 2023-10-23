
var
  n: Integer;
  answer: string;
  continue: Boolean;

begin
  continue := True;

  while continue do begin

    Writeln('Введите число: ');
    Readln(n);

    if n mod 2 = 0 then
      Writeln('Число четное')
    else
      Writeln('Число нечетное');


    Writeln('Продолжить? (Yep/Nah) ');
    Readln(answer);
    continue := (answer = 'Yep');

  end;
  readln;
end.

