pipe_line_1 = [
    {
        '$project': {
            'userId': {'$arrayElemAt': ['$events.attributes.userId', 0]},
            'firstEventDateTime': 1,
            '_id': 1,
            'document': '$$ROOT'
        }
    },
    {
        '$group': {
            '_id': '$userId',
            'data': {
                '$push': {
                    'sessionId': '$_id',
                    'eventDateTime': '$firstEventDateTime',
                    'document': '$$ROOT'
                }
            }
        }
    }
]
