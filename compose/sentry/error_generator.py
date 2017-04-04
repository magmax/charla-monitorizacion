from raven import Client

client = Client('http://1cb6587438054807b58ccedb0e593776:c8acbb8e651b45aeb11b251fa3150af5@localhost:10020/2', release="0.0.2")

client.captureMessage("Saludo 2", level="debug", tags=dict(whatever="value"), extra=dict(foo="bar"))

d = 0
n = 1


try:
    n / d
except ZeroDivisionError:
    client.captureException()
