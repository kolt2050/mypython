import json
import os

super_list_hotfix = dict()
super_list_release = dict()
super_list_develop = dict()

for root, dirs, files in os.walk("./mks-settings"):
    for filename in files:
        print("------------Считываем файл:\t " + filename + "\t -----------------")

        with open(f'./mks-settings/{filename}', 'r') as json_file:
            json_data = json.load(json_file)

        # Хотфиксы
        hotfix = json_data[0]['version']['hotfix']
        if hotfix:
            for i in hotfix:
                ver = json_data[0]['version']['hotfix'][i]['value']
                print("Hotfix " + i + " -> " + ver)
                super_list_hotfix.update({filename + " hotfix " + i: ver})
        else:
            print("Хотфиксов не было")

        # Релизные версии
        release = json_data[0]['version']['release']
        if release:
            for i in release:
                ver = json_data[0]['version']['release'][i]['value']
                print("Release " + i + " -> " + ver)
                super_list_release.update({filename + " release " + i: ver})
        else:
            print("Релизов не было")

        # Версии в разработке
        develop = json_data[0]['version']['develop']
        if develop:
            for i in develop:
                ver = json_data[0]['version']['develop'][i]['value']
                print("Develop " + i + " -> " + ver)
                super_list_develop.update({filename + " develop " + i: ver})
        else:
            print("Какая-то шляпа, develop отсутствует")

print("DICT Hotfix =====>", super_list_hotfix)
print("DICT Release =====>", super_list_release)
print("DICT Develop =====>", super_list_develop)

