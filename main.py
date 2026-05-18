import turtle

# Chaque planète a une couleur d'accent (sol) et une couleur de fond sombre (bg)
planetes = [
    {"nom": "Mercure", "masse": "3.30 x 10^23", "rayon": 2439, "g": 3.70, "color": "#a3a3a3", "bg": "#1a1a1a"},
    {"nom": "Vénus",   "masse": "4.87 x 10^24", "rayon": 6051, "g": 8.87, "color": "#fcd34d", "bg": "#2e1a05"},
    {"nom": "Terre",   "masse": "5.97 x 10^24", "rayon": 6371, "g": 9.81, "color": "#60a5fa", "bg": "#0f172a"},
    {"nom": "Lune",    "masse": "7.34 x 10^22", "rayon": 1737, "g": 1.62, "color": "#d1d5db", "bg": "#111827"},
    {"nom": "Mars",    "masse": "6.42 x 10^23", "rayon": 3389, "g": 3.71, "color": "#f87171", "bg": "#2a0a0a"},
    {"nom": "Jupiter", "masse": "1.90 x 10^27", "rayon": 69911,"g": 24.79,"color": "#fbbf24", "bg": "#2c1505"},
    {"nom": "Saturne", "masse": "5.68 x 10^26", "rayon": 58232,"g": 10.44,"color": "#fef08a", "bg": "#242005"},
    {"nom": "Uranus",  "masse": "8.68 x 10^25", "rayon": 25362,"g": 8.87, "color": "#22d3ee", "bg": "#08202a"},
    {"nom": "Neptune", "masse": "1.02 x 10^26", "rayon": 24622,"g": 11.15,"color": "#3b82f6", "bg": "#051024"}
]

index = 0
masse_balle = 0.058  # 58 grammes

ecran = turtle.Screen()
ecran.setup(width=800, height=900) # Taille de fenêtre classique et harmonieuse
ecran.title("Forces de gravité (Appuyez sur ESPACE)")

t = turtle.Turtle()
t.hideturtle()

def dessiner_fleche(x, y, angle, longueur, couleur, texte):
    t.penup()
    t.goto(x, y)
    t.color(couleur)
    t.pensize(3)
    t.setheading(angle)
    t.pendown()
    t.forward(longueur)
    
    t.left(150)
    t.forward(12)
    t.backward(12)
    t.right(300)
    t.forward(12)
    t.backward(12)
    t.setheading(angle)
    
    t.penup()
    t.forward(20)
    t.write(texte, align="center", font=("Arial", 14, "bold"))

def dessiner():
    ecran.tracer(0)
    t.clear()
    
    p = planetes[index]
    poids = masse_balle * p["g"]
    
    # 0. Changer dynamiquement la couleur d'arrière-plan !
    ecran.bgcolor(p["bg"])
    
    # 1. Le Sol
    t.penup()
    t.goto(-400, -100)
    t.pendown()
    t.setheading(0)
    t.pensize(4)
    t.color(p["color"])
    t.forward(800)
    
    t.pensize(2)
    for i in range(-400, 400, 30):
        t.penup()
        t.goto(i, -100)
        t.pendown()
        t.goto(i - 15, -120)
    
    # 2. La Balle
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.color("#a3e635")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    t.penup()
    t.goto(0, -60)
    t.color("black")
    t.dot(6)

    # Longueur des flèches ajustée pour ne pas se chevaucher
    longueur = p["g"] * 12 + 40

    dessiner_fleche(0, -60, 270, longueur, "#ef4444", f"P = {poids:.2f} N")
    dessiner_fleche(0, -100, 90, longueur, "#3b82f6", f"R = {poids:.2f} N")

    texte = (
        f"PLANÈTE : {p['nom']}\n"
        f"Masse   : {p['masse']} kg\n"
        f"Rayon   : {p['rayon']} km\n"
        f"Gravité : {p['g']} m/s²\n\n"
        f"BALLE :\n"
        f"Masse : {masse_balle} kg\n"
        f"Poids : {poids:.2f} N\n\n"
        f"[Appuyez sur ESPACE]"
    )
    t.penup()
    t.goto(-350, 300) # Remonté pour utiliser l'espace supplémentaire de 900px
    t.color("white")
    t.write(texte, font=("Courier", 14, "bold"))
    
    ecran.update()

def changer_planete():
    global index
    index = (index + 1) % len(planetes)
    dessiner()

dessiner()
ecran.onkey(changer_planete, "space")
ecran.listen()
turtle.done()