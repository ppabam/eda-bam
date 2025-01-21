from eda_bam.cli import group_by_count

def test_group_by_count():
    keyword = "평화"
    asc = False
    rcnt = 12
    group_by_count(keyword, asc, rcnt)
    assert True