from datetime import date

hoje = date.today()
print(hoje) # imprime a data atual no formato aaaa-mm-dd

from datetime import time

hora_atual = time.now()
print(hora_atual) # imprime o horário atual no formato hh:mm:ss

from datetime import datetime

agora = datetime.now()
print(agora) # imprime a data e o horário atual no formato aaaa-mm-dd hh:mm:ss

from datetime import timedelta

# somando um dia à data atual
amanha = hoje + timedelta(days=1)
print(amanha)

# subtraindo duas horas do horário atual
horario_anterior = hora_atual - timedelta(hours=2)
print(horario_anterior)

# calculando a diferença de tempo entre dois horários
diferenca = hora_atual - horario_anterior
print(diferenca) # imprime a diferença de tempo em segundos


from datetime import date, time, datetime

# comparando duas datas
data1 = date(2022, 3, 10)
data2 = date(2023, 3, 10)
if data1 < data2:
    print("data1 é anterior a data2")
else:
    print("data1 é posterior a data2")

# comparando dois horários
horario1 = time(10, 30, 0)
horario2 = time(12, 0, 0)
if horario1 < horario2:
    print("horario1 é anterior a horario2")
else:
    print("horario1 é posterior a horario2")

# comparando duas datas e horários
datetime1 = datetime(2022, 3, 10, 10, 30, 0)
datetime2 = datetime(2023, 3, 10, 12, 0, 0)
if datetime1 < datetime2:
    print("datetime1 é anterior a datetime2")
else:
    print("datetime1 é posterior a datetime2")
