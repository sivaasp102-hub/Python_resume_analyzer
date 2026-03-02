METHOD: POST ENDPOINT:/analyze-resume
1) INPUT TEXT :
Abhi is a highly skilled Senior Software Engineer with a deep expertise in modern backend technologies. He is proficient in Python and has extensive experience building web services using Flask. Abhi is also a master of SQL for database management and utilizes Pandas for complex data analysis tasks. Currently based in Chennai, he has successfully delivered numerous high-quality projects for international clients over the last eight years. Abhi is passionate about writing clean, maintainable code and mentoring junior developers in his team. He is looking for a challenging role that allows him to leverage his full-stack capabilities in a dynamic environment.

OUTPUT:
{
    "candidate_name": "abhi",
    "entities": {
        "locations": [
            "Chennai"
        ],
        "organizations": []
    },
    "match_score": 100.0,
    "matched_skills": [
        "Flask",
        "Pandas",
        "SQL",
        "Python"
    ],
    "warnings": [],
    "word_count": 101
}

2) INPUT TEXT:
Deepz.
Experience in managing large teams and coordinating logistics for national events.
Strong background in administration, project management, and public speaking.
Based in Bangalore, worked for 10 years in the corporate sector.
Passionate about literature and history.
Always looking for new challenges in the field of arts and culture.
I have no technical programming skills but I am a fast learner.
   OUTPUT:
   {
    "candidate_name": "deepz",
    "entities": {
        "locations": [
            "Bangalore"
        ],
        "organizations": []
    },
    "match_score": 0.0,
    "matched_skills": [],
    "warnings": [
        "No skills matched"
    ],
    "word_count": 61
}

3) INPUT TEXT:
Seshan is a renowned Wildlife Photographer and Travel Documentarian with a passion for capturing the beauty of the natural world. He has traveled to over fifty countries, documenting rare species and diverse ecosystems for various international publications. Seshan is an expert in high-end camera equipment, digital post-processing, and visual storytelling through powerful imagery. He has hosted several successful photography exhibitions and workshops for aspiring artists. Seshan is looking for new collaborations in the media and environmental conservation sectors to continue his work in visual advocacy.

OUTPUT:
{
    "candidate_name": "seshan",
    "entities": {
        "locations": [],
        "organizations": []
    },
    "match_score": 0.0,
    "matched_skills": [],
    "warnings": [
        "No skills matched",
        "No location detected"
    ],
    "word_count": 85
}

4) INPUT FILE:
FILE.DOCX

OUTPUT:
{
    "error": "Only .txt files are allowed"
}


METHOD : GET    ENDPOINT : analyses

OUTPUT:

