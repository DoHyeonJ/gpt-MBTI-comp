def calculate_compatibility(mbti1, mbti2):
    score = 0

    # Extraversion (E) - Introversion (I) compatibility
    if mbti1[0] == mbti2[0]:
        score += 1
    else:
        score += 0.5

    # Sensing (S) - Intuition (N) compatibility
    if mbti1[1] == mbti2[1]:
        score += 1
    else:
        score += 0.5

    # Thinking (T) - Feeling (F) compatibility
    if mbti1[2] == mbti2[2]:
        score += 1
    else:
        score += 0.5

    # Judging (J) - Perceiving (P) compatibility
    if mbti1[3] == mbti2[3]:
        score += 1
    else:
        score += 0.5

    compatibility = (score / 4) * 100
    return compatibility
