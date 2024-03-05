from utils import utils
def test_get_last_five_operations():
    assert utils.get_last_five_operations([{'date': 2},
                                           {'date': 5},
                                           {'date': 4},
                                           {'date': 1},
                                           {'date': 3}
                                           ]) == [{'date': 1},
                                                  {'date': 2},
                                                  {'date': 3},
                                                  {'date': 4},
                                                  {'date': 5}
  ]
    assert utils.get_last_five_operations([{'date': 2},
                                           {'date': 5},
                                           {'date': 4},
                                           {'date': 6},
                                           {'date': 1},
                                           {'date': 3}
                                           ]) == [{'date': 2},
                                                  {'date': 3},
                                                  {'date': 4},
                                                  {'date': 5},
                                                  {'date': 6}
                                                  ]


def test_formation_date():
    assert utils.formation_date([{'date': "2019-02-14 03:09:23"}]) == [{'date': '14.02.2019'}]