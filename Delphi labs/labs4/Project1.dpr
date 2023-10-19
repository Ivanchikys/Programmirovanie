program laba4;

var
  t, y: real;

begin
  t := 1;
  while t <= 3 do begin

    if t <= 3 then
      y := Sin(3 * t) + t / 2
    else
      y := Cos(2 * t - 3 / t);

    Writeln(t:0:2, '    y = ', y:0:1);

    t := t + 0.1;
  end;

  readln;
end.

