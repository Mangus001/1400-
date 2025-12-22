procedure PrintSymbols(Symbol: Char; Count: Integer);
var
  i: Integer;
begin
  for i := 1 to Count do
    Write(Symbol);
  WriteLn;
end;
