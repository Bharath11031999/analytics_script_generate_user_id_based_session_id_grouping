from database.mongodb_connector import session
from cron_utils.piple_line import pipe_line_1


def user_session_layer_executor(user_name, logger):
    logger.info("inside user_session_layer_executor(): user_name: {}".format(user_name))

    try:
        dbn = user_name["databaseName"]
        user_data_base = session.client[dbn]
        user_session_layer = user_data_base[session.user_session_layer]
        session_layer = user_data_base[session.session_layer]
        result = session_layer.aggregate(pipe_line_1)
        existing_ids = set(document['_id'] for document in user_session_layer.find({}, {'_id': 1}))
        for doc in result:
            if doc['_id'] not in existing_ids:
                user_session_layer.insert_one(doc)
            else:
                user_session_layer.update_one({'_id': doc['_id']}, {'$set': doc})

    except Exception as e:
        logger.error("inside master_layer_executor() exception e: {}".format(str(e)))
        return str(e), 400
