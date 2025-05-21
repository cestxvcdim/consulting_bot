def get_file_name(cb_data: str) -> str:
    match cb_data:
        case 'allowance':
            return 'Электронное пособие для родителей.pdf'
        case 'article1':
            return 'Агрессивный ребенок.docx'
        case 'article2':
            return 'Давай дружить.docx'
        case 'article3':
            return 'Дети и гаджеты.docx'
        case 'article4':
            return 'Дизграфия.docx'
        case 'article5':
            return 'Как воспитать в ребенке здоровую уверенность.docx'
        case 'article6':
            return 'Как помочь подростку.docx'
        case 'article7':
            return 'Мой ребенок готов к школе.docx'
        case 'article8':
            return 'Причины самоповреждающего поведения.docx'
        case 'article9':
            return 'Ребенок остро реагирует на критику.docx'
        case 'article10':
            return 'Роль отца в воспитании девочки.docx'
        case 'article11':
            return 'Что такое психосоматика.docx'
        case _:
            return cb_data
