from main.db_logic import execute_db_init, save_analysis_to_db, fetch_all_analyses

def init_db():
    execute_db_init()

def save_analysis(result):
    return save_analysis_to_db(result)

def get_all_analyses():
    return fetch_all_analyses()
