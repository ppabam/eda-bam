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


eda-bam 자유 --asc --rcnt 5
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
