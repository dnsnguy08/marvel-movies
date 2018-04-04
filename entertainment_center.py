import media
import fresh_tomatoes

black_panther = media.Movie("Black Panther", "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg", "https://www.youtube.com/watch?v=xjDjIWPwcPU")

avengers_infinity = media.Movie("Avengers: Infinity War", "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg", "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

avengers_ultron = media.Movie("Avengers: Age of Ultron", "https://upload.wikimedia.org/wikipedia/en/f/ff/Avengers_Age_of_Ultron_poster.jpg", "https://www.youtube.com/watch?v=tmeOjFno6Do")

avengers = media.Movie("Marvel's The Avengers", "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg", "https://www.youtube.com/watch?v=eOrNdBpGMv8")

iron_man_3 = media.Movie("Iron Man 3", "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg", "https://www.youtube.com/watch?v=YLorLVa95Xo")

iron_man_2 = media.Movie("Iron Man 2", "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg", "https://www.youtube.com/watch?v=BoohRoVA9WQ")

iron_man = media.Movie("Iron Man", "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG", "https://www.youtube.com/watch?v=8hYlB38asDY")

spider_man = media.Movie("Spider-Man: Homecoming", "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg", "https://www.youtube.com/watch?v=n9DwoQ7HWvI")

guardians_gal_2 = media.Movie("Guardians of the Galaxy Vol. 2", "https://upload.wikimedia.org/wikipedia/en/a/ab/Guardians_of_the_Galaxy_Vol_2_poster.jpg", "https://www.youtube.com/watch?v=dW1BIid8Osg")

guardians = media.Movie("Guardians of the Galaxy", "https://upload.wikimedia.org/wikipedia/en/b/b5/Guardians_of_the_Galaxy_poster.jpg","https://www.youtube.com/watch?v=d96cjJhvlMA&t=8s")

doctor_strange = media.Movie("Doctor Strange", "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg", "https://www.youtube.com/watch?v=HSzx-zryEgM")

ant_man_wasp = media.Movie("Ant-Man and The Wasp", "https://upload.wikimedia.org/wikipedia/en/2/2c/Ant-Man_and_the_Wasp_poster.jpg", "https://www.youtube.com/watch?v=8_rTIAOohas")

ant_man = media.Movie("Ant-Man", "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg", "https://www.youtube.com/watch?v=pWdKf3MneyI")

thor_ragnarok = media.Movie("Thor: Ragnarok", "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg", "https://www.youtube.com/watch?v=ue80QwXMRHg")

thor_2 = media.Movie("Thor: The Dark World", "https://upload.wikimedia.org/wikipedia/en/7/7e/Thor_-_The_Dark_World_poster.jpg", "https://www.youtube.com/watch?v=npvJ9FTgZbM")

thor = media.Movie("Thor", "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg", "https://www.youtube.com/watch?v=JOddp-nlNvQ")

ca_civil_war = media.Movie("Captain America: Civil War", "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg","https://www.youtube.com/watch?v=dKrVegVI0Us")

ca_winter_soldier = media.Movie("Captain America: The Winter Soldier", 
	"https://upload.wikimedia.org/wikipedia/en/e/e8/Captain_America_The_Winter_Soldier.jpg", "https://www.youtube.com/watch?v=tbayiPxkUMM")

captain_america = media.Movie("Captain America: The First Avenger", "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg", "https://www.youtube.com/watch?v=JerVrbLldXw")

incredible_hulk = media.Movie("The Incredible Hulk", "https://upload.wikimedia.org/wikipedia/en/8/88/The_Incredible_Hulk_poster.jpg", "https://www.youtube.com/watch?v=xbqNb2PFKKA")

movies = [black_panther, avengers_infinity, avengers_ultron, avengers, iron_man_3, iron_man_2, iron_man, spider_man, guardians_gal_2, guardians, doctor_strange, ant_man_wasp, ant_man, thor_ragnarok, thor_2, thor, ca_civil_war, ca_winter_soldier, captain_america, incredible_hulk]

fresh_tomatoes.open_movies_page(movies)


