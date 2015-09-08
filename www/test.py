import uuid, time

t = time.time()
print '%015d%s000' % (int(t * 1000), uuid.uuid4().hex)
print '%015d' % int(t * 1000)
print uuid.uuid4().hex