﻿   uses Math;

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


  sum:= 0;
  for i := 0 to Length(arr) - 1 do
    if arr[i] mod 2 <> 0 then
      sum := sum + arr[i];


 write('Sum odd elements = ',sum);

  readln;


end.
