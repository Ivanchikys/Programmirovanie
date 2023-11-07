program exc2uniqueV;

const
  N = 4;

type
  Matrix = array[0..3 , 0..3] of Integer;

var
  operationNumber, matrixNum, i, j: Integer;
  mat: Matrix;
  continue: Boolean;

function InputCount(): Integer;
begin
  Write('������� ���-�� ��������� �������: ');
  Readln(operationNumber);
  InputCount := operationNumber;
end;

function InputMatrix(matrixNum: integer): Matrix;
begin
  for i := 0 to matrixNum - 1 do
    for j := 0 to matrixNum - 1 do
    begin
      mat[i, j] := random(10);
    end;
  writeln('������� ��������� ��������');
  InputMatrix := mat;
end;

procedure PrintMatrix(matrixNum: integer; matrix: Matrix);
begin
  for i := 0 to matrixNum - 1 do
  begin
    for j := 0 to matrixNum - 1 do
      Write(' ', matrix[i, j]);
    Writeln;
  end;
end;

function ProductM(matrixNum: integer; matrix: Matrix): Integer;
var
  j,i: Integer;
  product: Integer;

begin
  product := 1;
  for i := 0 to matrixNum - 1 do
    for j := 0 to matrixNum - 1 do
      if  (i + j >= matrixNum - 1 )  then
        product := product * matrix[i, j];

  ProductM := product;
end;

begin
  continue := True;
  randomize;

  Writeln('1) ���������� ��������� � �������');
  Writeln('2) ������������ �������');
  Writeln('3) ����� �������');
  Writeln('4) ���������� ������������ ��� ��������');
  Writeln('5) �����');

  repeat
    Write('�������� �������� ��� ��������: ');
    Readln(operationNumber);

    if (operationNumber < 1) or (operationNumber > 5) then
    begin
      Write('�������� ����. ������� ����� �������� �� 1 �� 5: ');
      Readln(operationNumber);
    end;

    case operationNumber of
      1: matrixNum := InputCount();
      2: mat := InputMatrix(matrixNum);
      3: PrintMatrix(matrixNum, mat);
      4: Writeln('������������ ���������, ������������� �� ������� ��������� � ���� ��: ', ProductM(matrixNum, mat));
      5: Exit;
    end;
  until continue = False;

  readln;
end.
