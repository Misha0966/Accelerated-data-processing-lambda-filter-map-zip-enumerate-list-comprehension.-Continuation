# Программа удаляющая из текса все слова содержащие абв

def delete_abc(text: str):
    return ' '.join(list(filter(lambda x: 'абв' not in x, text.split()))) # Реализация через filter и lambda

print(delete_abc("Мороз и солнце день чудесный ещёабв абвты дремабвлешь абвдруг прелестныйабв"))