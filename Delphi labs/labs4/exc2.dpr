//� ���������� �������� ����� (������������� � �������������)
//� ��������������� ����������� �� ������.
//����� ���������� ��������� �����, ����� �� ����� ��������� 100.
var
  a :integer;
  count, summa :integer;
begin

summa := 0;
count := 0;

while summa <= 100 do
  begin
    Writeln('������� �����');
      readln(a);
        summa := summa + Abs(a);
        count := count + 1;
  end;
    writeln('���� ������� ����� ���-�� �����: ',count);
      readln;
  end.
