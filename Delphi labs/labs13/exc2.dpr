//Напишите программу с использованием динамического массива.
//Дана целочисленная матрица размером 5 x 4, все элементы которой различны.
//Вывести матрицу на экран.
//Найти в 5 строке наименьший элемент и вывести его индекс на экран.


program exc2;

var
  matrix: array of array of Integer;
  i, j, min, minIndex: Integer;

begin
  SetLength(matrix, 5);
  for i := 0 to 4 do
  begin
    SetLength(matrix[i], 4);
    for j := 0 to 3 do
      matrix[i][j] := i * 4 + j + 1;
  end;


  for i := 0 to 4 do
  begin
    for j := 0 to 3 do
      Write(matrix[i][j]:4);
    Writeln;
  end;


  min := matrix[4][0];
  minIndex := 0;
  for j := 1 to 3 do
  begin
    if matrix[4][j] < min then
    begin
      min := matrix[4][j];
      minIndex := j;
    end;
  end;

  Writeln('Min element in the 5th row is = ', min,' / at index = ', minIndex);
  readln;
end.
