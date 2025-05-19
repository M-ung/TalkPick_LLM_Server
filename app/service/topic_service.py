from typing import List
import random
import os
from llama_cpp import Llama
from ..dto.request.topic_req_dto import TopicReqDTO
from ..dto.response.topic_res_dto import TopicResDTO, RandomTopic
from ..common.exception.topic_exception import TopicException, ErrorCode
from ..common.config.settings import get_settings

class TopicService:
    def __init__(self):
        self.settings = get_settings()
        self.llm = self._initialize_llm()

    def _initialize_llm(self) -> Llama:
        try:
            if not os.path.exists(self.settings.MODEL_PATH):
                raise TopicException(
                    ErrorCode.INTERNAL_SERVER_ERROR,
                    f"모델 파일을 찾을 수 없습니다: {self.settings.MODEL_PATH}"
                )

            return Llama(
                model_path=self.settings.MODEL_PATH,
                temperature=self.settings.MODEL_TEMPERATURE,
                max_tokens=self.settings.MODEL_MAX_TOKENS,
                n_ctx=self.settings.MODEL_CONTEXT_LENGTH,
                n_threads=self.settings.MODEL_THREADS
            )
        except Exception as e:
            raise TopicException(
                ErrorCode.INTERNAL_SERVER_ERROR,
                f"LLM 초기화 중 오류가 발생했습니다: {str(e)}"
            )

    async def recommend(self, request: TopicReqDTO) -> TopicResDTO:
        try:
            # 1. 사용 가능한 토픽이 충분한지 확인
            if len(request.available_topics) < 4:
                raise TopicException(
                    ErrorCode.INSUFFICIENT_TOPICS,
                    f"사용 가능한 주제가 {len(request.available_topics)}개 뿐입니다."
                )

            # 2. 이전 주제 ID 제외
            used_topic_ids = {topic.id for topic in request.previous_topics}
            available_topics = [
                topic for topic in request.available_topics 
                if topic.topic_id not in used_topic_ids
            ]

            if len(available_topics) < 4:
                return await self._fallback_random_recommendation(available_topics)

            # 3. LLM 프롬프트 생성 및 추천
            try:
                prompt = self._create_recommendation_prompt(request, available_topics)
                selected_ids = self._get_topic_ids_from_llm(
                    self.llm.generate(prompt)
                )
            except Exception as e:
                # LLM 실패시 fallback
                return await self._fallback_random_recommendation(available_topics)

            # 4. 선택된 주제로 응답 생성
            recommended_topics = []
            for order, topic_id in enumerate(selected_ids, 1):
                try:
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
                except StopIteration:
                    # 잘못된 topic_id가 선택된 경우 fallback
                    return await self._fallback_random_recommendation(available_topics)

            return TopicResDTO(topics=recommended_topics)

        except TopicException:
            raise
        except Exception as e:
            raise TopicException(
                ErrorCode.INTERNAL_SERVER_ERROR,
                f"주제 추천 중 오류가 발생했습니다: {str(e)}"
            )

    def _get_topic_ids_from_llm(self, llm_response: str) -> List[int]:
        try:
            ids = [int(id.strip()) for id in llm_response.strip().split(',')]
            if len(ids) != 4:
                raise TopicException(
                    ErrorCode.LLM_RESPONSE_PARSING_ERROR,
                    "LLM이 정확히 4개의 주제를 선택하지 않았습니다."
                )
            return ids
        except Exception as e:
            raise TopicException(
                ErrorCode.LLM_RESPONSE_PARSING_ERROR,
                f"LLM 응답 파싱 중 오류: {str(e)}"
            )

    async def _fallback_random_recommendation(self, available_topics: List[TopicReqDTO.TopicData]) -> TopicResDTO:
        """LLM 추천 실패시 랜덤 추천 fallback"""
        selected_topics = random.sample(available_topics, min(4, len(available_topics)))
        recommended_topics = [
            RandomTopic(
                order=order,
                topic_id=topic.topic_id,
                category=topic.category_title,
                image_url=topic.category_image_url or "",
                keyword=topic.keyword.value,
                thumbnail=topic.topic_thumbnail or "",
                icon=topic.topic_icon or ""
            )
            for order, topic in enumerate(selected_topics, 1)
        ]
        return TopicResDTO(topics=recommended_topics)