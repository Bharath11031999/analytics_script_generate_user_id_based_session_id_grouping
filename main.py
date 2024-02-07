import threading
from datetime import datetime

from cron_jobs.user_id_layer_analysis import user_session_layer_executor
from cron_utils.logging import setup_logging
from database.mongodb_connector import session
from cron_utils.load_env import get_env


def user_session_analysis_layer_executor():
    logger = setup_logging('user_session_analysis_layer', env=get_env())
    logger.info("inside the user_session_analysis_layer_executor()")
    user_names = session.user_collection.find({"userType": "customer"}, {"_id": 0, "databaseName": 1})
    # user_names = [{'databaseName': 'Bharath223'}]
    threads = []

    for user_name in user_names:
        thread = threading.Thread(target=user_session_layer_executor, args=(user_name, logger))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start_time = datetime.now()
    user_session_analysis_layer_executor()
    end_time = datetime.now()
    print("total time took for execution for user_session_analysis_layer_executor(): {}".format(end_time - start_time))
