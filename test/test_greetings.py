from py_trace_image import greetings

def test_hello_world():
    output = greetings.hello_world()
    assert output == "Hello World"