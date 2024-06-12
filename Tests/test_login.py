from login import login

def test_login():
    assert login("user1234pasc", "1112224jgt") == True
    assert login("elwdfhue", "1skk23¿?¿") == True
    assert login("sdkl", "estoklj") == False
    assert login("9459b93", "dgsehgl¿?") == False
    assert login("odddoes", "skkdpvpeb") == False