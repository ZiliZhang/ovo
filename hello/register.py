from hello.models import User

p = User(email='abc.com', first_name='jason', last_name='kim', username='dongkyu',
	password='mchacks', birth_date='1993-12-15', gender='male', age='22')
p.save()
