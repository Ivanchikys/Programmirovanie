//В динамическом одномерном целочисленном массиве
//положительные элементы заменить на 1, а отрицательные – на –1.
        uses Math;

var
  arr: array of Integer;
  i , sum : Integer;
begin

  randomize;
  SetLength(arr, 10);
  for i := 0 to Length(arr) - 1 do
    arr[i] := RandomRange(-10 , 10);

  for i := 0 to Length(arr) - 1 do write(arr[i], ' ');
  writeln;
  write('↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ');
  writeln;

  for i := 0 to Length(arr) - 1 do
  begin
    if arr[i] > 0 then
      arr[i] := 1
    else if arr[i] < 0 then
      arr[i] := -1;
  end;

 for i := 0 to Length(arr) - 1 do write(arr[i], ' ');

 writeln;
 write('↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ');
 writeln;

  sum:= 0;
  for i := 0 to Length(arr) - 1 do
    if arr[i] mod 2 <> 0 then
      sum := sum + arr[i];


 write('Sum odd elements = ',sum);

  readln;


end.
