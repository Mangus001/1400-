procedure PrintLineWithSymbols(Symbol: Char; Count: Integer);
begin
  for i := 1 to Count do
    Write(Symbol, ' ');
  WriteLn;
end;

procedure DrawTriangleAscending;
var
  i: Integer;
begin
  for i := 1 to 10 do
    PrintSymbols('*', i);
end;

procedure DrawTriangleDescending;
var
  i: Integer;
begin
  for i := 10 downto 1 do
    PrintSymbols('*', i);
end;
