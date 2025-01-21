from eda_bam.cli import group_by_count
import pandas as pd

def test_group_by_count():
    search_word = "자유"
    asc = True
    rcnt = 3
    result_df = group_by_count(keyword=search_word, asc=asc, rcnt=3)
    
    # Assertions
    # 1. 총 행 수 확인
    assert len(result_df) == rcnt  # "economy" 키워드는 President A와 B에 해당

    # 2. 첫 행의 값 확인 (count 기준으로 내림차순 정렬)
    assert result_df.iloc[0]["president"] == "윤보선"
    assert result_df.iloc[0]["count"] == 1

    # 3. 반환 타입 확인
    assert isinstance(result_df, pd.DataFrame)

    # 4. 컬럼 이름 확인
    assert list(result_df.columns) == ["president", "count"]