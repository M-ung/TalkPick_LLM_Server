import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.domain.member.type.gender import Gender
from app.domain.member.type.mbti import MBTI
from app.domain.topic.type.keyword import Keyword
from app.domain.topic.type.category_group import CategoryGroup

@pytest.fixture
def client():
    return TestClient(app)

def test_recommend_topics(client):
    # 테스트용 요청 데이터
    request_data = {
        "mbti": "ENFP",
        "gender": "FEMALE",
        "age": 25,
        "previous_topics": [
            {
                "id": 1,
                "title": "여행",
                "detail": "좋아하는 여행지",
                "keyword": "TRAVEL",
                "category_group": "LIFESTYLE",
                "category": "여행"
            }
        ],
        "available_topics": [
            {
                "topic_id": 2,
                "topic_title": "음식",
                "topic_detail": "좋아하는 음식",
                "topic_thumbnail": "food.jpg",
                "topic_icon": "food_icon.png",
                "category_title": "음식",
                "category_description": "다양한 음식 이야기",
                "category_image_url": "food_category.jpg",
                "category_group": "LIFESTYLE",
                "keyword": "FOOD",
                "e_count": 10,
                "i_count": 5,
                "s_count": 8,
                "n_count": 7,
                "f_count": 12,
                "t_count": 3,
                "j_count": 6,
                "p_count": 9,
                "teen_count": 2,
                "twenties_count": 8,
                "thirties_count": 4,
                "forties_count": 1,
                "fifties_count": 0,
                "male_count": 7,
                "female_count": 8
            },
            # ... 더 많은 토픽 데이터 추가
        ]
    }

    # API 호출
    response = client.post("/api/v1/topics/recommend", json=request_data)
    
    # 응답 검증
    assert response.status_code == 200
    data = response.json()
    assert "topics" in data
    assert len(data["topics"]) == 4  # 4개의 주제가 추천되어야 함
    
    # 각 주제의 필수 필드 검증
    for topic in data["topics"]:
        assert "order" in topic
        assert "topic_id" in topic
        assert "category" in topic
        assert "image_url" in topic
        assert "keyword" in topic
        assert "thumbnail" in topic
        assert "icon" in topic

def test_recommend_topics_insufficient(client):
    # 토픽이 부족한 경우 테스트
    request_data = {
        "mbti": "ENFP",
        "gender": "FEMALE",
        "age": 25,
        "previous_topics": [],
        "available_topics": [
            {
                "topic_id": 1,
                "topic_title": "음식",
                "topic_detail": "좋아하는 음식",
                "topic_thumbnail": "food.jpg",
                "topic_icon": "food_icon.png",
                "category_title": "음식",
                "category_description": "다양한 음식 이야기",
                "category_image_url": "food_category.jpg",
                "category_group": "LIFESTYLE",
                "keyword": "FOOD",
                "e_count": 10,
                "i_count": 5,
                "s_count": 8,
                "n_count": 7,
                "f_count": 12,
                "t_count": 3,
                "j_count": 6,
                "p_count": 9,
                "teen_count": 2,
                "twenties_count": 8,
                "thirties_count": 4,
                "forties_count": 1,
                "fifties_count": 0,
                "male_count": 7,
                "female_count": 8
            }
        ]
    }

    response = client.post("/api/v1/topics/recommend", json=request_data)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    assert data["error"]["code"] == "INSUFFICIENT_TOPICS" 