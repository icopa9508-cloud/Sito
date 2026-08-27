# Python script to generate the complete TOPIC_MAPS JavaScript database
import json

# Let's define the comprehensive dataset for all subjects
subjects_data = {
    # IRELAND (ENGLISH)
    "spanish": {
        "Personal Descriptions & Daily Routines": [
            ("Rasgos Físicos y Carácter", "Vocabulary & Syntax", "Advanced adjectives describing physical appearance, moral traits, and nuanced personal attributes for natural self-presentation.", ["Vocabulary Spectrum Matrix", "Comparative Portrait Schema"]),
            ("Rutina Diaria y Horarios", "Temporal Expressions", "Structures for sequencing daily habits from morning waking to evening winding down, using reflexive verbs.", ["Daily Routine Timeline Flow", "Reflexive Verb Sequence"]),
            ("Relaciones Interpersonales", "Social Communication", "Phrasal verbs and idioms expressing friendship, trust, emotional support, and collaborative living.", ["Social Connection Network", "Conversation Flowchart"]),
            ("El Entorno de Vida", "Spatial Description", "Describing architectural layouts, residential spaces, urban surroundings, and living environments with prepositional accuracy.", ["Architectural Space Map", "Spatial Prepositions Grid"])
        ],
        "Verb Tenses (Present, Preterite & Imperfect)": [
            ("Pretérito Perfecto Compuesto", "Completed Past Actions", "Expressing recent past events with ongoing relevance to the present using 'haber + participio'.", ["Compound Tense Structure", "Present-Past Connection Graph"]),
            ("Pretérito Indefinido", "Definite Past Milestones", "Narrating distinct, punctual, completed historical events and precise chronological milestones.", ["Chronological Action Timeline", "Irregular Conjugation Grid"]),
            ("Pretérito Imperfecto", "Habitual & Descriptive Past", "Setting atmospheric background scenes, descriptions, ongoing past states, and recurring childhood memories.", ["Descriptive Scene Layering", "Aspectual Comparison Chart"]),
            ("Alternancia y Contraste", "Narrative Discourse", "Mastering the dynamic interplay between background description (Imperfecto) and interrupting sudden action (Indefinido).", ["Narrative Intersection Diagram", "Discourse Flow Schema"])
        ],
        "Family, Free Time & Passions": [
            ("Estructuras Familiares Modernas", "Sociology & Culture", "Contemporary terminology for diverse family units, generational bonds, and changing social dynamics in the Hispanic world.", ["Family Constellation Tree", "Sociological Spectrum"]),
            ("Aficiones y Ocio Activo", "Interests & Sports", "Lexicon for hobbies, athletic pursuits, outdoor activities, and leisure interests with dynamic verb collocations.", ["Activity Matrix Breakdown", "Leisure Time Distribution"]),
            ("Música y Expresión Artística", "Cultural Passions", "Discussing musical genres (flamenco, rock en español, reggaeton), instrumentation, and creative self-expression.", ["Artistic Expression Chart", "Cultural Influence Graph"]),
            ("Intercambio Conversacional", "Oral Interaction", "Conversational frameworks for negotiating plans, expressing preferences, debating ideas, and engaging in authentic dialogue.", ["Dialogue Strategy Flowchart", "Preference Spectrum"])
        ],
        "Social Media, Technology & School Life": [
            ("Impacto Digital y Redes Sociales", "Digital Ethics", "Analyzing smartphone ubiquity, algorithmic feeds, screen-time habits, and peer connectivity among youth.", ["Digital Connectivity Graph", "Platform Impact Metrics"]),
            ("Comparativa de Sistemas Escolares", "Comparative Education", "Contrasting the Irish Leaving Certificate modular system with the Spanish Bachillerato evaluation model.", ["Curricular Comparison Matrix", "Evaluation Pathway Schema"]),
            ("Huella Digital y Privacidad", "Cybersecurity & Identity", "Ethical considerations of online footprints, data protection, digital wellbeing, and authentic digital identity.", ["Privacy Shield Hierarchy", "Digital Footprint Flowchart"]),
            ("Debate y Argumentación", "Critical Discourse", "Constructing persuasive spoken and written arguments regarding technology's balance between isolation and community.", ["Argument Structure Model", "Pros vs. Cons Balance Scale"])
        ],
        "Spanish & Latin American Culture": [
            ("Semana Santa y Festividades", "Cultural Heritage", "Deconstructing sacred and secular traditions, processions, regional festivals, and social rituals across Spain.", ["Festival Calendar Matrix", "Ritual Iconography Map"]),
            ("Día de los Muertos", "Syncretism & Memory", "Exploring indigenous Mesoamerican beliefs merged with Catholic traditions, celebrating ancestral remembrance.", ["Cultural Syncretism Schema", "Altar Component Breakdown"]),
            ("Patrimonio Gastronómico", "Culinary Identity", "The social geography of tapas, regional agricultural specialties, Mediterranean diet principles, and dining etiquette.", ["Gastronomic Map of Spain", "Social Dining Flowchart"]),
            ("Diversidad Lingüística", "Dialectology", "Understanding regional co-official languages (Catalan, Galician, Basque) and continental Spanish variants.", ["Linguistic Distribution Map", "Dialectal Phonetic Grid"])
        ]
    },
    "business": {
        "Key Stakeholders & Conflict Resolution": [
            ("Internal vs. External Stakeholders", "Organizational Theory", "Categorizing primary actors from shareholders and staff to suppliers, lenders, local communities, and government bodies.", ["Stakeholder Mapping Grid", "Influence-Interest Matrix"]),
            ("Conflicting Interests & Trade-Offs", "Strategic Analysis", "Analyzing tensions between short-term shareholder profit demands and long-term employee welfare or environmental sustainability.", ["Conflict Dynamic Diagram", "Trade-Off Balance Model"]),
            ("Non-Legislative Resolution", "Negotiation Strategy", "Approaches including direct bilateral negotiation, conciliation, collective bargaining, and independent arbitration.", ["Resolution Protocol Pathway", "Negotiation Stage Pipeline"]),
            ("Legislative Frameworks", "Commercial Law", "Statutory mechanisms including industrial relations commissions, employment equality tribunals, and contract law safeguards.", ["Legal Redress Hierarchy", "Statutory Process Map"])
        ],
        "Enterprise in Action & Entrepreneurship": [
            ("Entrepreneurial Mindset & Traits", "Behavioral Economics", "Key attributes of visionary founders: calculated risk tolerance, proactivity, resilience, and lateral problem-solving.", ["Founder Attribute Spectrum", "Risk-Reward Curve"]),
            ("Opportunity Recognition & Ideation", "Innovation & Markets", "Identifying unmet consumer needs, exploiting market asymmetries, and converting innovative insights into commercial propositions.", ["Ideation Funnel Workflow", "Market Gap Analysis Schema"]),
            ("Intrapreneurship", "Corporate Innovation", "Fostering internal corporate venturing, employee initiative, and autonomous innovation within established corporate structures.", ["Intrapreneurship Flow Matrix", "Internal Innovation Loop"]),
            ("Feasibility & Prototyping", "Validation Process", "Conducting minimum viable product (MVP) testing, stress-testing operational constraints, and unit-economic validation.", ["MVP Validation Cycle", "Feasibility Checklist Chart"])
        ],
        "Business Planning & Market Research": [
            ("Business Plan Architecture", "Strategic Blueprint", "Structuring executive summaries, operational workflows, market analyses, and financial projections for venture capitalists.", ["Business Plan Structural Model", "Investor Deck Flowchart"]),
            ("Primary Market Research (Field)", "Direct Data Gathering", "Designing focus groups, consumer surveys, behavioral observation studies, and customer interviews.", ["Primary Methodology Matrix", "Sampling Distribution Diagram"]),
            ("Secondary Market Research (Desk)", "Aggregated Intelligence", "Leveraging industry census data, central statistics office reports, competitor filings, and commercial market databases.", ["Secondary Data Funnel", "Competitive Intelligence Grid"]),
            ("Market Segmentation & Positioning", "Target Marketing", "Segmenting consumer demographics, psychographics, and geographies to engineer distinctive perceptual brand positioning.", ["Perceptual Positioning Map", "Segmentation Triangle Model"])
        ],
        "Core Operations & Resource Management": [
            ("The Marketing Mix (4Ps & 7Ps)", "Commercial Strategy", "Harmonizing Product design, Pricing strategies (penetration, skimming), Placement logistics, and Promotion channels.", ["Marketing Mix Integration Matrix", "Pricing Strategy Curve"]),
            ("Human Resource Management (HRM)", "Workforce Dynamics", "Managing talent lifecycles: recruitment campaigns, skill training, performance appraisals, and motivational frameworks (Maslow/Herzberg).", ["Talent Lifecycle Workflow", "Motivation Spectrum Chart"]),
            ("Production Systems & Quality Control", "Operational Excellence", "Contrasting Job, Batch, and Flow production; implementing Total Quality Management (TQM) and Just-in-Time (JIT) protocols.", ["Production Continuum Schema", "Quality Control Loop Diagram"]),
            ("Sustainable Supply Chain Management", "Logistics & ESG", "Ethical sourcing, carbon-footprint reduction, warehouse inventory optimization, and circular economy integration.", ["Circular Supply Chain Loop", "Logistics Flow Matrix"])
        ],
        "Risk Management & Leadership Styles": [
            ("Commercial & Operational Risk Assessment", "Enterprise Risk", "Systematic identification of liability hazards, market volatility, cyber vulnerabilities, and supply interruptions.", ["Risk Heatmap Matrix", "Vulnerability Impact Curve"]),
            ("Insurance & Loss Minimization", "Financial Protection", "Principles of indemnity, utmost good faith, insurable interest, subrogation, and policy portfolio balancing.", ["Insurance Principles Triangle", "Loss Mitigation Pipeline"]),
            ("Leadership Paradigms", "Management Theory", "Evaluating Autocratic, Democratic, and Laissez-Faire leadership profiles across routine operations and acute turnaround crises.", ["Leadership Style Spectrum", "Decision Authority Matrix"]),
            ("Change Management & Crisis Response", "Organizational Agility", "Leading teams through restructuring, technological transitions, and emergency communications with empathy and clarity.", ["Crisis Communication Pathway", "Change Curve Model"])
        ]
    }
}

print("Base schema defined successfully.")
