from president_speech.db.parquet_interpreter import get_parquet_full_path
import pandas as pd
import typer

def group_by_count(keyword: str, asc: bool = False, rcnt: int = 12):
    """
    지정한 keyword로 필터링하여 대통령별로 그룹화하고, count를 기준으로 정렬하여 데이터프레임으로 반환합니다.
    """
    # TODO: ascending, 출력 rows size
    # pytest 코드를 만들어 보세요
    # import this <- 해석해보세요
    data_path = get_parquet_full_path()
    df = pd.read_parquet(data_path)
    fdf = df[df['speech_text'].str.contains(keyword, case=False)]
    gdf = fdf.groupby("president").size().reset_index(name="count")
    sdf = gdf.sort_values(by='count', ascending=asc).reset_index(drop=True)
    
    df = sdf.head(rcnt)
    return df
    
def print_president_speech(keyword: str, asc: bool = False, rcnt: int = 12):
    """
    지정한 keyword로 필터링하여 대통령별로 그룹화하고, count를 기준으로 정렬하여 출력합니다.
    """
    df = group_by_count(keyword, asc, rcnt)
    print(df.to_string(index=False))

def entry_point():
    typer.run(print_president_speech)

