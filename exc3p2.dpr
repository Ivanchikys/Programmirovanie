
var
  a, b: Integer;
  answer: string;
  continue: Boolean;

begin
  continue := True;

  repeat
    Write('������� ����� a: ');
    Readln(a);
    Write('������� ����� b: ');
    Readln(b);

    Writeln('������������: ', a * b);

    Writeln('����������? (Yep/Nah) ');
    Readln(answer);
    continue := (answer = 'Yep');

  until continue = False;

  readln;
end.

