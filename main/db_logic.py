import pyodbc
import json
import os
from datetime import datetime

DB_CONFIG = {
    "server": os.getenv("DB_SERVER", "localhost"),
    "database": os.getenv("DB_NAME", "ResumeDB"),
    "driver": "{ODBC Driver 17 for SQL Server}"
}

CONNECTION_STRING = f'DRIVER={DB_CONFIG["driver"]};SERVER={DB_CONFIG["server"]};DATABASE={DB_CONFIG["database"]};Trusted_Connection=yes;'
MASTER_CONNECTION_STRING = f'DRIVER={DB_CONFIG["driver"]};SERVER={DB_CONFIG["server"]};DATABASE=master;Trusted_Connection=yes;'

def get_connection():
    try:
        return pyodbc.connect(CONNECTION_STRING)
    except Exception as e:
        return None

def execute_db_init():
    try:
        master_conn = pyodbc.connect(MASTER_CONNECTION_STRING, autocommit=True)
        cursor = master_conn.cursor()
        
        cursor.execute(f"SELECT name FROM sys.databases WHERE name = '{DB_CONFIG['database']}'")
        if not cursor.fetchone():
            print(f"Database '{DB_CONFIG['database']}' not found. Attempting to create...")
            cursor.execute(f"CREATE DATABASE [{DB_CONFIG['database']}]")
            print(f"Successfully created database '{DB_CONFIG['database']}'.")
        
        master_conn.close()
    except Exception as e:
        print(f"Warning: Could not verify/create database '{DB_CONFIG['database']}': {e}")
        return

    conn = get_connection()
    if not conn:
        print(f"Error: Could not connect to database '{DB_CONFIG['database']}' after creation attempt.")
        return
    
    cursor = conn.cursor()
def save_analysis_to_db(result):
    conn = get_connection()
    if not conn:
        return False
    
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO ResumeAnalyses (candidate_name, word_count, match_score, matched_skills, entities_json, warnings_json)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    cursor.execute(insert_query, (
        result["candidate_name"],
        result["word_count"],
        result["match_score"],
        ",".join(result["matched_skills"]),
        json.dumps(result["entities"]),
        json.dumps(result["warnings"])
    ))
    conn.commit()
    conn.close()
    return True

def fetch_all_analyses():
    conn = get_connection()
    if not conn:
        return []
    
    cursor = conn.cursor()
    cursor.execute("SELECT candidate_name, word_count, match_score, matched_skills, entities_json, warnings_json, analysis_date FROM ResumeAnalyses ORDER BY analysis_date DESC")
    rows = cursor.fetchall()
    
    analyses = []
    for row in rows:
        analyses.append({
            "candidate_name": row[0],
            "word_count": row[1],
            "match_score": row[2],
            "matched_skills": row[3].split(",") if row[3] else [],
            "entities": json.loads(row[4]),
            "warnings": json.loads(row[5]),
            "date": row[6].isoformat()
        })
    conn.close()
    return analyses
