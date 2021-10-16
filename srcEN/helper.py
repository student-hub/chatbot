from datetime import date

def get_entities(entities):
    eventEntity = ''
    typeEventEntity = 'course'

    max_confidence_event = max((ent['confidence_entity'] for ent in entities if ent['entity'] == "event"), default=None)
    max_confidence_typeEvent = max((ent['confidence_entity'] for ent in entities if ent['entity'] == "typeEvent"), default=None)

    if max_confidence_event is not None:
        for ent in entities:
            if ent['confidence_entity'] == max_confidence_event and ent['entity'] == 'event':
                eventEntity = ent['value']
                break

    if max_confidence_typeEvent is not None:
        for ent in entities:
            if ent['confidence_entity'] == max_confidence_event and ent['entity'] == 'typeEvent':
                typeEventEntity = ent['value']
                break

    return eventEntity, typeEventEntity

def compute_event_name(classFields, eventEntity):
    
    event = "L" if classFields[0] == "BSc" else "M"
    words = classFields[3].split('-')
    year = words[0]
    serie = words[1]

    today = date.today()
    formatted_today = (today.strftime("%B %d, %Y")).split(' ')
    month = formatted_today[0]

    if month in ["February", "March", "April", "May", "June"]:
        event = event + "-A" + year + "-S2"
    else:
        event = event + "-A" + year + "-S1"

    if(len(eventEntity) < 6):
        event = event + "-" + eventEntity.upper() + "-" + serie
    else:
        abreviation = ""
        for x in eventEntity.split():
            if x[0].isalpha():
                abreviation = abreviation + x[0]
        if(eventEntity[-1].isnumeric()):
            abreviation = abreviation + eventEntity[-1]
        event = event + "-" + abreviation.upper() + "-" + serie

    return event

def get_type_event(type):
    types = {
        "course": "lecture",
        "seminar": "seminar",
        "laboratory": "lab",
        "lab":"lab"
    }
    if types.get(type) is not None:
        return types.get(type)
    else:
        return "unknown-ev"

def identify_student(classFields):
    sr = classFields[3]
    group = classFields[4]
    semigroup = classFields[5]

    return sr, group, semigroup