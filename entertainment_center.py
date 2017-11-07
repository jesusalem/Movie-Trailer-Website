import fresh_tomatoes
import media

#Set the attributes for each of the movies
xmen = media.Movie("X-Men: First Class",
                   "In the early 1960s, during the height of the Cold War, a mutant named Charles Xavier (James McAvoy) meets a fellow mutant named Erik Lehnsherr (Michael Fassbender)",
                   "https://upload.wikimedia.org/wikipedia/en/5/55/X-MenFirstClassMoviePoster.jpg",
                   "https://www.youtube.com/watch?v=kyQKi5-k0UU")

xmen_2 = media.Movie("X-Men: Days of Future",
                     "Convinced that mutants pose a threat to humanity, Dr. Bolivar Trask (Peter Dinklage) develops the Sentinels, enormous robotic weapons that can detect a mutant gene and zero in on that person.",
                     "https://upload.wikimedia.org/wikipedia/en/0/0c/X-Men_Days_of_Future_Past_poster.jpg",
                     "https://www.youtube.com/watch?v=pK2zYHWDZKo")

xmen_3 = media.Movie("X-Men: Apocalypse",
                     "En Sabah Nur, a powerful mutant believed to be the first of his kind, rules ancient Egypt until he is betrayed by his worshippers, who entomb him alive",
                     "https://upload.wikimedia.org/wikipedia/en/0/04/X-Men_-_Apocalypse.jpg",
                     "https://www.youtube.com/watch?v=COvnHv42T-A")

logan = media.Movie("Logan",
                    "Logan's healing ability has weakened and he has aged; he spends his days drinking and working as a limo driver in El Paso, Texas.",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

ghost_shell = media.Movie("Ghost in the Shell",
                          "In the near future, most humans are augmented with cybernetic improvements to traits such as vision, strength, and intelligence. ",
                          "https://upload.wikimedia.org/wikipedia/en/1/11/Ghost_in_the_Shell_%282017_film%29.png",
                          "https://www.youtube.com/watch?v=G4VmJcZR0Yg")

dragon_ball_z = media.Movie("Dragon Ball Z: Resurrection 'F'",
                            "The remnants of Frieza's army, led by an alien named Sorbet, head to Earth to collect the Dragon Balls, to summon the wish-granting dragon Shenron.",
                            "https://upload.wikimedia.org/wikipedia/en/6/6a/DBZ_THE_MOVIE_NO._15.png",
                            "https://www.youtube.com/watch?v=WiONylGn8Xw")

#Create the list of movies
movies = [xmen,xmen_2,xmen_3,logan,ghost_shell,dragon_ball_z]

#Open the movie page with the movies list
fresh_tomatoes.open_movies_page(movies)
