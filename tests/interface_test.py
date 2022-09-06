import subprocess

import requests

PATH_TO_WEBCALCULATOR = "C:\\Python\\infotecs_test_task\\resorces\\webcalculator.exe"

def setup_module():
    '''Запуск вебкалькулятора.'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "start"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def teardown_module():
    '''Остановка вебкалькулятора.'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def test_GetRequestStateApiFunction_ReturnCorrectJson():
    response_body = requests.get(
        url='http://127.0.0.1:17678/api/state',
        timeout=1.5).json()
    assert len(response_body) == 2
    assert response_body["statusCode"] == 0
    assert response_body["state"] == "OK"


def test_PostRequestAdditionApiFunction_ReturnCorrectJson():
    response_body = requests.post(
        url='http://127.0.0.1:17678/api/addition',
        json={"x": 1, "y": 2}, timeout=1.5).json()
    assert len(response_body) == 2
    assert response_body["statusCode"] == 0
    assert isinstance(response_body["result"], int)


def test_PostRequestMultiplication_ReturnCorrectJson():
    response_body = requests.post(
        url='http://127.0.0.1:17678/api/multiplication',
        json={"x": 1, "y": 2}, timeout=1.5).json()
    assert len(response_body) == 2
    assert response_body["statusCode"] == 0
    assert isinstance(response_body["result"], int)


def test_PostRequestDivision_ReturnCorrectJson():
    response_body = requests.post(
        url='http://127.0.0.1:17678/api/division',
        json={"x": 1, "y": 2}, timeout=1.5).json()
    assert len(response_body) == 2
    assert response_body["statusCode"] == 0
    assert isinstance(response_body["result"], int)


def test_PostRequestRemainder_ReturnCorrectJson():
    response_body = requests.post(
        url='http://127.0.0.1:17678/api/remainder',
        json={"x": 1, "y": 2}, timeout=1.5).json()
    assert len(response_body) == 2
    assert response_body["statusCode"] == 0
    assert isinstance(response_body["result"], int)


