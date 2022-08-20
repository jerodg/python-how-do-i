import faker

fake = faker.Faker(providers=["faker.providers.lorem"])
td = [fake.paragraph(nb_sentences=7, variable_nb_sentences=True) for _ in range(7)]
srch = choice(choice(td).split(" "))
