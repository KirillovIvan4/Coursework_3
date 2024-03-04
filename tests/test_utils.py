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