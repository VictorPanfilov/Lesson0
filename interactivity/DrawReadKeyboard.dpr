{$APPTYPE CONSOLE}
program DrawReadKeyboard;
 uses Winapi.Windows;

 var
  h: THandle;
  x: dword;
  e: TInputRecord;

 // Получить символ нажатой клавиши. Если ничего не нажато, то возвращается #0.
 // Используется для добавления интерактивности в консольное приложение,
 // например для получения информации о текущем состоянии работающей программы.
 function ReadKeyboard: char;
  begin
   Result:=#0;
   repeat
    GetNumberOfConsoleInputEvents(h, x);
    if x=0 then exit;
    ReadConsoleInput(h, e, 1, x);
    if (e.EventType = KEY_EVENT) and e.Event.KeyEvent.bKeyDown then
     begin
      Result:= e.Event.KeyEvent.UnicodeChar;
      exit
     end
   until false
  end;

 var
  c: char;

BEGIN
  h:= GetStdHandle(STD_INPUT_HANDLE);
  FlushConsoleInputBuffer(h);

  repeat
   c:= ReadKeyboard;
   if c <> #0 then writeln(ord(c))
  until false

END.
