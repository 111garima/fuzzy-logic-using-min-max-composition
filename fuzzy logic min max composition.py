import numpy as np

# Function for fuzzy relation composition using min-max composition
def fuzzy_relation_composition(relation1, relation2):
    result = np.zeros((relation1.shape[0], relation2.shape[1]))
    for i in range(relation1.shape[0]):
        for j in range(relation2.shape[1]):
            result[i][j] = np.max([np.min([relation1[i][k], relation2[k][j]]) for k in range(relation1.shape[1])])
    return result

# Function to evaluate a candidate
def evaluate_candidate(criteria, candidate_profile, fuzzy_relations):

    # Convert candidate profile to a 1D array
    candidate_vector = np.array([candidate_profile[criterion] for criterion in criteria])

    # Combine fuzzy relations using min-max composition
    combined_relation = fuzzy_relations[criteria[0]]
    for criterion in criteria[1:]:
        combined_relation = fuzzy_relation_composition(combined_relation, fuzzy_relations[criterion])

    # Per-criterion evaluation using min-max composition
    overall_suitability = []
    for idx, criterion in enumerate(criteria):
        score = candidate_profile[criterion]
        relation = fuzzy_relations[criterion]
        suitability = np.max(np.minimum(score, relation))
        overall_suitability.append(suitability)

    # Return overall suitability as a vector for all criteria
    return np.array(overall_suitability)

# Example usage
criteria = ["experience", "education", "interview_performance", "technical_skills", "teamwork", "communication", "problem_solving", "leadership"]

candidate_profile = {
    "experience": 0.8,
    "education": 0.6,
    "interview_performance": 0.9,
    "technical_skills": 0.7,
    "teamwork": 0.4,
    "communication": 0.5,
    "problem_solving": 0.6,
    "leadership": 0.1,
}

fuzzy_relations = {
    "experience": np.array([[0.2, 0.4, 0.6], [0.3, 0.5, 0.7], [0.4, 0.6, 0.8]]),
    "education": np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6], [0.3, 0.5, 0.7]]),
    "interview_performance": np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6], [0.3, 0.5, 0.7]]),
    "technical_skills": np.array([[0.2, 0.4, 0.6], [0.3, 0.5, 0.7], [0.4, 0.6, 0.8]]),
    "teamwork": np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6], [0.3, 0.5, 0.7]]),
    "communication": np.array([[0.2, 0.4, 0.6], [0.3, 0.5, 0.7], [0.4, 0.6, 0.8]]),
    "problem_solving": np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6], [0.3, 0.5, 0.7]]),
    "leadership": np.array([[0.2, 0.4, 0.6], [0.3, 0.5, 0.7], [0.4, 0.6, 0.8]]),
}

overall_suitability = evaluate_candidate(criteria, candidate_profile, fuzzy_relations)
print("Overall suitability:", overall_suitability)
