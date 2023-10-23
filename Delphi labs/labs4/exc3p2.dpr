
var
  a, b: Integer;
  answer: string;
  continue: Boolean;

begin
  continue := True;

  repeat
    Write('Введите число a: ');
    Readln(a);
    Write('Введите число b: ');
    Readln(b);

    Writeln('Произведение: ', a * b);

    Writeln('Продолжить? (Yep/Nah) ');
    Readln(answer);
    continue := (answer = 'Yep');

  until continue = False;

  readln;
end.

