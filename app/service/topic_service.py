from typing import List
from ..dto.request.topic_req_dto import TopicReqDTO
from ..dto.response.topic_res_dto import TopicResDTO, RandomTopic

class TopicService:
    def __init__(self):
        self.llm = self._initialize_llm()

    def _initialize_llm(self):
        # TODO: Llama 2 모델 초기화 로직 구현
        pass

    async def recommend(self, request: TopicReqDTO) -> TopicResDTO:
        # 1. 이전 주제 ID 제외
        used_topic_ids = {topic.id for topic in request.previous_topics}
        available_topics = [
            topic for topic in request.available_topics 
            if topic.topic_id not in used_topic_ids
        ]

        # 2. LLM 프롬프트 생성
        prompt = f"""
        당신은 대화 주제 추천 전문가입니다. 다음 사용자 특성과 대화 맥락을 고려하여 가장 적합한 주제 4개를 추천해주세요.

        [사용자 정보]
        - MBTI: {request.mbti}
        - 성별: {request.gender}
        - 나이: {request.age}

        [이전 대화 주제들]
        {self._format_previous_topics(request.previous_topics)}

        [선택 가능한 주제 목록]
        {self._format_available_topics(available_topics)}

        다음 기준으로 가장 적합한 주제 4개의 topic_id를 선택해주세요:
        1. 사용자의 MBTI 성향과 통계적 선호도 매칭
        2. 사용자의 연령대와 성별 통계 고려
        3. 이전 대화 주제들과의 자연스러운 연결성
        4. 대화의 다양성과 흥미 유지

        응답 형식: topic_id만 쉼표로 구분 (예: 1,4,7,12)
        """

        # 3. LLM으로 주제 선택
        selected_ids = self._get_topic_ids_from_llm(
            self.llm.generate(prompt)
        )

        # 4. 선택된 주제로 응답 생성
        recommended_topics = []
        for order, topic_id in enumerate(selected_ids, 1):
            topic = next(t for t in available_topics if t.topic_id == topic_id)
            recommended_topics.append(
                RandomTopic(
                    order=order,
                    topic_id=topic.topic_id,
                    category=topic.category_title,
                    image_url=topic.category_image_url or "",
                    keyword=topic.keyword.value,
                    thumbnail=topic.topic_thumbnail or "",
                    icon=topic.topic_icon or ""
                )
            )

        return TopicResDTO(topics=recommended_topics)

    def _format_previous_topics(self, previous_topics: List[TopicReqDTO.PreviousTopicData]) -> str:
        if not previous_topics:
            return "이전 대화 주제 없음"
        
        return "\n".join([
            f"- 주제: {topic.title}\n"
            f"  설명: {topic.detail}\n"
            f"  키워드: {topic.keyword.value}\n"
            f"  카테고리: {topic.category_group.value}/{topic.category}"
            for topic in previous_topics
        ])

    def _format_available_topics(self, topics: List[TopicReqDTO.TopicData]) -> str:
        return "\n".join([
            f"ID: {topic.topic_id}\n"
            f"제목: {topic.topic_title}\n"
            f"설명: {topic.topic_detail}\n"
            f"키워드: {topic.keyword.value}\n"
            f"카테고리: {topic.category_group.value}/{topic.category_title}\n"
            f"MBTI 통계: E({topic.e_count})/I({topic.i_count}), "
            f"S({topic.s_count})/N({topic.n_count}), "
            f"F({topic.f_count})/T({topic.t_count}), "
            f"J({topic.j_count})/P({topic.p_count})\n"
            f"연령대 통계: 10대({topic.teen_count}), 20대({topic.twenties_count}), "
            f"30대({topic.thirties_count}), 40대({topic.fortiesCount}), "
            f"50대({topic.fifties_count})\n"
            f"성별 통계: 남성({topic.male_count}), 여성({topic.female_count})\n"
            for topic in topics
        ])

    def _get_topic_ids_from_llm(self, llm_response: str) -> List[int]:
        try:
            ids = [int(id.strip()) for id in llm_response.strip().split(',')]
            if len(ids) != 4:
                raise ValueError("Must select exactly 4 topics")
            return ids
        except Exception as e:
            raise ValueError(f"Failed to parse LLM response: {e}") 