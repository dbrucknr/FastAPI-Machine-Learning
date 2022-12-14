def test_main(test_app_instance):
    response = test_app_instance.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "environment":"dev",
        "testing":False,
        "version":"0.0.1"
    }