
var
  n: Integer;
  answer: string;
  continue: Boolean;

begin
  continue := True;

  while continue do begin

    Writeln('������� �����: ');
    Readln(n);

    if n mod 2 = 0 then
      Writeln('����� ������')
    else
      Writeln('����� ��������');


    Writeln('����������? (Yep/Nah) ');
    Readln(answer);
    continue := (answer = 'Yep');

  end;
  readln;
end.

