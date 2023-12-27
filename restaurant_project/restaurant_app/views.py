from django.shortcuts import render

meals = [
    {
        "strMeal": "BeaverTails",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
        "idMeal": "52928",
        "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
    },
    {
        "strMeal": "Breakfast Potatoes",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
        "idMeal": "52965",
        "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
    },
    {
        "strMeal": "Canadian Butter Tarts",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
        "idMeal": "52923",
        "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
    },
    {
        "strMeal": "Montreal Smoked Meat",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
        "idMeal": "52927",
        "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
    },
    {
        "strMeal": "Nanaimo Bars",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
        "idMeal": "52924",
        "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
    },
    {
        "strMeal": "Pate Chinois",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
        "idMeal": "52930",
        "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
    },
    {
        "strMeal": "Pouding chomeur",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
        "idMeal": "52932",
        "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
    },
    {
        "strMeal": "Poutine",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
        "idMeal": "52804",
        "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
    },
    {
        "strMeal": "Rappie Pie",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
        "idMeal": "52933",
        "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
    },
    {
        "strMeal": "Split Pea Soup",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
        "idMeal": "52925",
        "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
    },
    
]

def home(request):
    return render(request, 'index.html', {'meals': meals})
