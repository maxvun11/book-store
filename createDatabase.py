import sqlite3
db = sqlite3.connect('db.sqlite')

db.execute('''CREATE TABLE books(
    book_id integer PRIMARY KEY,
    name text NOT NULL,
    author text NOT NULL,
    description text NOT NULL,
    availability BOOLEAN NOT NULL
)''')

cursor = db.cursor()

cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("To Kill a Mockingbird", "Harper Lee", "A classic novel about racial injustice and moral growth.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("1984", "George Orwell", "A dystopian novel depicting a totalitarian regime.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Great Gatsby", "F. Scott Fitzgerald", "A story of wealth, excess, and the American Dream.", 0)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("Pride and Prejudice", "Jane Austen", "A classic tale of love and social class in 19th-century England.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Hobbit", "J.R.R. Tolkien", "An adventure in Middle-earth with hobbits, dwarves, and a dragon.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "The first book in the magical Harry Potter series.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Catcher in the Rye", "J.D. Salinger", "A coming-of-age novel following Holden Caulfield.", 0)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Lord of the Rings", "J.R.R. Tolkien", "A high-fantasy epic with hobbits, wizards, and a powerful ring.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("Moby-Dick", "Herman Melville", "The epic tale of Captain Ahab's quest for the white whale.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("Brave New World", "Aldous Huxley", "A futuristic dystopian society with genetic engineering and social control.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Odyssey", "Homer", "The epic journey of Odysseus as he tries to return home.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Road", "Cormac McCarthy", "A post-apocalyptic father-son journey through a desolate landscape.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("War and Peace", "Leo Tolstoy", "A sweeping epic set during the Napoleonic Wars.", 0)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("Jane Eyre", "Charlotte Brontë", "The story of an orphaned governess and her turbulent romance.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Shining", "Stephen King", "A psychological horror novel set in an isolated hotel.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Hunger Games", "Suzanne Collins", "A dystopian adventure featuring the deadly Hunger Games.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Alchemist", "Paulo Coelho", "A philosophical novel about a shepherd's quest for treasure.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Martian", "Andy Weir", "A science fiction novel about an astronaut stranded on Mars.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Catcher in the Rye", "J.D. Salinger", "A coming-of-age novel following Holden Caulfield.", 0)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("Crime and Punishment", "Fyodor Dostoevsky", "A psychological novel that delves into the mind of a young student who commits a murder and grapples with the moral and psychological consequences.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Grapes of Wrath", "John Steinbeck", "A powerful novel that follows the Joad family as they struggle through the hardships of the Great Depression and the Dust Bowl era while searching for a better life in California.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("One Hundred Years of Solitude", "Gabriel García Márquez", "A magical realist masterpiece that spans generations, telling the story of the Buendía family in the fictional town of Macondo, blending history and mythology.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Picture of Dorian Gray", "Oscar Wilde", "A novel about a man named Dorian Gray, who remains youthful while a portrait of him ages, exploring themes of morality and the consequences of one's actions.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Adventures of Sherlock Holmes", "Arthur Conan Doyle", "A collection of detective stories featuring the brilliant detective Sherlock Holmes and his loyal friend Dr. John Watson as they solve complex cases in Victorian London.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Road Not Taken and Other Poems", "Robert Frost", "A collection of poems by Robert Frost, including the famous poem 'The Road Not Taken,' which explores choices and paths in life.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Old Man and the Sea", "Ernest Hemingway", "A novella that tells the story of an aging Cuban fisherman's epic battle with a giant marlin in the Gulf Stream.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Brothers Karamazov", "Fyodor Dostoevsky", "A novel that delves into the philosophical and moral dilemmas faced by the Karamazov brothers, exploring themes of faith, doubt, and the nature of evil.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Divine Comedy", "Dante Alighieri", "An epic poem divided into three parts—Inferno, Purgatorio, and Paradiso—that follows Dante's journey through Hell, Purgatory, and Heaven, exploring themes of sin, redemption, and divine love.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Stranger", "Albert Camus", "A philosophical novel that tells the story of Meursault, an emotionally detached French Algerian, and explores themes of absurdity, existentialism, and the meaning of life.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Iliad", "Homer", "An ancient Greek epic poem that narrates the events of the Trojan War, featuring heroes like Achilles and Hector and exploring themes of honor, heroism, and fate.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Odyssey", "Homer", "The epic journey of Odysseus as he tries to return home after the Trojan War, encountering mythical creatures and challenges along the way.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("Les Misérables", "Victor Hugo", "A novel that follows the lives of several characters in 19th-century France, including the ex-convict Jean Valjean, and explores themes of justice, love, and redemption.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("Frankenstein", "Mary Shelley", "A novel that tells the story of Victor Frankenstein, a scientist who creates a living being through an unconventional scientific experiment, leading to tragic consequences.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("Wuthering Heights", "Emily Brontë", "A novel that explores the passionate and destructive love between Catherine Earnshaw and Heathcliff on the wild and windswept Yorkshire moors.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("Great Expectations", "Charles Dickens", "A novel that follows the life of Pip, an orphan who receives a mysterious inheritance and navigates the challenges of Victorian society.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Scarlet Letter", "Nathaniel Hawthorne", "A novel set in 17th-century Puritan Massachusetts that tells the story of Hester Prynne, who is shamed for bearing an illegitimate child and wears a scarlet letter 'A' as a symbol of her sin.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("The Metamorphosis", "Franz Kafka", "A novella that tells the story of Gregor Samsa, who wakes up one morning to find himself transformed into a giant insect, exploring themes of alienation and identity.", 1)''')
cursor.execute('''INSERT INTO books(name, author, description, availability) VALUES("Heart of Darkness", "Joseph Conrad", "A novella that explores the dark and mysterious journey of Marlow as he travels up the Congo River into the heart of Africa, confronting the brutality of colonialism.", 1)''')


db.commit()
db.close()