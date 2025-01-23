from president_speech.db.parquet_interpreter import get_parquet_full_path
import pandas as pd
import typer

def add_keyword_count(df: pd.DataFrame, keyword: str) -> pd.DataFrame:
    """
    DataFrame에 keyword_count 컬럼을 추가하여 반환합니다.
    각 speech_text에서 keyword가 등장하는 횟수를 계산합니다.
    """
    # keyword_count 컬럼 추가
    df['keyword_count'] = df['speech_text'].str.count(keyword)
    return df

def group_by_count(keyword: str, asc: bool=False, rcnt: int=12, keyword_sum: bool=False) -> pd.DataFrame:
    # TODO: ascending, 출력 rows size
    # pytest 코드를 만들어 보세요
    # import this <- 해석해보세요
    data_path = get_parquet_full_path()
    df = pd.read_parquet(data_path)
    fdf = df[df['speech_text'].str.contains(keyword, case=False)]

    if(keyword_sum):
        #fdf['keyword_sum'] == '사표는 책상위에 올려두었습니다'
        pass

    gdf = fdf.groupby("president").size().reset_index(name="count")
    sdf = gdf.sort_values(by='count', ascending=asc).reset_index(drop=True)
    rdf = sdf.head(rcnt)
    rdf['keyword_sum'] = '부장이면다냐!'
    return rdf

def print_group_by_count(keyword: str, asc: bool=False, rcnt: int=12):
    df = group_by_count(keyword, asc, rcnt)
    print(df.to_string(index=False))


def entry_point():
    typer.run(print_group_by_count)

