import eltacourier

ec = eltacourier.EltaCourier()

print(ec.track(
    number="NUMBER"
))

print(ec.track(
    number=[
        "NUMBER1",
        "NUMBER2",
        "NUMBER3"
    ]
))