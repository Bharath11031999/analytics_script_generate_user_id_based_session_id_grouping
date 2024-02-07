pipe_line_1 = [
    {
        '$project': {
            'userId': {'$arrayElemAt': ['$events.attributes.userId', 0]},
            'firstEventDateTime': 1,
            '_id': 1
        }
    },
    {
        '$group': {
            '_id': '$userId',
            'data': {
                '$push': {
                    'sessionId': '$_id',
                    'eventDateTime': '$firstEventDateTime'
                }
            }
        }
    }
]
