//����� ���������� ������������� ��������� � ������ ������ �������.
function generateNumber(min, max: Integer): Integer;

  begin
    Result := Random(max - min) + min;
  end;

const N = 4;
      M = 4;


var matrix: array[1..N,1..M] of integer;
  i, j, count : Integer;
  dmin, dmax  : Integer;
begin
Writeln('������� �������� ������� ');
readln(dmin,dmax);
                //��� ���������� �������
 for i := 1 to N do
   for j := 1 to M do
    matrix[i, j] := generateNumber(dmin,dmax);

    writeln('�������� �������:');
  for i := 1 to N do
  begin
    for j := 1 to M do
      write(matrix[i, j], ' ');
    writeln;
  end;

  // ���������� ���������� ������������� ��������� � ������ ������
  count := 0;
  for i := 1 to M do
   begin
    if matrix[1][i] < 0 then
   count := count + 1;
  end;
  Writeln('���-�� ������������� ��������� � ������ ������ = ',count);
  readln;
  end.