[
    {
        "candidate_name": "seshan",
        "date": "2026-03-02T12:23:30.170000",
        "entities": {
            "locations": [],
            "organizations": []
        },
        "match_score": 0.0,
        "matched_skills": [],
        "warnings": [
            "No skills matched",
            "No location detected"
        ],
        "word_count": 85
    },
    {
        "candidate_name": "deepz",
        "date": "2026-03-02T12:22:11.370000",
        "entities": {
            "locations": [
                "Bangalore"
            ],
            "organizations": []
        },
        "match_score": 0.0,
        "matched_skills": [],
        "warnings": [
            "No skills matched"
        ],
        "word_count": 61
    },
    {
        "candidate_name": "abhi",
        "date": "2026-03-02T12:20:58.173000",
        "entities": {
            "locations": [
                "Chennai"
            ],
            "organizations": []
        },
        "match_score": 100.0,
        "matched_skills": [
            "Flask",
            "Pandas",
            "SQL",
            "Python"
        ],
        "warnings": [],
        "word_count": 101
    },
    {
        "candidate_name": "deepan",
        "date": "2026-03-02T11:13:57.963000",
        "entities": {
            "locations": [],
            "organizations": []
        },
        "match_score": 50.0,
        "matched_skills": [
            "Flask",
            "Python"
        ],
        "warnings": [
            "No location detected"
        ],
        "word_count": 82
    },
    {
        "candidate_name": "lakshi",
        "date": "2026-03-02T11:13:37.847000",
        "entities": {
            "locations": [
                "Chennai"
            ],
            "organizations": []
        },
        "match_score": 100.0,
        "matched_skills": [
            "Flask",
            "Pandas",
            "SQL",
            "Python"
        ],
        "warnings": [],
        "word_count": 91
    },
    {
        "candidate_name": "Sivasankarapandi S Java / C",
        "date": "2026-03-01T22:14:52.993000",
        "entities": {
            "locations": [],
            "organizations": [
                "Infosys\r\nSpringboard\r\nCertificate of Completion for CCNA Module",
                "Tableau\r\nCERTIFICATION\r\nCertificate of Completion for CCNA Module -1 05/2024",
                "MERN Stack",
                "Tableau\r\nINTERNSHIP\r\nEDUCATION\r\nSKILLS\r\nBachelor of Engineering : Information Technology\r\nJunior Web Developer",
                "CNN",
                "Student Attendance Management System",
                "Cisco\r\nNetworking Academy\r\nCertificate of Completion for Al primer Certificate",
                "Interface",
                "Madurai",
                "GAN & CNN",
                "Tirumangalam",
                "CRUD",
                "Convolutional Neural Networks",
                "Professional Development Courses",
                "NLP",
                "TB",
                "GPA",
                "Language Translator",
                "IP",
                "MSME",
                "AI/DL Developer",
                "Engg & Tech|",
                "CSS",
                "Cisco\r\nNetworking Academy\r\nPROJECTS\r\nPlant Disease Prediction"
            ]
        },
        "match_score": 25.0,
        "matched_skills": [
            "Python"
        ],
        "warnings": [
            "No location detected",
            "Low skill diversity (only 1 skill detected)"
        ],
        "word_count": 336
    },
    {
        "candidate_name": "Skill",
        "date": "2026-03-01T22:12:24.613000",
        "entities": {
            "locations": [
                "Mumbai"
            ],
            "organizations": []
        },
        "match_score": 25.0,
        "matched_skills": [
            "Python"
        ],
        "warnings": [
            "Low skill diversity (only 1 skill detected)"
        ],
        "word_count": 139
    },
    {
        "candidate_name": "Dhanush",
        "date": "2026-03-01T22:12:09.197000",
        "entities": {
            "locations": [
                "Chennai"
            ],
            "organizations": [
                "SQL Python"
            ]
        },
        "match_score": 50.0,
        "matched_skills": [
            "SQL",
            "Python"
        ],
        "warnings": [
            "Resume is too short (< 30 words)"
        ],
        "word_count": 25
    },
    {
        "candidate_name": "Chennai",
        "date": "2026-03-01T22:11:18.200000",
        "entities": {
            "locations": [
                "Chennai"
            ],
            "organizations": [
                "SQL Python"
            ]
        },
        "match_score": 50.0,
        "matched_skills": [
            "SQL",
            "Python"
        ],
        "warnings": [
            "Resume is too short (< 30 words)"
        ],
        "word_count": 23
    },
    {
        "candidate_name": "Shreya.",
        "date": "2026-03-01T22:10:13.120000",
        "entities": {
            "locations": [
                "Hyderabad",
                "India"
            ],
            "organizations": [
                "Experienced Data Scientist",
                "Hyderabad"
            ]
        },
        "match_score": 100.0,
        "matched_skills": [
            "Pandas",
            "SQL",
            "Flask",
            "Python"
        ],
        "warnings": [],
        "word_count": 128
    },
    {
        "candidate_name": "Unknown",
        "date": "2026-03-01T22:05:27.510000",
        "entities": {
            "locations": [
                "Hyderabad",
                "India",
                "Flask",
                "Python"
            ],
            "organizations": [
                "Hyderabad",
                "SQL",
                "Experienced Data Scientist"
            ]
        },
        "match_score": 100.0,
        "matched_skills": [
            "SQL",
            "Pandas",
            "Flask",
            "Python"
        ],
        "warnings": [],
        "word_count": 128
    },
    {
        "candidate_name": "Unknown",
        "date": "2026-03-01T22:04:11.030000",
        "entities": {
            "locations": [],
            "organizations": []
        },
        "match_score": 0.0,
        "matched_skills": [],
        "warnings": [
            "Resume is too short (< 30 words)",
            "No skills matched",
            "No location detected"
        ],
        "word_count": 2
    }
]



DB_SS:

<img width="1908" height="1014" alt="image" src="https://github.com/user-attachments/assets/e12b6966-93bb-473b-8186-74abeeb2af05" />
