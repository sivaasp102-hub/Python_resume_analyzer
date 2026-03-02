import spacy
import re
from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
from simstring.measure.cosine import CosineMeasure
from simstring.database.dict import DictDatabase
from simstring.searcher import Searcher


nlp = spacy.load("en_core_web_sm")

REQUIRED_SKILLS = ["Python", "Flask", "SQL", "Pandas"]

def preprocess_text(text):
    doc = nlp(text)
    tokens = [
        token.lemma_.lower()
        for token in doc
        if not token.is_stop and not token.is_punct
    ]
    return tokens

def extract_text_count(text):
    words = text.split()
    return len(words)

def match_skills(text, required_skills=REQUIRED_SKILLS):
    matched_skills = []
    text_lower = text.lower()
    
    db = DictDatabase(CharacterNgramFeatureExtractor(1))
    for word in text_lower.split():
        clean_word = re.sub(r'[^\w\s]', '', word)
        if clean_word:
            db.add(clean_word)
            
    searcher = Searcher(db, CosineMeasure())
    
    for skill in required_skills:
        skill_lower = skill.lower()
        matches = searcher.search(skill_lower, 0.85)
        if matches:
            matched_skills.append(skill)
            
    return list(set(matched_skills))

def extract_candidate_name(text, doc):
   
    technical_terms = [s.lower() for s in REQUIRED_SKILLS] + ["pythn", "falsk", "pandas", "sql", "flask", "python", "developer", "engineer", "resume", "summary", "experience", "senior", "junior"]
    
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text.strip()
            if 2 < len(name) < 30 and name.lower() not in technical_terms:
                if not any(char.isdigit() for char in name):
                    return name
    
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    if lines:
        first_line = lines[0]
        if 2 < len(first_line) < 40 and first_line.lower() not in technical_terms:
            return first_line
        first_sentence = first_line.split('.')[0].strip()
        if 2 < len(first_sentence) < 30 and first_sentence.lower() not in technical_terms:
            return first_sentence
        first_word = first_line.split()[0].replace('.', '').replace(',', '').strip()
        if 2 < len(first_word) < 20 and first_word.lower() not in technical_terms:
            return first_word
            
    return "Unknown"

def extract_entities(text, doc, matched_skills):
    entities = {
        "locations": [],
        "organizations": []
    }
    
    exclude_list = [s.lower() for s in matched_skills]
    noise_labels = ["experienced", "scientist", "developer", "engineer", "resume", "summary", "senior", "junior", "python", "flask", "sql", "pandas", "pythn", "falsk"]
    names_to_exclude = ["seshan", "deepan", "gowshik", "bommu", "abhi", "lakshi", "shreya", "sharmi", "dhanush", "deepz", "siva", "praka"]

    for ent in doc.ents:
        cleaned_ent = ent.text.strip().lower()
        
        if cleaned_ent in exclude_list or cleaned_ent in noise_labels:
            continue
            
        if ent.label_ in [ "GPE", "LOC" ]:
            if cleaned_ent not in names_to_exclude:
                entities["locations"].append(ent.text)
        elif ent.label_ == "ORG":
            if len(cleaned_ent) < 50 and cleaned_ent not in exclude_list:
                entities["organizations"].append(ent.text)
            
    indian_cities = ["Chennai", "Bangalore", "Mumbai", "Delhi", "Hyderabad", "Pune", "Kolkata"]
    for city in indian_cities:
        if re.search(rf'\b{city}\b', text, re.IGNORECASE):
            entities["locations"].append(city)
            
    entities["locations"] = list(set(entities["locations"]))
    entities["organizations"] = list(set(entities["organizations"]))
    
    return entities

def validate_resume(text, matched_skills, entities):
    warnings = []
    word_count = extract_text_count(text)
    
    if word_count < 30:
        warnings.append("Resume is too short (< 30 words)")
    if not matched_skills:
        warnings.append("No skills matched")
    if not entities["locations"]:
        warnings.append("No location detected")
    if len(matched_skills) == 1:
        warnings.append("Low skill diversity (only 1 skill detected)")
        
    return warnings

def run_resume_analysis(text):
    tokens = preprocess_text(text)
    preprocessed_text = " ".join(tokens)
    
    doc = nlp(preprocessed_text)
    word_count = extract_text_count(text)
    matched_skills = match_skills(preprocessed_text)
    entities = extract_entities(preprocessed_text, doc, matched_skills)
    warnings = validate_resume(preprocessed_text, matched_skills, entities)
    candidate_name = extract_candidate_name(preprocessed_text, doc)
    
    total_required = len(REQUIRED_SKILLS)
    match_score = (len(matched_skills) / total_required) * 100 if total_required > 0 else 0
    
    return {
        "candidate_name": candidate_name,
        "word_count": word_count,
        "matched_skills": matched_skills,
        "match_score": match_score,
        "entities": entities,
        "warnings": warnings
    }
