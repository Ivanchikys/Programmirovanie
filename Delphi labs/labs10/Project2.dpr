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
  Write('Введите кол-во элементов матрицы: ');
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
  writeln('Матрица выполнена рандомом');
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

  Writeln('1) количество элементов в матрице');
  Writeln('2) формирование матрицы');
  Writeln('3) вывод матрицы');
  Writeln('4) выполнение произведения над матрицей');
  Writeln('5) выход');

  repeat
    Write('Выберите операцию над матрицей: ');
    Readln(operationNumber);

    if (operationNumber < 1) or (operationNumber > 5) then
    begin
      Write('Неверный ввод. Введите номер операции от 1 до 5: ');
      Readln(operationNumber);
    end;

    case operationNumber of
      1: matrixNum := InputCount();
      2: mat := InputMatrix(matrixNum);
      3: PrintMatrix(matrixNum, mat);
      4: Writeln('Произведение элементов, расположенных на главной диагонали и выше ее: ', ProductM(matrixNum, mat));
      5: Exit;
    end;
  until continue = False;

  readln;
end.
