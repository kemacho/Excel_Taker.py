import os
import glob
from tqdm import tqdm
import shutil


# Сертификаты 2023 года
Num_SERT =  [201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215,
    216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230,
    231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245,
    246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
    261, 262, 263, 264]

folder_names = [
    "201 - АО КЭС им. Пискунова (01.02.2023)",
    "202 - Башкирэнерго-БЭС (31.03.2023)",
    "203 - Башкирэнерго-СЭС (31.03.2023)",
    "204 - Башкирэнерго-БцЭС (31.03.2023)",
    "205 - Сахалинэнерго (28.05.2023)",
    "206 - Башкирэнерго-СВЭС (30.04.2023)",
    "207 - Башкирэнерго-СВЭС (30.04.2023)",
    "208 - Башкирэнерго-СЭС (30.04.2023)",
    "209 - Башкирэнерго-УГЭС (30.04.2023)",
    "210 - Башкирэнерго-ЦЭС (30.04.2023)",
    "211 - Башкирэнерго-ЦЭС (30.04.2023)",
    "212 - Башкирэнерго-БЭС (30.04.2023)",
    "213 - Башкирэнерго-КЭС (30.04.2023)",
    "214 - Башкирэнерго-СЭС (30.05.2023)",
    "215 - Башкирэнерго-ЦЭС (30.05.2023)",
    "216 - Башкирэнерго-СВЭС (30.05.2023)",
    "217 - Башкирэнерго-ИЭС (30.05.2023)",
    "218 - Башкирэнерго-БцЭС (30.05.2023)",
    "219 - Прионежская СК (23.06.2023)",
    "220 - Башкирэнерго-БЭС (29.06.2023)",
    "221 - Башкирэнерго-СВЭС (29.06.2023)",
    "222 - Башкирэнерго-СЭС (29.06.2023)",
    "223 - Башкирэнерго-ИЭС (29.06.2023)",
    "224 - Башкирэнерго-КЭС (29.06.2023)",
    "225 - ОЭК-Ростов (30.06.2023)",
    "226 - Камчатскэнерго ЦЭС (28.07.2023)",
    "227 - Башкирэнерго-УГЭС (28.07.2023) ок",
    "228 - Башкирэнерго-УГЭС (28.07.2023) ок",
    "229 - Башкирэнерго-БцЭС (28.07.2023) ок",
    "230 - Башкирэнерго-ЦЭС (28.07.2023) ок",
    "231 - Башкирэнерго-ИЭС (28.07.2023) ок",
    "232 - Башкирэнерго-ОЭС (28.07.2023) ок",
    "233 - Башкирэнерго-ОЭС (28.07.2023) ок",
    "234 - КЭС им.Пискунова (25.08.2023)",
    "235 - Вологодский ф-л Россети С-З, ВУЭС (29.08.2023)",
    "236 - Вологодский ф-л Россети С-З, ЧЭС (29.08.2023)",
    "237 - Уральские ЭС (29.08.2023)",
    "238 - Уральские ЭС (29.08.2023)",
    "239 - Башкирэнерго-КЭС (30.08.2023) ок",
    "240 - Башкирэнерго-СЭС (30.08.2023) ок",
    "241 - Башкирэнерго-УГЭС (30.08.2023) ок",
    "242 - Башкирэнерго-ЦЭС (30.08.2023) ок",
    "243 - Башкирэнерго-ОЭС (30.08.2023) ок",
    "244 - Вологодский ф-л Россети С-З, ВЭС (11.09.2023)",
    "245 - Оборонэнерго-Камч. (28.09.2023)",
    "246 - Башкирэнерго-ЦЭС (29.09.2023) ок",
    "247 - Карельский ф-л Россети С-З, ЗКЭС (29.09.2023)",
    "248 - Карельский ф-л Россети С-З, CЭС (17.10.2023)",
    "249 - Карельский ф-л Россети С-З, ЮКЭС (23.10.2023)",
    "250 - Промэнергосбыт Новомосковск (25.10.2023)",
    "251 - Башкирэнерго-НЭС (30.10.2023) ок",
    "252 - Башкирэнерго-НЭС (30.10.2023) ок",
    "253 - Башкирэнерго-НЭС (30.10.2023) ок",
    "254 - Башкирэнерго-ОЭС (30.10.2023) ок",
    "255 - Волгодонск (13.11.2023)",
    "256 - Ленэнерго, CЭС (16.11.2023)",
    "257 - СМЗ, Самара (20.11.2023)",
    "258 - Ленэнерго, КС (24.11.2023)",
    "259 - Ленэнерго - КнЭС (13.12.2023)",
    "260 - Салют-Самара (13.12.2023)",
    "261 - Оборонэнерго-Вологда (13.12.2023)",
    "262 - Жилкомхоз (29.12.2023)",
    "263 - Агроимпульс-Кгд (29.12.2023) нет скана",
    "264 - Энергосеть-Кгд (29.12.2023) нет скана"
]


for i in tqdm(range(55, len(Num_SERT))):

    name = folder_names[i]
    pathSI = rf'\\192.168.34.9\линвит\ПОЛЬЗОВАТЕЛИ\USER49\!Сертификаты_2023\{name}\СИ'
    pathSRC = rf'\\192.168.34.9\линвит\ОБЩИЕ ДОКУМЕНТЫ\ЛИНВИТ\12. Обмен файлами\1. Чурсанов Андрей\Сертификаты ЛИНВИТ\_Сертификаты-2023 (201-264)\{name}'

    contents = os.listdir(pathSRC)

    for contents in contents:
        source_path = os.path.join(pathSRC, contents)
        dest_path = os.path.join(pathSI, contents)

        if os.path.isfile(source_path):
            shutil.copy2(source_path, dest_path)
            print(f"Файл скопирован: {source_path} -> {dest_path}")
        elif os.path.isdir(source_path):

            shutil.copytree(source_path, dest_path, dirs_exist_ok=True)
            print(f"Папка скопирована: {source_path} -> {dest_path}")
        else:
            print(f"Неизвестный тип файла: {source_path}")

    print(contents, '\n')