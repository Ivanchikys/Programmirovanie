program laba4.exc1.b;

uses
  Math;

var
  x, y: real;

begin
  x := 1;

  repeat
    y := 2.5 + ln(x) + cos(x);

    Writeln('x = ', x:0:2, '    y = ', y:4:2);

    x := x + 0.5;
  until x >= 10;

  readln;
end.
