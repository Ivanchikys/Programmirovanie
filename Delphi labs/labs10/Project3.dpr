

var matrix: array[0..4,0..4] of integer;
  i, j : Integer;
  K , L, sum: Integer;

  Function CalculateSum (num :Integer) :Integer;
       begin;
         sum := sum + num;
      end;

begin
                //ген двумерного массива
 for i := 0 to 4 do
   for j := 0 to 4 do
    matrix[i, j] :=  i * j;

    writeln('Исходная матрица:');
  for i := 0 to 4 do
  begin
    for j := 0 to 4 do
      write(matrix[i, j], ' ');
    writeln;
  end;

  K := 0;
  L := 20;

  for i := 0 to 4 do
    for j := i to 4 do
      if (matrix[i, j] >= K) and (matrix[i, j] < L) then
        sum := sum + (matrix[i, j]);

         write('Сумма чисел выше главной диагонали в входий в [K ; L) = ',sum);
  readln;
  end.
