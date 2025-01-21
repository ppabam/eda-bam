# eda-bam
![LGTM](https://i.lgtm.fun/2vtm.png)

### Use
```bash
eda-bam --help
                                                                                                  
 Usage: eda-bam [OPTIONS] KEYWORD                                                                 
                                                                                                  
 지정한 keyword로 필터링하여 대통령별로 그룹화하고, count를 기준으로 정렬하여 출력합니다.         
                                                                                                  
╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────╮
│ *    keyword      TEXT  [default: None] [required]                                             │
╰────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────╮
│ --asc     --no-asc             [default: no-asc]                                               │
│ --rcnt                INTEGER  [default: 12]                                                   │
│ --help                         Show this message and exit.                                     │
╰────────────────────────────────────────────────────────────────────────────────────────────────╯


$ eda-bam 자유
president  count
      박정희    513
      이승만    438
      노태우    399
      김대중    305
      문재인    275
      김영삼    274
      이명박    262
      전두환    242
      노무현    230
      박근혜    111
      최규하     14
      윤보선      1


eda-bam 자유 --asc --rcnt 3
president  count
      윤보선      1
      최규하     14
      박근혜    111
      노무현    230
      전두환    242
```

### DEV
```bash
$ source .venv/bin/activate
$ pdm add pandas
$ pdm add -dG eda jupyterlab
```
### EDA
- run jupyterlab
```
$ jupyter lab
```
### Ref
- [install jupyterlab](https://jupyter.org/install)
- https://pypi.org/project/president-speech/


### Test
```python
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
```
