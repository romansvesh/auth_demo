1) Открыть https://auth-demo.aerobatic.io/
2) Нажать кнопку ""Standart auth""
3) Пройти авторизацию (логин и пароль ""aerobatic"")
Уточню по поводу практики, на Selenium достаточно выполнить третий шаг. Не забудьте добавить ожидаемый результат (проверку, что мы реально авторизовались).
Т.е. в тесте можно сразу открывать url https://auth-demo.aerobatic.io/protected-standard/, без промежуточных нажиманий на "Standart auth"

Use Python 3.6.3

geckodriver.exe is require in root folder