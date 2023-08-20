34.125.251.54

# TODO

- [x] aimysql과 fastapi 연결
- [] user 테이블 생성, crud 기능
- [] test code 작성
- [] docker-compose 작성
- [] 기타 설정 (pytest, makefile, health_check, logging, exception 등등)
- [] 기능 개발 <- 여기서 항상 막혔음
- [] alembic
- [] teamhide 코드 보고 리팩토링 (후순위)

----
1. from contextvars import ContextVar, Token
    https://chat.openai.com/c/ed2148b1-9ce3-4b6d-babc-360748bd06a4#none
2. from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_scoped_session,
)
3. session_context: ContextVar[str] = ContextVar("session_context")
4. __getattr__
    https://chat.openai.com/?model=text-davinci-002-render-sha