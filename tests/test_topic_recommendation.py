import random
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.domain.member.type.gender import Gender
from app.domain.member.type.mbti import MBTI
from app.domain.topic.type.keyword import Keyword

@pytest.fixture
def client():
    return TestClient(app)

def generate_dummy_topics():
    titles_and_details = [
        ("만약에 너가 슈퍼 히어로라면?", "어떤 능력을 갖고 어떤 악당을 물리치고 싶어?"),
        ("바람피는 애인 vs 잠수이별", "둘 중 하나만 겪어야 한다면 무엇을 선택할래?"),
        ("머리에 꽃이 핀다면?", "세상 모든 사람이 머리에 꽃을 피우고 다닌다면 어떤 일이 생길까?"),
        ("하루 동안 투명인간이 된다면?", "어디에 가고 누구를 볼 거야?"),
        ("로또 1등에 당첨된다면?", "가장 먼저 무엇을 할 거야?")
    ]

    keywords = [Keyword.FOOD, Keyword.TRAVEL, Keyword.MOVIE, Keyword.HOBBY, Keyword.DREAM]

    dummy_topics = []
    for i, (title, detail) in enumerate(titles_and_details, start=1):
        dummy_topics.append({
            "topic_id": i,
            "topic_title": title,
            "topic_detail": detail,
            "topic_thumbnail": f"thumbnail_{i}.jpg",
            "topic_icon": f"icon_{i}.png",
            "category_title": f"카테고리 {i % 5}",
            "category_description": f"카테고리 {i % 5}에 대한 설명입니다.",
            "category_image_url": f"cat_img_{i}.jpg",
            "keyword": random.choice(keywords).value,
            "e_count": 10,
            "i_count": 10,
            "s_count": 10,
            "n_count": 10,
            "f_count": 10,
            "t_count": 10,
            "j_count": 10,
            "p_count": 10,
            "teen_count": 5,
            "twenties_count": 5,
            "thirties_count": 5,
            "forties_count": 5,
            "fifties_count": 5,
            "male_count": 5,
            "female_count": 5,
        })
    return dummy_topics

def to_previous_format(topic):
    return {
        "id": topic["topic_id"],
        "title": topic["topic_title"],
        "detail": topic["topic_detail"],
        "keyword": topic["keyword"],
        "category": topic["category_title"]
    }

def test_just_show_recommendation_response(client):
    all_topics = generate_dummy_topics()
    previous_topics = [to_previous_format(t) for t in all_topics[:2]]  # 이전 토픽 2개만

    request_data = {
        "mbti": MBTI.ENFP.name,
        "gender": Gender.FEMALE.name,
        "age": 25,
        "previous_topics": previous_topics,
        "available_topics": all_topics
    }

    response = client.post("/api/v1/topics/recommend", json=request_data)
    print("\n✅ 추천 토픽 응답 결과:\n", response.json())